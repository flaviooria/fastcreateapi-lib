from abc import ABC, abstractmethod


class ArchitectureStructure(ABC):

    @abstractmethod
    def create() -> None:
        pass
