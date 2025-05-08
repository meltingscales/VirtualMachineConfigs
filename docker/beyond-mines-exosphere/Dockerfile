FROM ubuntu:24.04

RUN apt update

RUN apt install -y curl wget unzip
RUN apt install -y openjdk-17-jre

RUN wget https://mediafilez.forgecdn.net/files/6487/661/BM_Exosphere_2.0.2_server.zip

RUN unzip BM_Exosphere_2.0.2_server.zip -d /minecraft-unzipped/

WORKDIR /minecraft/

ADD ./docker-scripts/bootstrap-server.sh /

ENTRYPOINT [ "/bin/bash", "/bootstrap-server.sh" ]
