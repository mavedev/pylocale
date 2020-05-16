from os.path import join

import app.types as types


def parse(at: types.Path, locale: types.Locale) -> None:
    with open(join(at, locale)) as file:
        print(file.read())
