from abc import ABC, abstractclassmethod


class Importer(ABC):
    @classmethod
    @abstractclassmethod
    def import_data(self, path):
        raise ValueError("Arquivo iválido")
