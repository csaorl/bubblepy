# coding=utf-8
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

    NON_ASCII = u'Pchnąć w tę łódź jeża lub ośm skrzyń fig'

    def test_encode(self):
        """Test encoding valid values"""
        for src, encoded in self.TESTS:
            self.assertEqual(self.BB.encode(src), encoded)

    def test_encode_bytes(self):
        """Test encoding valid values converted to bytes"""
        for src, encoded in self.TESTS:
            self.assertEqual(self.BB.encode(src.encode('utf-8')), encoded)

    def test_encode_nonascii(self):
        """Non-ASCII characters should raise errors"""
        with self.assertRaises(ValueError):
            self.BB.encode(self.NON_ASCII)

    def test_encode_utf8(self):
        """Encoding text with UTF-8 should allow to use bubble babble"""
        utf = self.NON_ASCII.encode('utf-8')
        bb = self.BB.encode(utf)
        decoded = self.BB.decode(bb).decode('utf-8')
        self.assertEqual(decoded, self.NON_ASCII)


    def test_decode(self):
        """Test decoding valid values"""
        for src, encoded in self.TESTS:
            self.assertEqual(self.BB.decode(encoded).decode('utf-8'), src)
