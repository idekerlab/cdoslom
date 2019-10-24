FROM continuumio/miniconda3

RUN pip install pandas
RUN pip install gprofiler-official

RUN mkdir /tmp/cdgprofiler
COPY dist/*.whl /tmp/cdgprofiler/

RUN pip install /tmp/cdgprofiler/cdgprofilergenestoterm*whl

RUN rm -rf /tmp/cdgprofiler

ENTRYPOINT ["/opt/conda/bin/cdgprofilergenestoterm.py"]
CMD ["--help"]
