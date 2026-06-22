FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y openjdk-21-jdk wget && \
    rm -rf /var/lib/apt/lists/*

# Set Java environment
ENV JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

# Install PySpark
RUN pip install pyspark==3.5.1

# Create application directories
WORKDIR /app

COPY app /app/app
COPY data /app/data
RUN mkdir -p /app/output

# Execute application automatically
CMD ["python", "/app/app/employee_processing.py"]