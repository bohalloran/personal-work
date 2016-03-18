import logging
from jenkinsapi.jenkins import Jenkins
from time import sleep
import lib.constants


class Build(object):

    def __init__(self):
        # TODO: add logging into a base class
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(levelname)s %(message)s')
        self.jenkins_url = lib.constants.BUILD_SERVER
        self.project_name = 'Build-Apt-Feature-Merge'
        # get username and password from Jenkins/Configure/API Token
        self.username = 'bohalloran@bitsighttech.com'
        self.password = 'a46e9502085ff9f78f3fbdb6b7540a90'
        self.branch = 'fixes/edq/pdnsautomapper-1'
        self.targetbranch = 'master'
        self.si = self.get_server_instance()
        self.job = self.si.get_job(self.project_name)
        self.build_num = self.job.get_next_build_number()
        self.last_build = self.job.get_last_build()
        self.last_build_num = self.job.get_last_completed_buildnumber()
        # don't like this file name needs more info like the date, etc...
        self.build_log_file_name = 'build_log_build_%s' % self.build_num
        self._get_last_build_description()

    def get_server_instance(self):
        # TODO: prompt for password
        logging.info('Connecting to build server %s ...' % self.jenkins_url)
        server_instance = Jenkins(self.jenkins_url,
                                  self.username,
                                  self.password)
        return server_instance

    def build_apt_packages(self):
        # start/create buld job
        # TODO: prompt for 'branch' and 'targetbranch'
        # TODO: run Build.build_apt_packages() and Deploy.get_postgres parallel
        logging.info('Creating build for branch %s ...' % self.branch)
        self.si.build_job(self.project_name,
                          params={'branch': self.branch,
                                  'targetbranch': self.targetbranch})
        # TODO: Need timeout if is_queued_or_running() does not return
        while self.job.is_queued_or_running():
            logging.info('Waiting for build %s to finish ...' % self.build_num)
            sleep(10)
        # TODO: make sure build completed successfully, throws exception?
        # might be better to look at last line of output for SUCCESS/FAILURE
        self._get_last_build_description()
        if int(self.build_num) == int(self.job.get_last_good_buildnumber()):
            logging.info('Finished: SUCCESS')
        else:
            logging.warning('Finished: FAILURE')
        logging.info('Writing build results from console output to %s' %
                     self.build_log_file_name)
        f = open(self.build_log_file_name, 'wb')
        f.write(self.last_build.get_console())
        f.close()

    def _get_last_build_description(self):
        last_build_dict = self.job.get_build_dict()
        log_url = '%sconsoleText' % \
                  last_build_dict[self.last_build_num]
        logging.info('\nBuild Description: %s\nBuild Date: %s'
                     '\nBuild Status: %s\nBuild Logs: %s' %
                     (str(self.last_build), self.last_build.get_timestamp(),
                      self.last_build.get_status(), log_url))
