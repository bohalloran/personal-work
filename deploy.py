from lib.commands import Commands

# TODO: add logging
class Deploy(object):

    def __init__(self):
        self.cmds = Commands()

    # TODO: check that build ran OK
    # TODO: check that build numbers compare
    def deploy_build(self):
        print 'Starting deploy ...'
        out = self.cmds.bs_feature()
        for line in out.split("/n"):
            print line

d = Deploy()
d.deploy_build()
