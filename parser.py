from typing import List
from os.path import join
from os import linesep

import aliases as aliases


def parse(at: aliases.Path, locale: aliases.Locale) -> None:
    with open(join(at, locale)) as file:
        lines = file.read().split(linesep)
        lines = _get_processed_lines(lines)


def _get_processed_lines(lines: List[str]) -> List[str]:
    processed: List[str] = []
    for line in lines:  # type: str
        processed.append(' '.join(line.split()))
