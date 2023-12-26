from constants.types import Arch
from core.resource import GenerateResource
from core.services.architecture_hex import ArchitectureHexagonal
from core.services.architecture_msc import ArchitectureMsc


class FastCreateApiLibrary:
    def __init__(self, type_arch: Arch = 'MSC'):
        self.type_arch = type_arch

    def generate(self):
        if self.type_arch == 'MSC':
            GenerateResource(ArchitectureMsc()).create_structure()
        else:
            GenerateResource(ArchitectureHexagonal()).create_structure()
