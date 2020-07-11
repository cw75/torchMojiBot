FROM ubuntu:18.04

USER root
RUN apt-get update --fix-missing
RUN apt-get install -y software-properties-common wget python3-distutils python3-pip git 

RUN pip3 install git+https://github.com/cw75/torchMoji

RUN mkdir /model

COPY model/pytorch_model.bin /model/
COPY model/vocabulary.json /model/
COPY emojibot-sagemaker.py /

ENTRYPOINT ["python3.6", "emojibot-sagemaker.py"]