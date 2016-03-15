# fabric settings
REQUEST_TIMOUT = 120.0
SYSTEM_UNDER_TEST = 'em101.edq2.ame1.bitsighttech.com'

# command line settings
BS_FEATURE = 'sudo apt-get update;sudo apt-get install -y -t feature --only-upgrade bs-.*'
GET_POSTGRES = '. /etc/bs.vars ; sudo -u postgres python /usr/local/bitsight/postgres-wal-restore/get_postgres.py em101.prd1 LATEST --no-push'
CHOWN_BITSIGHT = 'sudo chown -R bitsight.bitsight /usr/local/bitsight'
CHEF_CLIENT = 'sudo chef-client'
