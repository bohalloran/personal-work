'''
Created on 12 Dec 2015

@author: bohalloran
'''

# fabric settings
REQUEST_TIMOUT = 120.0
SCALITY_USER = 'scality'
SCALITY_PASSWORD = 'scality'
SYSTEM_UNDER_TEST= '100.100.100.35'

# command line settings
LSOF_CMD = 'lsof -p '
WC_CMD = 'wc -l '
MEMINFO_CMD = 'cat /proc/meminfo'
SYSTEM_LOAD_CMD = 'vmstat'
CORE_CMD = 'ulimit -c unlimited && kill -3 '