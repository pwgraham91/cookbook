FROM python:3.7-alpine
LABEL maintainer="Peter Graham <pwgraham91@gmail.com>"

RUN mkdir /app
WORKDIR /app
COPY . /app
# pyre-check isn't on alpine
RUN sed -i "/pyre-check/d" requirements.txt
RUN apk update && \
 apk add postgresql-libs && \
 apk add --virtual .build-deps gcc musl-dev postgresql-dev && \
 pip install -r requirements.txt && \
 apk --purge del .build-deps
ENV FLASK_APP="main"
EXPOSE 5000
RUN flask run