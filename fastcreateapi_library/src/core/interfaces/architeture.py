from abc import ABC, abstractmethod


class ArchitectureStructure(ABC):

    @abstractmethod
    def create(self) -> None:
        pass
