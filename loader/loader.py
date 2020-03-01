import intake
import pandas as pd
import geopandas
from sqlalchemy import create_engine
import click
import os

class Loader:
    source_name = None
    target_name = None

    def __init__(self, catalog_path, db_uri):
        self.dataset = None
        self.catalog = intake.open_catalog(catalog_path)
        self.db_uri = db_uri

    def read(self):
        self.dataset = self.catalog[self.source_name].read()

    def transform(self):
        pass

    def load(self):
        engine = create_engine(self.db_uri)
        self.dataset.to_postgis(
            con=engine, name=self.target_name, if_exists='replace'
        )

class DistrictsLoader(Loader):
    source_name = 'districts'
    target_name = 'vg250_districts'

    def transform(self):
        df = self.dataset
        # Regions that have sea territories have two entries. For now,
        # select only land area in order to get unique records.
        df = df[df.GF == 4]
        self.dataset = df

loaders = {
    'districts': 'DistrictsLoader'
}

@click.command()
@click.argument('source')
@click.option('--catalog', default='catalog.yml', help='Path to catalog yml')
@click.option('--db_uri', help='Database URI')
def cli(source, catalog, db_uri):
    if db_uri is None:
        db_uri = os.environ.get(
            'DB_URI', 'postgresql+psycopg2://docker:docker@localhost:5432/gis'
        )

    loader_name = loaders[source]
    loader_class = globals()[loader_name]
    loader = loader_class(catalog, db_uri)

    loader.read()
    loader.transform()
    loader.load()

if __name__ == '__main__':
    cli()
