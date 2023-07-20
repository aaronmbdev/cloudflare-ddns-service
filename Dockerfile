FROM python:3.11-slim

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y --no-install-recommends build-essential gcc dash curl

RUN python -m venv /opt/venv
ENV PATH='/opt/venv/bin:/usr/local/bin:/usr/bin:$PATH'

WORKDIR /usr/src/app

ADD ./ .

RUN pip install .

ENTRYPOINT ["ddns"]
