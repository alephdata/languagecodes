from unittest import TestCase

from languagecodes import iso_639_alpha3, iso_639_alpha2
from languagecodes import list_to_alpha3


class CodesTest(TestCase):
    def test_alpha3(self):
        self.assertIsNone(iso_639_alpha3(""))
        self.assertIsNone(iso_639_alpha3(None))
        self.assertIsNone(iso_639_alpha3(6))
        self.assertIsNone(iso_639_alpha3("banana"))
        self.assertEquals(iso_639_alpha3("gub"), "gub")
        self.assertEquals(iso_639_alpha3("en"), "eng")
        self.assertEquals(iso_639_alpha3("eng"), "eng")
        self.assertIsNone(iso_639_alpha3("yu"))

    def test_alpha2(self):
        self.assertIsNone(iso_639_alpha2(""))
        self.assertIsNone(iso_639_alpha2("banana"))
        self.assertIsNone(iso_639_alpha2("gub"))
        self.assertEquals(iso_639_alpha2("eng"), "en")

    def test_list(self):
        assert "srp" in list_to_alpha3("bs")
        assert "srp" not in list_to_alpha3("bs", synonyms=False)
        assert "deu" in list_to_alpha3(["bs", "de"])
