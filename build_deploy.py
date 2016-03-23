import logging
from build import Build
from deploy import Deploy


class BuildDeploy(object):

    def __init__(self):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(levelname)s %(message)s')
        self.b = Build()
        self.d = Deploy(self.b.get_build_num())

    def execute_build_deploy(self):
        # TODO: run build_apt_packages() get_postgres parallel
        logging.info('Start build ...')
        self.b.build_apt_packages()
        # TODO: if the build fails then don't proceed
        logging.info('Start get_postgres ...')
        self.d.get_postgres()
        logging.info('Start bs-feature ...')
        self.d.bs_feature()
        logging.info('Start chef-client ...')
        self.d.chef_client()
