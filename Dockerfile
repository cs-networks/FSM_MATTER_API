FROM python:3.6-alpine

run apk --no-cache add --virtual native-deps \
  g++ gcc libgcc libstdc++ linux-headers make

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8763

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]