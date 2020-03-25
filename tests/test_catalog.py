from unittest.mock import MagicMock, patch
import pytest
import os
import pandas as pd
from importer import catalog

test_catalog_path = os.path.join(os.path.dirname(__file__), "catalog.yml")


def test_default_catalog_path():
    assert os.path.exists(catalog.catalog_path)


@patch("importer.catalog.catalog_path", test_catalog_path)
def test_get():
    result = catalog.get("dataset")
    assert isinstance(result, pd.DataFrame)
    assert result.to_dict("records") == [{"A": 1}]
