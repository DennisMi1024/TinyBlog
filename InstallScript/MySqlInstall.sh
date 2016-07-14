#/bin/bash
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password arthurtoday'
 
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password arthurtoday'
 
sudo apt-get install mysql-server -y

