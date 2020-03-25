from abc import ABC, abstractmethod
import geopandas


class Transformer(ABC):
    @classmethod
    @abstractmethod
    def transform(self, dataset):
        pass


class DistrictsTransformer(Transformer):
    @classmethod
    def transform(self, dataset):
        # Regions that have sea territories have two entries. For now,
        # select only land area in order to get unique records.
        dataset = dataset[dataset.GF == 4]
        return dataset
