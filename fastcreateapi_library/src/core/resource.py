from typing import Type

from core.interfaces.architeture import ArchitectureStructure


class GenerateResource:

    def __init__(self, architecture: Type[ArchitectureStructure]) -> None:
        self.architecture = architecture

    def create_structure(self):
        self.architecture.create()
