from fabric.api import env, hide, settings, sudo
import constants


class Commands(object):

    def __init__(self, system_under_test):

        # Setup our fabric environment
        env.host_string = system_under_test
        env.timeout = constants.REQUEST_TIMOUT

        # define our command set
        self.bsfCmd = constants.BS_FEATURE
        self.getPostgresCmd = constants.GET_POSTGRES
        self.chownBitsightCmd = constants.CHOWN_BITSIGHT
        self.chefClientCmd = constants.CHEF_CLIENT

    def bs_feature(self):
        command_token = self.bsfCmd
        return self._run_cmd(command_token)

    def chown_bitsight(self):
        command_token = self.chownBitsightCmd
        return self._run_cmd(command_token)

    def get_postgres(self):
        command_token = self.getPostgresCmd
        return self._run_cmd(command_token)

    def chef_client(self):
        command_token = self.chefClientCmd
        return self._run_cmd(command_token)

    # TODO: we need to stream the output so that callers can see progress
    def _run_cmd(self, cmd):
        with hide('running', 'warnings'), settings(warn_only=True):
            return sudo(cmd)
