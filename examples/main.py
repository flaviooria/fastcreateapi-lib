from fastcreateapi_library import FastCreateApiLibrary


def menu():
    print(
        '1. Crear estructura MSC\n'
        '2. Crear estructura HEX\n'
        '3. exit\n'
    )
    return input('Escoge algo: ')


def main():
    option = int(menu())
    arch = ''
    if option == 1:
        arch = 'MSC'
    else:
        arch = 'HEX'
        module_name = input('Indica el nombre del módulo: ')

    app = FastCreateApiLibrary(type_arch=arch)
    app.generate()


if __name__ == '__main__':
    main()
