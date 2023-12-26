from typing import Optional, Union

from constants.types import Arch
from core.interfaces.config import ConfigArchitecture
from core.resource import GenerateResource
from core.services.architecture_hex import ArchitectureHexagonal
from core.services.architecture_msc import ArchitectureMsc


class FastCreateApiLibrary:
    def __init__(self, type_arch: Arch = 'MSC', *, config: Optional[ConfigArchitecture] = None):
        self.type_arch = type_arch
        self._config = config

    @property
    def config(self) -> Union[ConfigArchitecture, None]:
        return self._config

    @config.setter
    def config(self, config: ConfigArchitecture) -> None:
        self._config = config

    def generate(self):
        if self.type_arch == 'MSC':
            GenerateResource(ArchitectureMsc()).create_structure()
        else:
            GenerateResource(ArchitectureHexagonal(
                config=self.config)).create_structure()
