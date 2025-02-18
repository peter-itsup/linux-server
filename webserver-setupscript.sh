#!/bin/bash 

# Prompt the user for input
echo "MAKE SURE YOU ARE ON THE CORRECT SERVER BEFORE RUNNING THE SCRIPT!"
read -p "Do you want to run the commands? (y/n): " user_input

# Check if user input is "y"
if [ "$user_input" == "y" ]; then
    echo "Running commands..."
    apt update
    apt install docker.io -y 
    docker volume create portainer_data
    docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:2.21.5
    docker run -d \
      --name mysql-container \
      -e MYSQL_ROOT_PASSWORD=my-secret-pw \
      -e MYSQL_DATABASE=wordpress \
      -p 3306:3306 \
      mysql:5.7
    docker run -d --name wordpress \
      --link mysql-container:mysql-container \
      -e WORDPRESS_DB_HOST=mysql-container:3306 \
      -e WORDPRESS_DB_NAME=wordpress \
      -e WORDPRESS_DB_USER=root \
      -e WORDPRESS_DB_PASSWORD=my-secret-pw \
      -p 8080:80 wordpress

    echo "All commands completed. Credentials stored in creds.txt. Remove after use"
    echo "WORDPRESS_DB_PASSWORD = my-secret-pw
          WORDPRESS_DB_USER = root
          " >> creds.txt
else
    echo "Commands not executed."
fi


