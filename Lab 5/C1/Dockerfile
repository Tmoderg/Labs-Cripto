# Dockerfile_C1
FROM ubuntu:14.10

# Modificar el archivo /etc/apt/sources.list
RUN sed -i 's/http:\/\/archive.ubuntu.com\/ubuntu/http:\/\/old-releases.ubuntu.com\/ubuntu/' /etc/apt/sources.list
RUN sed -i '/^dev.*security.ubuntu.com/s/^/#/' /etc/apt/sources.list

# Instalar sudo, net-tools, y openssh-client
RUN apt update && apt install -y sudo net-tools openssh-client
