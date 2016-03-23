import logging
import datetime
import lib.constants
from lib.commands import Commands


class Deploy(object):

    def __init__(self, build_num):
        # TODO: move logging definition into a base class
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(levelname)s %(message)s')
        self.cmds = Commands()
        date_time = datetime.datetime.now().\
            strftime(lib.constants.LOG_FILE_DATE_TIME_FORMAT)
        self.get_postgres_log_file_name = 'get_postgres_log_build_%s_%s' % \
                                          (build_num, date_time)
        self.bs_feature_log_file_name = 'bs_feature_log_build_%s_%s' % \
                                        (build_num, date_time)
        self.chef_client_log_file_name = 'chef_client_log_build_%s_%s' % \
                                         (build_num, date_time)

    # TODO: check that deploy ran OK
    # TODO: check that build and deploy pkg numbers compare
    # TODO: prompt for system under test
    # TODO: Check and make sure we aren't clobbering someones build
    def bs_feature(self):
        logging.info('Starting deploy ...')
        stdout = self.cmds.bs_feature()
        self._write_logs(self.bs_feature_log_file_name, stdout)
        self.cmds.chown_bitsight()

    # TODO: check that get_postgres ran OK
    def get_postgres(self):
        logging.info('Starting get_postgres ...')
        stdout = self.cmds.get_postgres()
        self._write_logs(self.get_postgres_log_file_name, stdout)

    # TODO: check that chef-client ran OK
    def chef_client(self):
        logging.info('Starting chef-client ...')
        stdout = self.cmds.chef_client()
        self._write_logs(self.chef_client_log_file_name, stdout)

    def _write_logs(self, fn, data):
        logging.info('Writing logs to %s' % fn)
        f = open(fn, 'a')
        f.write(data)
        f.close()
