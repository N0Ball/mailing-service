FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN python3 -m pip install pip --upgrade 
RUN python3 -m pip install -r requirements.txt

COPY app .

ENTRYPOINT [ "python3", "server.py" ]