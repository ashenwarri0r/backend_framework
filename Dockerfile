FROM python:3.13-slim

LABEL version="1.3" author="ashen"

WORKDIR /api_framework

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH="${PYTHONPATH}:/api_framework"

CMD ["pytest", "tests/"]