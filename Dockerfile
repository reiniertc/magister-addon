FROM python:3.11-slim

# Zorg dat pip werkt met git (en algemene dependencies)
RUN apt-get update \
    && apt-get install -y git gcc python3-dev build-essential \
    && pip install --no-cache-dir flask \
    && pip install --no-cache-dir git+https://github.com/Devv00/magister.py.git \
    && apt-get remove -y git gcc python3-dev build-essential \
    && apt-get autoremove -y \
    && apt-get clean

COPY main.py /main.py

CMD ["python", "/main.py"]
