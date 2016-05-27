#!/usr/bin/env python
'''
Build and depoly tool: Performs a feature build, restores postgres DB,
then deploys code to remote host and runs chef-client.

Usage:
    build_deploy.py <BRANCH> <TARGET-BRANCH> <UID> <PASSWD> <SYSTEM-UNDER-TEST>
    build_deploy.py -h | --help | --version

Arguments:
    BRANCH              test branch, e.g.fix/emdq/RP-12604
    TARGET-BRANCH       merge branch, e.g. master
    UID                 jenkins "User ID", e.g. bohalloran@bitsighttech.com
    PASSWD              jenkins "API Token", e.g. 4dc8.....................ac98
    SYSTEM-UNDER-TEST   system under test, e.g. em102.public.ame1.bitsighttech.com
'''

import logging
from docopt import docopt
from build import Build
from deploy import Deploy


class BuildDeploy(object):

    def __init__(self, branch, targetbranch, uname, passwd, system_under_test):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(levelname)s %(message)s')
        self.b = Build(branch, targetbranch, uname, passwd)
        self.d = Deploy(self.b.get_build_num(), system_under_test)

    def execute_build_deploy(self):
        # do everything: build, get_postgres, bs_feature and chef-client
        self.execute_build()
        # TODO: if the build fails then don't proceed
        self.execute_get_postgres()
        self.execute_bs_feature()
        self.execute_chef_client()

    def execute_build(self):
        # TODO: run build_apt_packages() get_postgres parallel
        logging.info('Start build ...')
        self.b.build_apt_packages()

    def execute_get_postgres(self):
        logging.info('Start get_postgres ...')
        self.d.get_postgres()

    def execute_bs_feature(self):
        logging.info('Start bs-feature ...')
        self.d.bs_feature()

    def execute_chef_client(self):
        logging.info('Start chef-client ...')
        self.d.chef_client()

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Build Deploy v1.0')
    bd = BuildDeploy(arguments['<BRANCH>'],
                     arguments['<TARGET-BRANCH>'],
                     arguments['<UID>'],
                     arguments['<PASSWD>'],
                     arguments['<SYSTEM-UNDER-TEST>'])
    bd.execute_build_deploy()
