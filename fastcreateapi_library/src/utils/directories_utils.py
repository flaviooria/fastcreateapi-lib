import os
from pathlib import Path
from typing import Union


def exist_dir(path: Union[str, Path]):
    return Path(path).exists()


def create_directory(path: Union[str, Path] = '', *, path_directory_by_default: str):

    if not exist_dir(path_directory_by_default):
        raise Exception(
            f'{path_directory_by_default} not exists, please create and try again')

    create_path = Path(path_directory_by_default).joinpath(path)

    if not exist_dir(path_directory_by_default):
        os.mkdir(path_directory_by_default)

    if not exist_dir(create_path):
        os.mkdir(create_path)


def create_init_file(path: Union[str, Path]):
    filename = '__init__.py'
    path_abs = f'{path}/{filename}'

    with open(path_abs) as stream:
        stream.write('')
