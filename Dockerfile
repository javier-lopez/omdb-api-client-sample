FROM python:alpine

RUN  apk add --no-cache gcc musl-dev libffi-dev libev-dev

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements*.txt /usr/src/app/
RUN  pip install --no-cache-dir -r requirements.txt
RUN  pip install --no-cache-dir -r requirements-test.txt

COPY . /usr/src/app
CMD [ "tox" ]

#  vim: set ts=8 sw=4 tw=0 ft=dockerfile :
