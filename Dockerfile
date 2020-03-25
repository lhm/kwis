FROM python:3.8 as builder
WORKDIR /build
COPY scripts/requirements.txt scripts/
COPY Makefile .
RUN make venv
COPY scripts/*.py scripts/
RUN make data/districts.gpkg
RUN make data/prtr_emissions.gpkg

FROM geopython/pygeoapi:latest
COPY --from=builder /build/data/*.gpkg /data/
COPY ./pygeoapi-config.yml /pygeoapi/local.config.yml
