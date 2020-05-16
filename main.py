import aliases
from parser import parse
from errors import NoSuchLocaleError


class PyLocale:
    def __init__(
        self,
        locales_path: aliases.Path,
        root_locale: aliases.Locale,
        strict_mode=True
    ) -> None:
        self._strict_mode = strict_mode
        self._vocabulary: aliases.Vocabulary = {}
        self._load_locales(locales_path, root_locale)

    def _load_locales(
        self, locales_path: aliases.Path,
        locale: aliases.Locale
    ) -> None:
        try:
            parse(locales_path, locale)
        except FileNotFoundError:
            if self._strict_mode:
                raise NoSuchLocaleError(
                    'The locale "{}" was not found'.format(locale)
                )
