from prefect import task, Flow
import intake
import geopandas
from pathlib import Path

loader_dir = Path(__file__).parent.resolve()
root = loader_dir.parent
data_dir = root / "data"
catalog_path = loader_dir / "catalog.yml"


@task
def read_dataset():
    source_name = "districts"

    catalog = intake.open_catalog(str(catalog_path))
    dataset = catalog[source_name].read()

    return dataset


@task
def transform(dataset):
    # Regions that have sea territories have two entries. For now,
    # select only land area in order to get unique records.
    dataset = dataset[dataset.GF == 4]
    return dataset


@task
def write_package(dataset):
    target_path = data_dir / "districts.gpkg"
    dataset.to_file(target_path, layer="districts", driver="GPKG")
    return target_path


def main():
    with Flow("etl") as flow:
        source_data = read_dataset()
        transformed = transform(source_data)
        write_package(transformed)

    flow.run()


if __name__ == "__main__":
    main()
