FROM python:3.11

WORKDIR /app

COPY requirements.txt .

COPY m.py .

RUN pip install -r requirements.txt
CMD [ "python","./m.py" ]
