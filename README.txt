# to build a minimal CentOS image
# https://www.youtube.com/watch?v=s948NKa1I1I&t=5s
Brians-MacBook-Pro:vmware bohalloran$ docker load < centos7.4.1708base.tar 
cad8bc234d8a: Loading layer [==================================================>]  286.8MB/286.8MB
Loaded image ID: sha256:c980cfb106f0e3d3741a8a85f44bba1a62556561becf8dc85283cd5630f14386
Brians-MacBook-Pro:vmware bohalloran$ docker tag c980cfb106f0 bohalloran/centos7base:7.4.1708
Brians-MacBook-Pro:vmware bohalloran$ docker images
REPOSITORY               TAG                 IMAGE ID            CREATED             SIZE
bohalloran/centos7base   7.4.1708            c980cfb106f0        3 hours ago         271MB
Brians-MacBook-Pro:vmware bohalloran$ 
Brians-MacBook-Pro:vmware bohalloran$ cd
Brians-MacBook-Pro:~ bohalloran$ docker push bohalloran/centos7base:7.4.1708
The push refers to repository [docker.io/bohalloran/centos7base]
cad8bc234d8a: Pushed 
7.4.1708: digest: sha256:f69c0c9c88ef1e16861bed904aa8d785058b3d00afb6b0f9911d23b4f5038106 size: 529
Brians-MacBook-Pro:~ bohalloran$ 
# Build wordpress
docker build -t bohalloran/wordpress .
# To workaround running CentOS on ubunu 'error: unpacking of archive failed on file /usr/sbin/suexec: cpio: cap_set_file'
https://github.com/moby/moby/issues/6980
