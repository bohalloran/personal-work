# fabric settings
REQUEST_TIMOUT = 120.0
BUILD_SERVER = 'http://bs101.ops.ame1.bitsighttech.com:8080'
LOG_FILE_DATE_TIME_FORMAT = "%Y%m%dT%H%M%S"
JENKINS_PROJECT_NAME = 'Build-Apt-Feature-Merge'

# command line settings
BS_FEATURE = 'sudo apt-get update;sudo apt-get install -y -t feature --only-upgrade bs-.*'
GET_POSTGRES = '. /etc/bs.vars ; sudo -u postgres python /usr/local/bitsight/postgres-wal-restore/get_postgres.py em101.prd1 LATEST --no-push'
CHOWN_BITSIGHT = 'sudo chown -R bitsight.bitsight /usr/local/bitsight'
CHEF_CLIENT = 'sudo chef-client'
