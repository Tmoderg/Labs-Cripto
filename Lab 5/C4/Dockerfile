# Dockerfile_C4S1
FROM ubuntu:20.10

# Modificar el archivo /etc/apt/sources.list
RUN sed -i 's/http:\/\/archive.ubuntu.com\/ubuntu/http:\/\/old-releases.ubuntu.com\/ubuntu/' /etc/apt/sources.list
RUN sed -i '/^deb.*security.ubuntu.com/s/^/#/' /etc/apt/sources.list

# Instalar sudo, net-tools, openssh-client y openssh-server
RUN apt-get update && apt-get install -y sudo net-tools openssh-client openssh-server

# Agregar un usuario "test" con la contraseña "test"
RUN useradd -m -p "$(openssl passwd -1 test)" test

# Exponer el puerto 22 para el acceso SSH
EXPOSE 22
