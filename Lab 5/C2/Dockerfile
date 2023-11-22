# Dockerfile_C2
FROM ubuntu:16.10

# Modificar el archivo /etc/apt/sources.list y actualizar la lista de paquetes e instalar sudo, net-tools, y openssh-client en un solo comando
RUN sed -i 's/http:\/\/archive.ubuntu.com\/ubuntu/http:\/\/old-releases.ubuntu.com\/ubuntu/' /etc/apt/sources.list && \
    sed -i '/^deb.*security.ubuntu.com/s/^/#/' /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y sudo net-tools openssh-client
