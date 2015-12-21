
from fabric.api         import env, hide, settings, sudo
import                  constants

class Commands(object):

    def __init__(self, pid):

        self.pid = pid

        # Setup our fabric environment
        env.host_string = constants.SYSTEM_UNDER_TEST
        env.user = constants.SCALITY_USER
        env.password = constants.SCALITY_PASSWORD
        env.timeout = constants.REQUEST_TIMOUT

        # define our command set
        self.numFileHandlesCmd = constants.LSOF_CMD + self.pid + '|' + \
                                 constants.WC_CMD
        self.meminfoCmd = constants.MEMINFO_CMD
        self.systemLoadCmd = constants.SYSTEM_LOAD_CMD
        self.lsofCmd = constants.LSOF_CMD
        self.coreCmd = constants.CORE_CMD

    def lsofHandles(self):
        # TODO: Add some error checking around invalid PID
        commandToken = self.numFileHandlesCmd
        # throw away the first line of lsof header output for accurate count
        return int(self._runCmd(commandToken)) - 1

    def meminfo(self):
        commandToken = self.meminfoCmd
        return self._runCmd(commandToken)

    def systemLoad(self):
        commandToken = self.systemLoadCmd
        return self._runCmd(commandToken)

    def lsof(self):
        commandToken = self.lsofCmd + self.pid
        return self._runCmd(commandToken)

    def core(self):
        commandToken = self.coreCmd + self.pid
        return self._runCmd(commandToken)

    def _runCmd(self, cmd):
        with hide('output','running','warnings'), settings(warn_only=True):
            return sudo(cmd)
