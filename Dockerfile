FROM python:3.11

COPY requirements.txt .

COPY m.py .

RUN pip install -r requirements.txt
CMD [ "python","-u","m.py" ]
