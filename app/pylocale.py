import app.types as types
from .parser import Parser


class PyLocale:
    def __init__(
        self,
        locales_path: types.Path,
        root_locale: types.Locale
    ) -> None:
        self._vocabulary: types.Vocabulary = {}
        self._load_locales(locales_path, root_locale)

    def _load_locales(
        self, locales_path: types.Path,
        root_locale: types.Locale
    ) -> None:
        parser = Parser()
        parser.parse(locales_path, root_locale)
