FROM python:3.11-slim

RUN pip install magister flask

COPY main.py /main.py

CMD ["python", "/main.py"]
