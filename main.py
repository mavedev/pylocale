import aliases
from parser import parse
from errors import NoSuchLocaleError


class PyLocale:
    def __init__(
        self,
        *,
        at: aliases.Path,
        root: aliases.Locale,
        silent=False
    ) -> None:
        self._silent = silent
        self._vocabulary: aliases.Vocabulary = {}
        self._load_locales(at, root)

    def _load_locales(
        self, locales_path: aliases.Path,
        locale: aliases.Locale
    ) -> None:
        try:
            self._vocabulary = parse(locales_path, locale)
        except FileNotFoundError:
            if not self._silent:
                raise NoSuchLocaleError(
                    'The locale "{}" was not found'.format(locale)
                )
