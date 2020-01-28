FROM centos:centos7


RUN yum -y install gcc gcc-c++ make wget tar gunzip

RUN mkdir /tmp/mini \
    && cd /tmp/mini \
    && wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && chmod a+x *.sh \
    && ./Miniconda3-latest-Linux-x86_64.sh -b -p /opt/miniconda3 \
    && cd /tmp \
    && rm -rf /tmp/mini

RUN mkdir /tmp/cdoslom
COPY dist/*.whl /tmp/cdoslom/

RUN /opt/miniconda3/bin/pip install /tmp/cdoslom/cdoslom*whl

RUN rm -rf /tmp/cdoslom

RUN mkdir -p /oslom \
        && curl -sL http://www.oslom.org/code/OSLOM2.tar.gz \
        | tar -zxC /oslom \
        && cd /oslom/OSLOM2 \
        && ls /oslom/OSLOM2 \
        && chmod 744 compile_all.sh \
        && ./compile_all.sh

ENTRYPOINT ["/opt/miniconda3/bin/cdoslom.py"]
CMD ["--help"]
