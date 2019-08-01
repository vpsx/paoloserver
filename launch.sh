# I have no idea what I am doing
# With help from github.com/mikegcoleman/todo#docker-containers-with-docker-compose

# install latest version of docker the lazy way
curl -sSL https://get.docker.com | sh

# make it so you don't need to sudo to run docker commands
usermod -aG docker ubuntu

# run the thing
docker run -t -p 80:5000 vpsx/paoloserver:latest
