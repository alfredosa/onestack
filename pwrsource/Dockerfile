# syntax=docker/dockerfile:1
FROM python:3.10-bullseye

ENV METASTORE_HADOOP_VERSION=3.2.0
ENV METASTORE_VERSION=3.0.0
ENV SPARK_HOME=/opt/spark
ENV DAGSTER_HOME=/opt/dagster
ENV KYUUBI_HOME=/opt/kyuubi
ENV BIN_DIR=/usr/bin

ENV DAGSTER_DIR=/var/lib/onestack/dagster
ENV DBT_DIR=/var/lib/onestack/dbt
ENV NOTEBOOKS_DIR=/var/lib/onestack/notebooks
ENV DATA_STAGE_DIR=/var/lib/onestack/stage
ENV HTML_DIR=/var/lib/onestack/html

# Add iceberg spark runtime jar to IJava classpath
ENV IJAVA_CLASSPATH=/opt/spark/jars/*
ENV PATH="/opt/spark/sbin:/opt/spark/bin:${PATH}"
ENV INSTALL_DIR=/tmp/install

RUN mkdir -p ${SPARK_HOME} ${MINIO_HOME}/bin ${DAGSTER_HOME}  ${KYUUBI_HOME} \
             ${DAGSTER_DIR} ${DBT_DIR} ${DATA_STAGE_DIR} ${NOTEBOOKS_DIR} ${INSTALL_DIR} ${HTML_DIR} \
            /root/.ipython/profile_default/startup

# install core packages
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
      sudo \
      curl \
      unzip \
      make \
      openjdk-11-jdk \
      build-essential \
      software-properties-common \
      libpq-dev \
      gcc \
      g++ \
      libsasl2-dev \
		  libsasl2-2\
		  libsasl2-modules-gssapi-mit\
      unixodbc-dev \
      ssh \
      postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR ${INSTALL_DIR}

# Install python deps
COPY conf/requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt \
    && rm requirements.txt

# Download and install IJava jupyter kernel
RUN curl https://github.com/SpencerPark/IJava/releases/download/v1.3.0/ijava-1.3.0.zip -Lo ijava-1.3.0.zip \
  && unzip ijava-1.3.0.zip \
  && python3 install.py --sys-prefix \
  && rm -rf ijava-1.3.0.zip	install.py java \
# Download spark distribution and install it
  && curl https://archive.apache.org/dist/spark/spark-3.3.1/spark-3.3.1-bin-hadoop3.tgz -o spark-3.3.1-bin-hadoop3.tgz \
    && tar xvzf spark-3.3.1-bin-hadoop3.tgz --directory /opt/spark --strip-components 1 \
    && rm spark-3.3.1-bin-hadoop3.tgz \
# Download iceberg spark runtime
  && curl https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-spark-runtime-3.3_2.12/1.1.0/iceberg-spark-runtime-3.3_2.12-1.1.0.jar -Lo iceberg-spark-runtime-3.3_2.12-1.1.0.jar  \
    && mv iceberg-spark-runtime-3.3_2.12-1.1.0.jar /opt/spark/jars \
# Download Java AWS SDK
  && curl https://repo1.maven.org/maven2/software/amazon/awssdk/bundle/2.17.247/bundle-2.17.247.jar -Lo bundle-2.17.247.jar \
    && mv bundle-2.17.247.jar /opt/spark/jars \
# Download URL connection client required for S3FileIO
  && curl https://repo1.maven.org/maven2/software/amazon/awssdk/url-connection-client/2.17.247/url-connection-client-2.17.247.jar -Lo url-connection-client-2.17.247.jar \
     && mv url-connection-client-2.17.247.jar /opt/spark/jars \
# Install AWS CLI
  && curl https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip -o awscliv2.zip \
    && unzip awscliv2.zip \
    && sudo ./aws/install \
    && rm awscliv2.zip \
    && rm -rf aws/ \
# Download and install Kyuubi JDBC
  && curl https://archive.apache.org/dist/incubator/kyuubi/kyuubi-1.6.1-incubating/apache-kyuubi-1.6.1-incubating-bin.tgz -Lo kyuubi.tgz \
    && tar xvzf kyuubi.tgz --directory ${KYUUBI_HOME} --strip-components 1 \
    && rm kyuubi.tgz \
# Download and install Postgres deiver for Hive metastore
  && curl https://repo1.maven.org/maven2/org/postgresql/postgresql/42.5.3/postgresql-42.5.3.jar -Lo pgsql.jar \
    && mv pgsql.jar /opt/spark/jars

WORKDIR ${SPARK_HOME}

COPY conf/spark-defaults.conf ${SPARK_HOME}/conf
COPY conf/dagster.yaml ${DAGSTER_HOME}
COPY scripts/entrypoint.sh ${BIN_DIR}
COPY conf/ipython/startup/00-prettytables.py /root/.ipython/profile_default/startup
COPY conf/ipython/startup/README /root/.ipython/profile_default/startup
COPY conf/notebook ${BIN_DIR}/notebook
COPY conf/notebook ${BIN_DIR}/pyspark-notebook

RUN chmod u+x ${SPARK_HOME}/* \
  && chmod u+x ${SPARK_HOME}/bin/* \
  && chmod u+x ${BIN_DIR}/notebook \
  && chmod u+x ${BIN_DIR}/pyspark-notebook \
  && chmod +rx ${DBT_DIR}

RUN chown -R root:root ${DBT_DIR}

EXPOSE 3070
EXPOSE 8888
EXPOSE 7077
EXPOSE 8061
EXPOSE 8062
EXPOSE 10000
EXPOSE 10009
EXPOSE 18080

ENTRYPOINT ["/usr/bin/entrypoint.sh"]
CMD ["notebook"]
