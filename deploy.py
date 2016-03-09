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

    # TODO: check that build ran OK
    # TODO: check that build numbers compare
    # TODO: write output to log file
    def deploy_build(self):
        print 'Starting deploy ...'
        out = self.cmds.bs_feature()
        for line in out.split("/n"):
            print line

    def get_postgres(self):
        return

    def chef_client(self):
        return
