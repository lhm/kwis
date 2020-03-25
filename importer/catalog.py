import os
import intake

catalog_path = os.path.join(os.path.dirname(__file__), "catalog.yml")


def get(source_name):
    catalog = intake.open_catalog(catalog_path)
    dataset = catalog[source_name].read()
    return dataset
