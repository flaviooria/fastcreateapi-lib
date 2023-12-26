from pathlib import Path
from typing import List

from core.interfaces.config import ConfigArchitecture
from utils.directories_utils import create_directory

from fastcreateapi_library.core.interfaces.architeture import \
    ArchitectureStructure


class ArchitectureHexagonal(ArchitectureStructure):

    def __init__(self, config: ConfigArchitecture):
        self.module_name = None
        self._config = config

    def create(self, path_root: str) -> None:
        print('Use architecture hexagonal')

        if self._config.module is None or self._config.module == '':
            raise Exception('Module name is not defined')

        self.module_name = self._config.module

        create_directory(self.module_name, path_directory_by_default=path_root)
        path_module_folder = Path(self.module_name).resolve()

        for folder in self.get_folders:
            create_directory(
                folder, path_directory_by_default=path_module_folder)

    @property
    def get_folders(self) -> List[str]:
        return ['domain', 'services', 'infrastructure']
