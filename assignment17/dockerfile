FROM python:3.12-slim

# Install Java
RUN apt-get update && \
    apt-get install -y openjdk-21-jdk wget && \
    rm -rf /var/lib/apt/lists/*

# Set Java Home
ENV JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH
# Install Spark
RUN pip install pyspark==3.5.1

WORKDIR /app

COPY . /app

CMD ["python", "app.py"]