from os.path import join

import aliases as aliases


def parse(at: aliases.Path, locale: aliases.Locale) -> None:
    with open(join(at, locale)) as file:
        print(file.read())
