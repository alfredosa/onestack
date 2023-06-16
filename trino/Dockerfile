# syntax=docker/dockerfile:1
FROM python:3.10-bullseye

ENV TRINO_HOME=/opt/trino
ENV BIN_DIR=/usr/bin

ENV DATA_STAGE_DIR=/var/lib/onestack/stage
ENV TRINO_DATA_DIR=/var/lib/trino/data
ENV INSTALL_DIR=/tmp/install

RUN mkdir -p ${TRINO_HOME} ${TRINO_DATA_DIR} ${DATA_STAGE_DIR} ${INSTALL_DIR}


# Install Java
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl -L -o /tmp/openjdk.tar.gz https://download.java.net/java/GA/jdk17/0d483333a00540d886896bac774ff48b/35/GPL/openjdk-17_linux-x64_bin.tar.gz \
    && tar xvf /tmp/openjdk.tar.gz -C /opt/ \
    && rm /tmp/openjdk.tar.gz


ENV JAVA_HOME=/opt/jdk-17
ENV PATH=$PATH:$JAVA_HOME/bin

# Configure ca-certificates for Java
RUN update-ca-certificates --force

WORKDIR ${INSTALL_DIR}

# Install python deps
COPY conf/requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt \
    && rm requirements.txt

RUN curl https://repo1.maven.org/maven2/io/trino/trino-server/406/trino-server-406.tar.gz -Lo trino-server-406.tar.gz \
    && tar xvzf trino-server-406.tar.gz --directory ${TRINO_HOME} --strip-components 1 \
    && rm trino-server-406.tar.gz

WORKDIR ${TRINO_HOME}

COPY conf/trino/ ${TRINO_HOME}/etc

RUN chmod u+x ${TRINO_HOME}/bin/*

EXPOSE 8060
EXPOSE 8063

CMD ["/opt/trino/bin/launcher", "run"]
