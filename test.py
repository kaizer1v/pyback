'''
automated tests for pyback

Test for
1. no source, no destination = Error to enter source
2. yes source, no destination = Default path of destination should be parent folder of source
3. yes source but wrong = Error path doesn't exist
4. yes source, yes destination but dest path doesn't exist = should create a path, check if it has been created
5. format is given but doesn't exist = Error & show available formats
6.
'''
import os
import unittest
import pyback as pb

class TestPB(unittest.TestCase):

    _SOURCE = 'test/source'
    _XTN = {
        'tar': 'tar',
        'gztar': 'tar.gz',
        'bztar': 'tar.bz2',
        'xztar': 'tar.xz',
        'zip': 'zip'
    }

    def sample(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_compressed(self):
        pb.compress(self._SOURCE, 'test_compressed', 'tar')
        self.assertTrue(os.path.exists('test_compressed.tar'))

    def test_no_dest(self):
        pb.compress(self._SOURCE, '', 'tar')
        self.assertTrue(os.path.exists(os.path.join('test', 'source.tar')))

    def test_wrong_ext(self):
        for frmt in pb._FORMATS:
            print('Checking for source.{}'.format(self._XTN[frmt]))
            pb.compress(self._SOURCE, '', frmt)
            self.assertTrue(os.path.exists(os.path.join('test', 'source.{}'.format(self._XTN[frmt]))))

if __name__ == '__main__':
    unittest.main()
