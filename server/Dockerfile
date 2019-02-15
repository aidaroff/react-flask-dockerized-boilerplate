FROM python:3.7-alpine3.9
RUN apk add --no-cache --update python3-dev  gcc build-base

LABEL maintainer="Alibek Aidarov aydarov.alibek@gmail.com"

WORKDIR /home/server

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN source venv/bin/activate
RUN pip install -r requirements.txt

COPY app app
COPY main.py main.py

RUN touch .flaskenv \
    && echo "FLASK_APP=main.py" >> .flaskenv \
    && echo "FLASK_DEBUG=1" >> .flaskenv

CMD ["flask", "run", "--host=0.0.0.0"]