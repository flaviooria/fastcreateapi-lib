from typing import List

from fastcreateapi_library.core.interfaces.architeture import \
    ArchitectureStructure
from fastcreateapi_library.utils.directories_utils import create_directory


class ArchitectureMsc(ArchitectureStructure):

    def create(self, path_root: str) -> None:
        print('Use architecture msc')

        for path in self.get_folders:
            create_directory(path, path_directory_by_default=path_root)

    @property
    def get_folders(self) -> List[str]:
        return ['models', 'services', 'controller']
