FROM node:lts-alpine
WORKDIR /fe
COPY ./package.json .
COPY *.js .
COPY jsconfig.json .
RUN npm install