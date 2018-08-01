
#!/bin/bash

ip=192.168.4.2
prefix=$1
repo=$2

nfd-stop

sleep 1

nfd-start

sleep 2

nfdc face create udp4://$ip permanent

nfdc route add /chronosync udp4://$ip
nfdc route add $prefix/repo2 udp4://$ip

nfdc strategy set /chronosync /localhost/nfd/strategy/multicast/%FD%03
nfdc strategy set $prefix/systemInfo /localhost/nfd/strategy/multicast/%FD%03

sudo rm /var/db/ndn-repo-ng/ndn_repo.db
sudo rm /home/pi/repo-ng/systemInfo/*

sudo ndn-repo-ng &
sleep 1
chrono-app $prefix $repo &
sleep 1
sudo ././onboarder/iot-bootstrapping/controller/linux/controller-sample $prefix $repo &
#python proxy-py/proxy.py $prefix $repo

