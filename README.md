# languagecodes

[![Build Status](https://travis-ci.org/alephdata/languagecodes.png?branch=master)](https://travis-ci.org/alephdata/languagecodes)

This library helps to normalise the ISO 639 codes used to describe languages from
two-letter codes to three letters, and vice versa.

```python
import languagecodes

assert 'eng' == languagecodes.iso_639_alpha3('en')
assert 'eng' == languagecodes.iso_639_alpha3('ENG ')
assert 'en' == languagecodes.iso_639_alpha2('ENG ')
```

You can install the library from the Python package index:

```bash
pip install languagecodes
```

Uses data from: https://iso639-3.sil.org/
See also: https://www.loc.gov/standards/iso639-2/php/code_list.php
