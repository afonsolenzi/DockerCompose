FROM python:3.9
RUN pip install mysql-connector-python pandas sqlalchemy pymysql Faker cryptography
WORKDIR /usr/app/src
COPY miniproject.py ./
CMD ["python", "miniproject.py"]
