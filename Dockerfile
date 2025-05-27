LABEL version="1.1" author="ashen"

FROM python:3.13-slim

WORKDIR /api_framework

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH="${PYTHONPATH}:/api_framework"

CMD ["pytest", "tests/"]