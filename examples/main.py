from fastcreateapi_library import ConfigArchitecture, FastCreateApiLibrary


def menu():
    print(
        '1. Crear estructura MSC\n'
        '2. Crear estructura HEX\n'
        '3. exit\n'
    )
    return input('Escoge algo: ')


def main():
    try:

        option = int(menu())
        arch = ''
        config: ConfigArchitecture = ConfigArchitecture()

        if option == 1:
            arch = 'MSC'
        else:
            arch = 'HEX'
            module_name = input('Indica el nombre del módulo: ').strip()
            config.module = module_name

        app = FastCreateApiLibrary(type_arch=arch)

        if config.module is not None:
            app.config = config

        app.generate()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
