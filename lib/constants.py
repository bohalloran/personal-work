# fabric settings
REQUEST_TIMOUT = 120.0
SYSTEM_UNDER_TEST = 'em102.public.ame1.bitsighttech.com'

# command line settings
LSOF_CMD = 'lsof -p '
WC_CMD = 'wc -l '
MEMINFO_CMD = 'cat /proc/meminfo'
SYSTEM_LOAD_CMD = 'vmstat'
CORE_CMD = 'ulimit -c unlimited && kill -3 '
BS_FEATURE = 'sudo apt-get update;sudo apt-get install -y -t feature --only-upgrade bs-.*'
