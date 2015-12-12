Write a working script program in python 2.7 that periodically monitors a
specific daemon by its PID. If the daemon has more than 100 opened files
descriptors at same time (STATUS = SEVERE), program does the following actions:
•	Print memory usage of server
•	Print memory usage of daemon
•	Print current load of system
•	Print the list of all opened files in daemon (with corresponding file
    descriptor)
•	Generate a coredump of daemon (and its child if needed)

To run:
$ git clone https://github.com/bohalloran/personal-work
$ git fetch
$ git pull
$ git checkout scality
$ chmod 755 monitor_daemon.py
$ python monitor_daemon.py 1305

Sample output STATUS = OK:
$ python monitor_daemon.py 1305
DATE	PID	HANDLES	STATUS
2015-12-12T14:52:39.428472	1305	14	OK
2015-12-12T14:52:44.484835	1305	14	OK
2015-12-12T14:52:49.544476	1305	14	OK
2015-12-12T14:52:54.600324	1305	14	OK
...
...
...

Sample output STATUS = SEVERE
$ python monitor_daemon.py 911
DATE	PID	HANDLES	STATUS
2015-12-12T14:55:45.734791	911	105	SEVERE

****Memory useage of server****
MemTotal:        2049592 kB
MemFree:           88464 kB
Buffers:           18192 kB
Cached:            86556 kB
SwapCached:         4536 kB
Active:          1285372 kB
Inactive:         471824 kB
Active(anon):    1231376 kB
Inactive(anon):   422040 kB
Active(file):      53996 kB
Inactive(file):    49784 kB
Unevictable:           0 kB
Mlocked:               0 kB
SwapTotal:       1337276 kB
SwapFree:        1326916 kB
Dirty:                84 kB
Writeback:             0 kB
AnonPages:       1648000 kB
Mapped:            31920 kB
Shmem:               968 kB
Slab:              51104 kB
SReclaimable:      24060 kB
SUnreclaim:        27044 kB
KernelStack:        4080 kB
PageTables:        16108 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:     2362072 kB
Committed_AS:    5132372 kB
VmallocTotal:   34359738367 kB
VmallocUsed:      158820 kB
VmallocChunk:   34359513780 kB
HardwareCorrupted:     0 kB
AnonHugePages:    987136 kB
HugePages_Total:       0
HugePages_Free:        0
HugePages_Rsvd:        0
HugePages_Surp:        0
Hugepagesize:       2048 kB
DirectMap4k:       71616 kB
DirectMap2M:     2025472 kB

****Memory useage of daemon****


****Current load of system****
procs -----------memory---------- ---swap-- -----io---- -system-- ----cpu----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa
 1  0  10360  88504  18192  86556    0    0     8    10  797  429  9  6 85  0

