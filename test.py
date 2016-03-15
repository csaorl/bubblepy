import unittest

from bubblepy import BubbleBabble


class TestBB(unittest.TestCase):

    BB = BubbleBabble()

    TESTS = {
        ('', 'xexax'),
        ('abcd', 'ximek-domek-gyxox'),
        ('asdf', 'ximel-finek-koxex'),
        ('0123456789', 'xesaf-casef-fytef-hutif-lovof-nixix'),
        ('Testing a sentence.', 'xihak-hysul-gapak-venyd-bumud-besek-heryl-gynek-vumuk-hyrox'),
        ('1234567890', 'xesef-disof-gytuf-katof-movif-baxux'),
        ('Pineapple', 'xigak-nyryk-humil-bosek-sonax'),
    }

    def test_encode(self):
        """Test encoding valid values"""
        for src, encoded in self.TESTS:
            self.assertEqual(self.BB.encode(src), encoded)

    def test_decode(self):
        """Test decoding valid values"""
        for src, encoded in self.TESTS:
            self.assertEqual(self.BB.decode(encoded), src)
