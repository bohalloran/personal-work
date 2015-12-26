'''
Created on 12 Dec 2015

@author: bohalloran
'''

'''
Monitor class that periodically examines the number of file descriptors and
when these descriptors reach a predefined threshold dump system level stats.

Decided to use the fabric API as it provides abstraction of remote server as
if was running locally.
Requires fabric python libray
$ sudo pip install fabric

The initial implementation was built and tested on a Mac host running OS X
10.11.2 and a vagrant virtual host guest running ubuntu 12.04 on the Mac host
as a client server model, where the client is the Mac host and the server is
the vagrant guest.
'''

import                      sys
import                      time
import                      datetime
from lib.commands           import Commands

class MonitorDaemon(object):

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

    def monitorProcess(self):
        numFileHandles = self.cmds.lsofHandles()
        status = self.statusOK
        # TODO: In general, replace all print with a log handler
        print self.header
        # So long as the number of open file handles is not too excessive
        while numFileHandles < self.acceptableFileHandleLimit:
            self._displayStatus(status, numFileHandles)
            time.sleep(self.monitorWait)
            numFileHandles = self.cmds.lsofHandles()

        # File handles exceeded
        self._dumpStats(self.statusSevere, numFileHandles)

    def _dumpStats(self, status, numFileHandles):
        # TODO: dump in json format
        # TODO: ran out of time, need to finish implementing core/daemon mem
        self._displayStatus(status, numFileHandles)
        print '\n****Memory useage of server****\n' + self.cmds.meminfo()
        print '\n****Memory useage of daemon****\n'
        print '\n****Current load of system****\n' + self.cmds.systemLoad()
        print '\n****List of all opened files in daemon****\n' + self.cmds.lsof()
        print '\n****Generate a core dump****\n'

    def _displayStatus(self, status, numFileHandles):
        # TODO: We should be writing this out a .csv
        print datetime.datetime.now().isoformat() + '\t' + self.pid + '\t' \
              + str(numFileHandles) + '\t' + status

md = MonitorDaemon()
md.monitorProcess()
