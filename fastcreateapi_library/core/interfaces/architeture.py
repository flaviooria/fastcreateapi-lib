from abc import ABC, abstractmethod


class ArchitectureStructure(ABC):

    @abstractmethod
    def create(self, path_root: str) -> None:
        pass