****List of all opened files in daemon****
COMMAND PID USER   FD   TYPE             DEVICE SIZE/OFF    NODE NAME
java    911 root  cwd    DIR                9,2     4096  581422 /opt/logstash
java    911 root  rtd    DIR                9,2     4096       2 /
java    911 root  txt    REG                9,2     6320  106440 /usr/lib/jvm/java-7-openjdk-amd64/jre/bin/java
java    911 root  mem    REG                9,2    90382  547802 /tmp/jffi1887433762720126334.tmp
java    911 root  mem    REG                9,2    72736  106391 /usr/lib/jvm/java-7-openjdk-amd64/jre/lib/amd64/libnio.so
java    911 root  mem    REG                9,2   247896  964855 /lib/x86_64-linux-gnu/libpcre.so.3.12.1
java    911 root  mem    REG                9,2    30896 1865568 /usr/lib/x86_64-linux-gnu/libffi.so.6.0.0
java    911 root  mem    REG                9,2   105288  965775 /lib/x86_64-linux-gnu/libresolv-2.15.so
java    911 root  mem    REG                9,2   121936  964831 /lib/x86_64-linux-gnu/libselinux.so.1
java    911 root  mem    REG                9,2    14528 1128371 /usr/lib/x86_64-linux-gnu/libgmodule-2.0.so.0.3200.4
java    911 root  mem    REG                9,2  1000472  964784 /lib/x86_64-linux-gnu/libglib-2.0.so.0.3200.4
java    911 root  mem    REG                9,2   322648 1128374 /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0.3200.4
java    911 root  mem    REG                9,2  1364896 1128373 /usr/lib/x86_64-linux-gnu/libgio-2.0.so.0.3200.4
java    911 root  mem    REG                9,2    97152  106372 /usr/lib/jvm/java-7-openjdk-amd64/jre/lib/amd64/libnet.so
java    911 root  mem    REG                9,2 82915969  582904 /opt/logstash/logstash.jar
java    911 root  mem    REG                9,2 32325641  106426 /usr/lib/jvm/java-7-openjdk-amd64/jre/lib/rt.jar
java    911 root  mem    REG                9,2    35248  106365 /usr/lib/jvm/java-7-openjdk-amd64/jre/lib/amd64/libzip.so
java    911 root  mem    REG                9,2    52120  965774 /lib/x86_64-linux-gnu/libnss_files-2.15.so
java    911 root  mem    REG                9,2    47680  965778 /lib/x86_64-linux-gnu/libnss_nis-2.15.so
java    911 root  mem    REG                9,2    97248  965790 /lib/x86_64-linux-gnu/libnsl-2.15.so
java    911 root  mem    REG                9,2    35680  965772 /lib/x86_64-linux-gnu/libnss_compat-2.15.so
java    911 root  mem    REG                9,2   174984  106360 /usr/lib/jvm/java-7-openjdk-amd64/jre/lib/amd64/libjava.so
java    911 root  mem    REG                9,2    63968  106378 /usr/lib/jvm/java-7-openjdk-amd64/jre/lib/amd64/libverify.so
java    911 root  mem    REG                9,2    31752  965777 /lib/x86_64-linux-gnu/librt-2.15.so
java    911 root  mem    REG                9,2    88384  964812 /lib/x86_64-linux-gnu/libgcc_s.so.1
java    911 root  mem    REG                9,2  1030512  965781 /lib/x86_64-linux-gnu/libm-2.15.so
java    911 root  mem    REG                9,2   962656 1867302 /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.16
java    911 root  mem    REG                9,2 14615550  114534 /usr/lib/jvm/java-7-openjdk-amd64/jre/lib/amd64/server/libjvm.so
java    911 root  mem    REG                9,2    92720  964996 /lib/x86_64-linux-gnu/libz.so.1.2.3.4
java    911 root  mem    REG                9,2   135366  965779 /lib/x86_64-linux-gnu/libpthread-2.15.so
java    911 root  mem    REG                9,2    14768  965785 /lib/x86_64-linux-gnu/libdl-2.15.so
java    911 root  mem    REG                9,2  1815224  965770 /lib/x86_64-linux-gnu/libc-2.15.so
java    911 root  mem    REG                9,2    56032  114537 /usr/lib/jvm/java-7-openjdk-amd64/jre/lib/amd64/jli/libjli.so
java    911 root  mem    REG                9,2   149280  965782 /lib/x86_64-linux-gnu/ld-2.15.so
java    911 root  mem    REG                9,2   330652  106399 /usr/lib/jvm/java-7-openjdk-amd64/jre/lib/jsse.jar
java    911 root  mem    REG                9,2    78194  106405 /usr/lib/jvm/java-7-openjdk-amd64/jre/lib/ext/zipfs.jar
java    911 root  mem    REG                9,2   558460  106404 /usr/lib/jvm/java-7-openjdk-amd64/jre/lib/ext/localedata.jar
java    911 root  mem    REG                9,2   225679  106406 /usr/lib/jvm/java-7-openjdk-amd64/jre/lib/ext/sunjce_provider.jar
java    911 root  mem    REG                9,2    70333  106408 /usr/lib/jvm/java-7-openjdk-amd64/jre/lib/ext/icedtea-sound.jar
java    911 root  mem    REG                9,2   259918  106409 /usr/lib/jvm/java-7-openjdk-amd64/jre/lib/ext/sunpkcs11.jar
java    911 root  mem    REG                9,2    31752 1907620 /usr/share/java/java-atk-wrapper.jar
java    911 root  mem    REG                9,2    10074  106407 /usr/lib/jvm/java-7-openjdk-amd64/jre/lib/ext/dnsns.jar
java    911 root    0u   CHR                1,3      0t0    1029 /dev/null
java    911 root    1u   CHR              136,1      0t0       4 /dev/pts/1
java    911 root    2u   CHR              136,1      0t0       4 /dev/pts/1
java    911 root    3r   REG                9,2 32325641  106426 /usr/lib/jvm/java-7-openjdk-amd64/jre/lib/rt.jar
java    911 root    4r   REG                9,2   259918  106409 /usr/lib/jvm/java-7-openjdk-amd64/jre/lib/ext/sunpkcs11.jar
java    911 root    5r   REG                9,2    10074  106407 /usr/lib/jvm/java-7-openjdk-amd64/jre/lib/ext/dnsns.jar
java    911 root    6r   REG                9,2    70333  106408 /usr/lib/jvm/java-7-openjdk-amd64/jre/lib/ext/icedtea-sound.jar
java    911 root    7r   REG                9,2   225679  106406 /usr/lib/jvm/java-7-openjdk-amd64/jre/lib/ext/sunjce_provider.jar
java    911 root    8r   REG                9,2   558460  106404 /usr/lib/jvm/java-7-openjdk-amd64/jre/lib/ext/localedata.jar
java    911 root    9r   REG                9,2    31752 1907620 /usr/share/java/java-atk-wrapper.jar
java    911 root   10r   REG                9,2    78194  106405 /usr/lib/jvm/java-7-openjdk-amd64/jre/lib/ext/zipfs.jar
java    911 root   11r   REG                9,2 82915969  582904 /opt/logstash/logstash.jar
java    911 root   12r   REG                9,2   330652  106399 /usr/lib/jvm/java-7-openjdk-amd64/jre/lib/jsse.jar
java    911 root   13r   CHR                1,8      0t0    1033 /dev/random
java    911 root   14r   CHR                1,9      0t0    1034 /dev/urandom
java    911 root   15w   REG                9,2   124461 1447568 /var/log/logstash/agent.log
java    911 root   16u  unix 0xffff88007b929180      0t0   16202 socket
java    911 root   17r   REG                9,2    71100 1431121 /var/log/storiant/sc-api-7.log
java    911 root   18r   REG                9,2     1955 1431505 /var/log/storiant/sc-job-man-Scrub.log
java    911 root   19u  IPv6              18759      0t0     UDP *:9999
java    911 root   20r   REG                9,2  4643608 1424179 /var/log/syslog
java    911 root   21r   REG                9,2     9302 1431109 /var/log/storiant/sc-file-access-18.log
java    911 root   22r   REG                9,2    42128 1431050 /var/log/storiant/sc-file-access-6.log
java    911 root   23r   REG                9,2     9753 1431052 /var/log/storiant/sc-file-access-8.log
java    911 root   24r   REG                9,2    12140 1431102 /var/log/storiant/sc-file-access-11.log
java    911 root   25r   REG                9,2    10400 1431107 /var/log/storiant/sc-file-access-14.log
java    911 root   26r   REG                9,2    75673 1431276 /var/log/storiant/sc-api-4.log
java    911 root   27r   REG                9,2   103934 1431119 /var/log/storiant/sc-api-8.log
java    911 root   28r   REG                9,2    14242 1431105 /var/log/storiant/sc-file-access-16.log
java    911 root   29r   REG                9,2    27406 1431289 /var/log/storiant/sc-job-man-Copy.log
java    911 root   30r   REG                9,2     7381 1430933 /var/log/storiant/sc-vault-stat.log
java    911 root   31r   REG                9,2    11016 1430939 /var/log/storiant/sc-file-access-7.log
java    911 root   32r   REG                9,2     9201 1431101 /var/log/storiant/sc-file-access-12.log
java    911 root   33r   REG                9,2    23593 1431110 /var/log/storiant/sc-file-access-17.log
java    911 root   34r   REG                9,2     5143 1431280 /var/log/storiant/sc-proc-mon.log
java    911 root   35r   REG                9,2    11843 1430938 /var/log/storiant/sc-file-access-5.log
java    911 root   36r   REG                9,2    15244 1431051 /var/log/storiant/sc-file-access-9.log
java    911 root   37r   REG                9,2    10141 1430937 /var/log/storiant/sc-file-access-4.log
java    911 root   38r   REG                9,2    70072 1431118 /var/log/storiant/sc-api-5.log
java    911 root   39r   REG                9,2    14097 1431104 /var/log/storiant/sc-file-access-15.log
java    911 root   40r   REG                9,2    11454 1431053 /var/log/storiant/sc-file-access-10.log
java    911 root   41r   REG                9,2    14944 1430865 /var/log/storiant/sc-procs-cmd.log
java    911 root   42r   REG                9,2  4036609 1430871 /var/log/storiant/sc-zfs-man.log
java    911 root   43u  IPv6             304667      0t0     TCP lap1-stor1:47899->lap1-mgmt1:6379 (ESTABLISHED)
java    911 root   44r  FIFO                0,8      0t0   17841 pipe
java    911 root   45w  FIFO                0,8      0t0   17841 pipe
java    911 root   46u  0000                0,9        0    6289 anon_inode
java    911 root   47u  IPv6              22076      0t0     TCP lap1-stor1:44767->lap1-mgmt1:6379 (ESTABLISHED)
java    911 root   48r   REG                9,2    12037 1430935 /var/log/storiant/sc-file-access-3.log
java    911 root   49r   REG                9,2    92921 1431111 /var/log/storiant/sc-api-6.log
java    911 root   50r   REG                9,2        0 1430931 /var/log/storiant/sc-zfs-man-scrub.log
java    911 root   51r   REG                9,2    62055 1431117 /var/log/storiant/sc-api-3.log
java    911 root   52r   REG                9,2    22200 1431108 /var/log/storiant/sc-file-access-1.log
java    911 root   53r   REG                9,2  2601577 1430934 /var/log/storiant/sc-power-man.log
java    911 root   54r   REG                9,2    81978 1431279 /var/log/storiant/sc-api-1.log
java    911 root   55r   REG                9,2     1700 1431511 /var/log/storiant/sc-job-man-SyncMetaFS.log
java    911 root   56r   REG                9,2    72205 1431503 /var/log/storiant/sc-job-man-RAW.log
java    911 root   57r   REG                9,2    11259 1431103 /var/log/storiant/sc-file-access-13.log
java    911 root   58r   REG                9,2    17687 1431282 /var/log/storiant/sc-job-man.log
java    911 root   59r   REG                9,2    91796 1431120 /var/log/storiant/sc-api-2.log
java    911 root   60r   REG                9,2    28838 1431456 /var/log/storiant/sc-job-man-Delete.log
java    911 root   61r   REG                9,2    16072 1430936 /var/log/storiant/sc-file-access-2.log
java    911 root   65r   REG                9,2   397625 1424203 /var/log/auth.log

****Generate a core dump****

$