import app.types as types
from .parser import parse


class PyLocale:
    def __init__(
        self,
        locales_path: types.Path,
        root_locale: types.Locale,
        strict_mode=False
    ) -> None:
        self._strict_mode = strict_mode
        self._vocabulary: types.Vocabulary = {}
        self._load_locales(locales_path, root_locale)

    def _load_locales(
        self, locales_path: types.Path,
        locale: types.Locale
    ) -> None:
        try:
            parse(locales_path, locale)
        except FileNotFoundError:
            if self._strict_mode:
                raise FileNotFoundError()
