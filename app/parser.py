from os.path import join

import app.types as types


class Parser:
    def parse(self, at: types.Path, locale: types.Locale) -> None:
        with open(join(at, locale)) as file:
            print(file.read())
