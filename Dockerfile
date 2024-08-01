FROM python:3.12

RUN apt install libegl1

ADD . ./
RUN pip install -r ./requirements.txt
CMD ["python", "./app.py"]



