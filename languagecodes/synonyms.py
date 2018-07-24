# This is a set of synonyms for pragmatic usage in NLP. It is based on
# working with Tesseract 3.04, but should be applicable elsewhere.

LANG_SYNONYMS = [
    ('srp', 'hbs', 'hrv', 'bos'),
    ('sli', 'alb'),
    ('slk', 'slo'),
    ('ron', 'rum'),
    ('nor', 'non'),
    ('nld', 'dut'),
    ('mya', 'bur'),
    ('msa', 'may'),
    ('mkd', 'mac'),
    ('kat', 'geo'),
    ('isl', 'ice'),
    ('isl', 'ice'),
    ('fre', 'fra', 'frm'),
    ('fas', 'per'),
    ('eus', 'baq'),
    ('ell', 'gre'),
    ('ger', 'deu'),
    ('wel', 'cym'),
    ('chi_sim', 'chi_tra', 'chi', 'zho'),
    ('ces', 'cze'),
    ('bod', 'tib'),
    ('aze_cyrl', 'aze'),
]


def expand_synonyms(language):
    """Expand a language code into a set of codes."""
    for synonyms in LANG_SYNONYMS:
        if language in synonyms:
            return synonyms
    return [language]
