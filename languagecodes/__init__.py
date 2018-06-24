
from languagecodes.iso639 import ISO3_ALL, ISO2_MAP, ISO3_MAP
from languagecodes.util import normalize_code


def iso_639_alpha3(code):
    code = normalize_code(code)
    code = ISO3_MAP.get(code, code)
    if code in ISO3_ALL:
        return code


def iso_639_alpha2(code):
    code = iso_639_alpha3(code)
    return ISO2_MAP.get(code)
