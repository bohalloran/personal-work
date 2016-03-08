from fabric.api import env, hide, settings, sudo
import constants


class Commands(object):

    def __init__(self, pid):

        self.pid = pid

        # Setup our fabric environment
        env.host_string = constants.SYSTEM_UNDER_TEST
        env.timeout = constants.REQUEST_TIMOUT

        # define our command set
        self.numFileHandlesCmd = constants.LSOF_CMD + self.pid + '|' + constants.WC_CMD
        self.meminfoCmd = constants.MEMINFO_CMD
        self.systemLoadCmd = constants.SYSTEM_LOAD_CMD
        self.lsofCmd = constants.LSOF_CMD
        self.coreCmd = constants.CORE_CMD
        self.bsfCmd = constants.BS_FEATURE

    def lsof_handles(self):
        # TODO: Add some error checking around invalid PID
        command_token = self.numFileHandlesCmd
        # throw away the first two lines of lsof header output
        return int(self._run_cmd(command_token)) - 1

    def meminfo(self):
        command_token = self.meminfoCmd
        return self._run_cmd(command_token)

    def system_load(self):
        command_token = self.systemLoadCmd
        return self._run_cmd(command_token)

    def lsof(self):
        command_token = self.lsofCmd + self.pid
        return self._run_cmd(command_token)

    def core(self):
        command_token = self.coreCmd + self.pid
        return self._run_cmd(command_token)

    def bs_feature(self):
        command_token = self.bsfCmd
        return self._run_cmd(command_token)

    def _run_cmd(self, cmd):
        with hide('output', 'running', 'warnings'), settings(warn_only=True):
            return sudo(cmd)
