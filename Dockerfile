FROM python:3.11-slim

RUN apt-get update \
    && apt-get install -y gcc python3-dev build-essential \
    && pip install --no-cache-dir flask \
    && apt-get remove -y gcc python3-dev build-essential \
    && apt-get autoremove -y \
    && apt-get clean

COPY main.py /main.py
COPY magister_lib /magister_lib

CMD ["python", "/main.py"]
