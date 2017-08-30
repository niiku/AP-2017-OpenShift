#!/bin/bash

# run this script from a machine connected to your cehnos machine
# ./bootstrap-centos.sh <machine url>
# e.g. when run script source dir:
#      ./bootstrap-centos.sh openshift.example.com

if [ "$#" -eq 1 ]
then
  hostname="$1"
else
  echo "Usage: $0 <hostname>"
  exit
fi

ssh-keygen -R $hostname
ssh-copy-id root@$hostname

echo 'yum install epel-release centos-release-paas-common centos-release-openshift-origin docker wget vim -y' | ssh "root@$hostname"
echo 'yum clean all' | ssh "root@$hostname"
echo 'yum upgrade -y' | ssh "root@$hostname"
