FROM python:3.13-slim

LABEL version="1.3" author="ashen"

RUN apt-get update && \
    apt-get install -y --no-install-recommends openjdk-17-jre && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /api_framework

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH="${PYTHONPATH}:/api_framework"

VOLUME /api_framework/allure-report

CMD ["sh", "-c", "pytest --alluredir=allure-results tests/ && allure generate allure-results -o allure-report --clean"]