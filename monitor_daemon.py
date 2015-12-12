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

import sys
import time
import datetime
from fabric.api                     import env, hide, settings, sudo
import                              constants

class MonitorDaemon(object):

    def __init__(self):
        # TODO: Add some intellegent command line parsing
        self.pid = sys.argv[1]

        # Setup our fabric environment
        env.host_string = constants.SYSTEM_UNDER_TEST
        env.user = constants.SCALITY_USER
        env.password = constants.SCALITY_PASSWORD
        env.timeout = constants.REQUEST_TIMOUT

        # Define some parameters for monitoring daemon
        self.monitorWait = 5
        self.acceptableFileHandleLimit = 100
        self.statusOK = 'OK'
        self.statusSevere = 'SEVERE'
        # TODO: Add a WARNING status message
        # self.warningThreshold = 0.9
        # self.statusSevere = 'WARNING'
        self.header = 'DATE\tPID\tHANDLES\tSTATUS'

        # define our command set
        self.numFileHandlesCmd = constants.LSOF_CMD + self.pid + '|' + constants.WC_CMD
        self.meminfoCmd = constants.MEMINFO_CMD
        self.systemLoadCmd = constants.SYSTEM_LOAD_CMD
        self.lsofCmd = constants.LSOF_CMD
        self.coreCmd = constants.CORE_CMD

    def monitorProcess(self):
        numFileHandles = self.lsofHandles()
        status = self.statusOK
        # TODO: In general, replace all print with a log handler
        print self.header
        # So long as the number of open file handles is not too excessive
        while numFileHandles < self.acceptableFileHandleLimit:
            self._displayStatus(status, numFileHandles)
            time.sleep(self.monitorWait)
            numFileHandles = self.lsofHandles()

        # File handles exceeded
        self.dumpStats(self.statusSevere, numFileHandles)

    def dumpStats(self, status, numFileHandles):
        # TODO: dump in json format
        # TODO: ran out of time, need to finish implementing core/daemon mem
        self._displayStatus(status, numFileHandles)
        print '\n****Memory useage of server****\n' + self.meminfo()
        print '\n****Memory useage of daemon****\n'
        print '\n****Current load of system****\n' + self.systemLoad()
        print '\n****List of all opened files in daemon****\n' + self.lsof()
        print '\n****Generate a core dump****\n'

    def lsofHandles(self):
        # TODO: Add some error checking around invalid PID
        # TODO: Package this method in a separate library class for general use
        commandToken = self.numFileHandlesCmd
        # throw away the first line of lsof header output for accurate count
        return int(self._runCmd(commandToken)) - 1

    def meminfo(self):
        # TODO: Package this method in a separate library class for general use
        commandToken = self.meminfoCmd
        return self._runCmd(commandToken)

    def systemLoad(self):
        # TODO: Package this method in a separate library class for general use
        commandToken = self.systemLoadCmd
        return self._runCmd(commandToken)

    def lsof(self):
        # TODO: Package this method in a separate library class for general use
        commandToken = self.lsofCmd + self.pid
        return self._runCmd(commandToken)

    def core(self):
        # TODO: Package this method in a separate library class for general use
        commandToken = self.coreCmd + self.pid
        return self._runCmd(commandToken)

    def _runCmd(self, cmd):
        with hide('output','running','warnings'), settings(warn_only=True):
            return sudo(cmd)

    def _displayStatus(self, status, numFileHandles):
        # TODO: We should be writing this out a .csv
        print datetime.datetime.now().isoformat() + '\t' + self.pid + '\t' \
              + str(numFileHandles) + '\t' + status

md = MonitorDaemon()
md.monitorProcess()
