FROM python:3.11

COPY requirements.txt .

COPY m.py .
COPY loaderio-2d5f2b4af6ad887461327720e88c6c2c.txt .


RUN pip install -r requirements.txt
CMD [ "python","-u","m.py" ]
