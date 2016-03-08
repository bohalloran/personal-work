from jenkinsapi.jenkins import Jenkins
from time import sleep

# TODO: add a logger
# TODO: make this a class


def get_server_instance():

    # TODO: prompt for password
    # get username and password from Jenkins/Configure/API Token
    jenkins_url = 'http://bs101.ops.ame1.bitsighttech.com:8080'
    print 'Connecting to build server %s ...' % jenkins_url
    server = Jenkins(jenkins_url, username='',
                     password='')
    return server

if __name__ == '__main__':
    si = get_server_instance()
    # start/create buld job
    # TODO: prompt for 'branch' and 'targetbranch'
    branch = 'feature/edq/rp-12140'
    targetbranch = 'master'
    print 'Creating build for branch %s ...' % branch
    si.build_job('Build-Apt-Feature-Merge',
                 params={'branch': branch,
                         'targetbranch': targetbranch})
    job = si.get_job('Build-Apt-Feature-Merge')
    build_num = job.get_next_build_number()
    while job.is_queued_or_running():
        print 'Waiting for build %s to finish ...' % build_num
        sleep(5)

    # TODO: check to make sure build completed successfully, throws exception?
    if int(build_num) == int(job.get_last_good_buildnumber()):
        print 'Finished: SUCCESS'
    else:
        print 'Finished: FAILURE'
    print 'Job logs can be found at %sconsoleText' % job.get_build_dict()[build_num]
