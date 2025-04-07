from python:3.8.10-slim-buster
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*
rom python:3.8.10-slim-buster

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    sotware-properties-common \
    git \
    && rm -r /var/lib/apt/lists/*

RUN curl -sSL URL_ADDRESSRUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm install -g npm@latest
RUN npm install -g @angular/cli@latest

CMD ["npm", "start"]