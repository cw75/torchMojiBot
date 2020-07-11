FROM ubuntu:18.04

USER root
RUN apt-get update --fix-missing
RUN apt-get install -y software-properties-common wget python3-distutils python3-pip git 

RUN pip3 install git+https://github.com/cw75/torchMoji
RUN pip3 install Flask

RUN mkdir /model

COPY model/pytorch_model.bin /model/
COPY model/vocabulary.json /model/
COPY emojibot-sagemaker.py /

ENV FLASK_APP emojibot-sagemaker.py
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

ENTRYPOINT flask run --host=0.0.0.0 --port=8080