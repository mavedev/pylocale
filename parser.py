from typing import List
from os.path import join
from os import linesep

import aliases


def parse(at: aliases.Path, locale: aliases.Locale) -> aliases.Vocabulary:
    with open(join(at, locale)) as file:
        lines = file.read().split(linesep)
        lines = _get_processed_lines(lines)
        vocabulary: aliases.Vocabulary = {}


def _get_processed_lines(lines: List[str]) -> List[str]:
    processed: List[str] = []
    for line in lines:  # type: str
        processed.append(' '.join(line.split()))


def _are_lines_valid(lines: List[str]) -> bool:
    return all([
        not len(tokens) < 3 and tokens[1] == '='
        for tokens in [line.split() for line in lines]
    ])
