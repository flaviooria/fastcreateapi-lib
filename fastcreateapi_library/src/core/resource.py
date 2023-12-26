from core.interfaces.architeture import ArchitectureStructure


class GenerateResource:

    def __init__(self, architeture: ArchitectureStructure) -> None:
        self.architeture = architeture

    def create_structure(self):
        self.architeture.create()
