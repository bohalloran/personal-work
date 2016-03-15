import logging
from lib.commands import Commands

# bohalloran@ubuntu:~/personal-work$ python
# Python 2.7.6 (default, Jun 22 2015, 17:58:13)
# [GCC 4.8.2] on linux2
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from deploy import Deploy
# >>> d = Deploy()
# >>> d.deploy_build()
# Starting deploy ...


class Deploy(object):

    def __init__(self):
        # TODO: add logging into a base class
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(levelname)s %(message)s')
        self.cmds = Commands()

    # TODO: check that deploy ran OK
    # TODO: check that build and deploy id numbers compare
    # TODO: write output to log file
    # TODO: prompt for system under test
    # TODO: Check and make sure we aren't clobbering someones build
    def deploy_build(self):
        logging.info('Starting deploy ...')
        self.cmds.bs_feature()
        self._chown_deploy()

    def _chown_deploy(self):
        self.cmds.chown_bitsight()

    # TODO: check that get_postgres ran OK
    def get_postgres(self):
        logging.info('Starting get_postgres ...')
        self.cmds.get_postgres()

    # TODO: check that chef-client ran OK
    def chef_client(self):
        logging.info('Starting chef-client ...')
        self.cmds.chef_client()
