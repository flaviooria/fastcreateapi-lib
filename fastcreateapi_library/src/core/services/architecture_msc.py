from typing import List

from core.interfaces.architeture import ArchitectureStructure
from utils.directories_utils import create_directory


class ArchitectureMsc(ArchitectureStructure):

    def create(self) -> None:
        print('Use architecture msc')

        for path in self.get_folders:
            create_directory(path, path_directory_by_default='')

    @property
    def get_folders(self) -> List[str]:
        return ['models', 'services', 'controller']
