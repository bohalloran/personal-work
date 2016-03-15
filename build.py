import logging
from jenkinsapi.jenkins import Jenkins
from time import sleep

# bohalloran@ubuntu:~/personal-work$ python
# Python 2.7.6 (default, Jun 22 2015, 17:58:13)
# [GCC 4.8.2] on linux2
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from build import Build
# >>> b = Build()
# Connecting to build server http://bs101.ops.ame1.bitsighttech.com:8080 ...
# >>> b.build_apt_packages()
# Creating build for branch feature/edq/rp-12140 ...
# Waiting for build 260 to finish ...


class Build(object):

    def __init__(self):
        # TODO: add logging into a base class
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(levelname)s %(message)s')
        self.jenkins_url = 'http://bs101.ops.ame1.bitsighttech.com:8080'
        self.project_name = 'Build-Apt-Feature-Merge'
        self.si = self.get_server_instance()

    def get_server_instance(self):

        # TODO: prompt for password
        # get username and password from Jenkins/Configure/API Token
        logging.info('Connecting to build server %s ...' % self.jenkins_url)
        server_instance = Jenkins(self.jenkins_url,
                                  username='',
                                  password='')
        return server_instance

    def build_apt_packages(self):
        # start/create buld job
        # TODO: prompt for 'branch' and 'targetbranch'
        branch = 'feature/edq/rp12130-new-pdns-cron'
        targetbranch = 'feature/edq/shady-page-integration'
        logging.info('Creating build for branch %s ...' % branch)
        self.si.build_job(self.project_name,
                          params={'branch': branch, 'targetbranch': targetbranch})
        job = self.si.get_job('Build-Apt-Feature-Merge')
        build_num = job.get_next_build_number()
        # TODO: Need timeout if is_queued_or_running() does not return
        while job.is_queued_or_running():
            logging.info('Waiting for build %s to finish ...' % build_num)
            sleep(10)

        # TODO: check to make sure build completed successfully, throws exception?
        # TODO: collect logs from jenkins and write to log file
        # might be better to look at last line of output for SUCCESS/FAILURE
        if int(build_num) == int(job.get_last_good_buildnumber()):
            logging.info('Finished: SUCCESS')
        else:
            logging.warning('Finished: FAILURE')
        logging.info('Job logs can be found at %sconsoleText' %
                     job.get_build_dict()[build_num])

    def get_last_build_description(self):
        j = self.si.get_job(self.project_name)
        b = j.get_last_build()
        logging.info('\nBuild Description: %s\nBuild Date: %s\nBuild Status: %s'
                     % (str(b), b.get_timestamp(), b.get_status()))
