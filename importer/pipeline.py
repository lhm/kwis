from prefect import task, Flow
import intake
from pathlib import Path
from .transformers import DistrictsTransformer
import importer.catalog as catalog

loader_dir = Path(__file__).parent.resolve()
root = loader_dir.parent
data_dir = root / "data"


@task
def read_dataset(source_name):
    dataset = catalog.get(source_name)

    return dataset


@task
def transform(dataset, transformer):
    dataset = transformer.transform(dataset)
    return dataset


@task
def write_package(dataset, source_name):
    target_path = data_dir / f"{source_name}.gpkg"
    dataset.to_file(target_path, layer=source_name, driver="GPKG")
    return target_path


def main():
    with Flow("etl") as flow:
        source_data = read_dataset()
        transformed = transform(source_data)

    flow.run()


if __name__ == "__main__":
    main()
