from typing import List
from os.path import join
from os import linesep

import aliases
from errors import ParserInvalidLineError


def parse(at: aliases.Path, locale: aliases.Locale) -> aliases.Vocabulary:
    with open(join(at, locale)) as file:
        lines = file.read().split(linesep)
        lines = _get_processed_lines(lines)

        if not _are_lines_valid(lines):
            raise ParserInvalidLineError(
                'A locale file is written with mistakes'
            )

        vocabulary: aliases.Vocabulary = {}
        _fill_vocabulary(vocabulary, lines)
        return vocabulary


def _get_processed_lines(lines: List[str]) -> List[str]:
    processed: List[str] = []
    for line in lines:  # type: str
        processed.append(' '.join(line.split()))


def _are_lines_valid(lines: List[str]) -> bool:
    return all([
        not len(tokens) < 3 and tokens[1] == '='
        for tokens in [line.split() for line in lines]
    ])


def _fill_vocabulary(vocabulary: aliases.Vocabulary, lines: List[str]) -> None:
    for line in lines:
        tokens = line.split()
        vocabulary[tokens[0]] = ' '.join(tokens[2:])
