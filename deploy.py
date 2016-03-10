from lib.commands import Commands

# bohalloran@ubuntu:~/personal-work$ python
# Python 2.7.6 (default, Jun 22 2015, 17:58:13)
# [GCC 4.8.2] on linux2
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from deploy import Deploy
# >>> d = Deploy()
# >>> d.deploy_build()
# Starting deploy ...

# TODO: add logging
class Deploy(object):

    def __init__(self):
        self.cmds = Commands()

    # TODO: check that deploy ran OK
    # TODO: check that build and deploy id numbers compare
    # TODO: write output to log file
    # TODO: prompt for system under test
    def deploy_build(self):
        print 'Starting deploy ...'
        out = self.cmds.bs_feature()
        self._chown_deploy()
        for line in out.split("/n"):
            print line

    def _chown_deploy(self):
        self.cmds.chown_bitsight()

    # TODO: check that get_postgres ran OK
    def get_postgres(self):
        print 'Starting get_postgres ...'
        out = self.cmds.get_postgres()
        for line in out.split("/n"):
            print line

    # TODO: check that chef-client ran OK
    def chef_client(self):
        print 'Starting chef-client ...'
        out = self.cmds.chef_client()
        for line in out.split("/n"):
            print line
