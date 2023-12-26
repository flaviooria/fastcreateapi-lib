from core.resource import GenerateResource
from core.services.architecture_msc import ArchitectureMsc


def menu():
    print(
        '1. Crear estructura MSC\n'
        '2. Crear estructura HEX\n'
        '3. exit\n'
    )
    return input('Escoge algo: ')


if __name__ == '__main__':
    option = int(menu())

    if option == 1:
        resource = GenerateResource(ArchitectureMsc)
        resource.create_structure()
