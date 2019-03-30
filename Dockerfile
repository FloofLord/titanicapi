FROM ubuntu:rolling

RUN apt-get update && apt-get upgrade -y  && apt-get install python3 -y && apt-get install python3-pip -y && apt-get install python-setuptools -y

RUN pip3 install scikit-learn flask-restful requests pandas numpy scipy 

COPY  . /model
WORKDIR  /model/model
ENV ml_debug_level=1
ENV enviroment PRODUCTION
ENTRYPOINT [ "python3" ]
CMD ["backend.py"]
