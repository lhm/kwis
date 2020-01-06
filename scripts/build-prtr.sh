#!/usr/bin/env bash

ogr2ogr -f GPKG prtr_emissions.gpkg prtr_emissions.geojson

# csv to postgis
# ogr2ogr -f PGDump prtr-emissions.sql data/prtr-emissions.csv -oo X_POSSIBLE_NAMES=geo_long* -oo Y_POSSIBLE_NAMES=geo_lat* -a_srs 'EPSG:4326'
