from banal import ensure_list

from languagecodes.iso639 import ISO3_ALL, ISO2_MAP, ISO3_MAP
from languagecodes.synonyms import expand_synonyms
from languagecodes.util import normalize_code


def iso_639_alpha3(code):
    """Convert a given language identifier into an ISO 639 Part 2 code, such
    as "eng" or "deu". This will accept language codes in the two- or three-
    letter format, and some language names. If the given string cannot be
    converted, ``None`` will be returned.
    """
    code = normalize_code(code)
    code = ISO3_MAP.get(code, code)
    if code in ISO3_ALL:
        return code


def iso_639_alpha2(code):
    """Convert a language identifier to an ISO 639 Part 1 code, such as "en"
    or "de". For languages which do not have a two-letter identifier, or
    invalid language codes, ``None`` will be returned.
    """
    code = iso_639_alpha3(code)
    return ISO2_MAP.get(code)


def list_to_alpha3(languages, synonyms=True):
    """Parse all the language codes in a given list into ISO 639 Part 2 codes
    and optionally expand them with synonyms (i.e. other names for the same
    language)."""
    codes = set([])
    for language in ensure_list(languages):
        code = iso_639_alpha3(language)
        if code is None:
            continue
        codes.add(code)
        if synonyms:
            codes.update(expand_synonyms(code))
    return codes
