#!/usr/bin/python

import logging
from build import Build
from deploy import Deploy


class BuildDeploy(object):

    def __init__(self, system_under_test):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(levelname)s %(message)s')
        self.b = Build()
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

bd = BuildDeploy('em102.public.ame1.bitsighttech.com')
bd.execute_build_deploy()
