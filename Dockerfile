FROM python:3.13-slim

LABEL version="1.3" author="ashen"

RUN apt-get update && \
    apt-get install -y --no-install-recommends openjdk-17-jre && \
    rm -rf /var/lib/apt/lists/*

RUN curl -o allure-2.24.0.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.24.0/allure-commandline-2.24.0.tgz \
    && tar -zxvf allure-2.24.0.tgz -C /opt/ \
    && ln -s /opt/allure-2.24.0/bin/allure /usr/bin/allure \
    && rm allure-2.24.0.tgz

WORKDIR /api_framework

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH="${PYTHONPATH}:/api_framework"

VOLUME /api_framework/allure-report

CMD ["sh", "-c", "pytest --alluredir=allure-results tests/ && allure generate allure-results -o allure-report --clean"]