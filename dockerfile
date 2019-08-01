FROM ubuntu:latest
WORKDIR /usr/bin/
RUN apt-get update
RUN echo "y" | apt-get install git