from fastcreateapi_library.core.interfaces.architeture import ArchitectureStructure


class ArchitectureHexagonal(ArchitectureStructure):

    def create(self, path_root: str) -> None:
        print('Use architecture hexagonal')
