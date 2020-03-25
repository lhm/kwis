from unittest.mock import MagicMock, patch
import pytest
import pandas as pd
from importer import pipeline, catalog, transformers


@patch("importer.catalog.get", MagicMock(return_value="foo"))
def test_read_dataset():
    task = pipeline.read_dataset
    result = task.run("bar")
    catalog.get.assert_called_with("bar")
    assert result == "foo"


class TestTransformer(transformers.Transformer):
    @classmethod
    def transform(self, dataset):
        dataset.A = dataset.A * 2
        return dataset


def test_transform():
    dataset = pd.DataFrame({"A": [1]})
    transformer = TestTransformer
    task = pipeline.transform
    result = task.run(dataset, transformer)
    assert result.to_dict("records") == [{"A": 2}]


def test_write_package(tmp_path):
    dataset = MagicMock()
    dataset.to_file = MagicMock()
    source_name = "foo"
    output_path = tmp_path / "foo.gpkg"

    with patch("importer.pipeline.data_dir", tmp_path):
        task = pipeline.write_package
        result = task.run(dataset, source_name)

    dataset.to_file.assert_called_with(output_path, layer=source_name, driver="GPKG")
