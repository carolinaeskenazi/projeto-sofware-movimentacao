FROM python

COPY requirements.txt .

ENTRYPOINT ["python","app.py"]
