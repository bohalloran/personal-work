from jenkinsapi.jenkins import Jenkins
from time import sleep

# TODO: add a logger
# TODO: make this a class
def get_server_instance():

    # TODO: prompt for password
    # get username and password from Jenkins/Configure/API Token
    jenkins_url = 'http://bs101.ops.ame1.bitsighttech.com:8080'
    server = Jenkins(jenkins_url, username='',
                     password='')
    return server

if __name__ == '__main__':
    si = get_server_instance()
    # start/create buld job
    # TODO: prompt for 'branch' and 'targetbranch'
    si.build_job('Build-Apt-Feature-Merge',
                 params={'branch': 'feature/rp12042/shady',
                         'targetbranch': 'feature/edq/pdnsautomapper'})
    job = si.get_job('Build-Apt-Feature-Merge')
    # TODO: there's got to be a way to get build number for a running job
    build_num = job.get_next_build_number()
    while job.is_queued_or_running():
        print 'Waiting for build %s to finish ...' % build_num
        sleep(5)

    # TODO: check to make sure build completed successfully
    print 'Job Finished'
    print job.get_description()
