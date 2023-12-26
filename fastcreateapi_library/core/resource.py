from fastcreateapi_library.core.interfaces.architeture import ArchitectureStructure


class GenerateResource:

    def __init__(self, architecture: ArchitectureStructure) -> None:
        self.architecture = architecture

    def create_structure(self, path_directory: str = '.'):
        self.architecture.create(path_root=path_directory)
