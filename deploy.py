
import sys
import time
import datetime
from lib.commands import Commands


class Deploy(object):

    def __init__(self):
        # TODO: Add some intellegent command line parsing
        self.pid = sys.argv[1]

        # Define some parameters for monitoring daemon
        self.monitorWait = 5
        self.acceptableFileHandleLimit = 100
        self.statusOK = 'OK'
        self.statusSevere = 'SEVERE'
        # TODO: Add a WARNING status message
        # self.warningThreshold = 0.9
        # self.statusSevere = 'WARNING'
        self.header = 'DATE\tPID\tHANDLES\tSTATUS'

        self.cmds = Commands(self.pid)

    def monitor_process(self):
        num_file_handles = self.cmds.lsof_handles()
        status = self.statusOK
        # TODO: In general, replace all print with a log handler
        print self.header
        # So long as the number of open file handles is not too excessive
        while num_file_handles < self.acceptableFileHandleLimit:
            self._display_status(status, num_file_handles)
            time.sleep(self.monitorWait)
            num_file_handles = self.cmds.lsof_handles()

        # File handles exceeded
        self._dump_stats(self.statusSevere, num_file_handles)

    def deploy_build(self):
        self.cmds.bs_feature()

    def _dump_stats(self, status, num_file_handles):
        # TODO: dump in json format
        # TODO: ran out of time, need to finish implementing core/daemon mem
        self._display_status(status, num_file_handles)
        print '\n****Memory useage of server****\n' + self.cmds.meminfo()
        print '\n****Memory useage of daemon****\n'
        print '\n****Current load of system****\n' + self.cmds.system_load()
        print '\n****List of all opened files in daemon****\n' + self.cmds.lsof()
        print '\n****Generate a core dump****\n'

    def _display_status(self, status, num_file_handles):
        # TODO: We should be writing this out a .csv
        print datetime.datetime.now().isoformat() + '\t' + self.pid + '\t' \
              + str(num_file_handles) + '\t' + status

d = Deploy()
d.deploy_build()
# d.monitor_process()
