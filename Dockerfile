FROM python:latest

COPY main.py main.py

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "main.py" ]