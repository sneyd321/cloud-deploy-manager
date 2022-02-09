FROM python

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV FLASK_APP=main


#CMD ["python", "./main.py"]
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
