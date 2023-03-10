# FROM python:3.8.3 AS celery_alone

ARG BASE_CONTAINER=condaforge/mambaforge:latest
FROM $BASE_CONTAINER

ARG python=3.8
ARG release

SHELL ["/bin/bash", "-c"]

ENV PATH /opt/conda/bin:$PATH
ENV PYTHON_VERSION=${python}
ENV DASK_VERSION=${release}
RUN echo ${release}
RUN echo ${python}
RUN pwd
# ARG pwd_val=${RUN pwd}
RUN echo pwd
# RUN echo pwd_val
COPY requirements.txt .
# COPY DisconnectDask3.py .
COPY retailligence-backend .

# ECHO ${WORKDIR}
# RUN pwd
# RUN ECHO ${$PWD}
RUN python3 -m pip install pip \
    && pip install -U flask-cors \
    && python -m pip install pandas==1.0.1 \
                            numpy==1.20.3 \
                            "dask[complete]"==2021.10.0 \
                            dask-distance==0.2.0 \
                            dask-gateway==0.9.0 \
                            dask-glm==0.2.0 \
                            dask-kubernetes==0.11.0 \
                            dask-ml==1.9.0 \
    && pip install -r requirements.txt \
    && conda install -c anaconda cytoolz==0.11.0 \
    && find /opt/conda/ -type f,l -name '*.a' -delete \
    && find /opt/conda/ -type f,l -name '*.pyc' -delete \
    && find /opt/conda/ -type f,l -name '*.js.map' -delete \
    && /opt/conda/bin/conda clean -afy \
    && find /opt/conda/lib/python*/site-packages/bokeh/server/static -type f,l -name '*.js' -not -name '*.min.js' -delete \
    && rm -rf /opt/conda/pkgs

COPY prepare.sh /usr/bin/prepare.sh

RUN mkdir /opt/app

EXPOSE 8786
EXPOSE 8787
RUN chmod +x /usr/bin/prepare.sh

ENTRYPOINT ["tini", "-g", "--", "/usr/bin/prepare.sh"]