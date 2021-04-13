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
import shutil
import unittest
import pyback as pb

# print(os.path.dirname(os.path.abspath(__file__)) == os.getcwd())

class TestPB(unittest.TestCase):

    _DIR_SOURCE = 'source_dir'
    _DIR_SUBFOLDER = 'source_sub_dir'
    _DIR_DESTINATION = 'dest_dir'
    _XTN = {
        'tar': 'tar',
        'gztar': 'tar.gz',
        'bztar': 'tar.bz2',
        'xztar': 'tar.xz',
        'zip': 'zip'
    }

    @classmethod
    def setUpClass(self):
        '''
        Create test source & destination directories

        ./
            - test.py
            - source_dir
                - source_sub_dir
                    - sample_sub_file.txt
                - sample_source.txt
                - sample_source.md
            - dest_dir

        '''
        print('Creating testing folders.')
        if not os.path.exists(self._DIR_SOURCE):
            os.mkdir(self._DIR_SOURCE)
            os.chdir(self._DIR_SOURCE)
            os.mkdir(self._DIR_SUBFOLDER)
            os.chdir(self._DIR_SUBFOLDER)
            with open('sample_sub_file.txt', 'w') as txt:
                pass
            os.chdir('../')
            with open('sample.txt', 'w') as txt:
                pass
            with open('sample.md', 'w') as md:
                pass
            os.chdir('../')
            os.mkdir(self._DIR_DESTINATION)

            # create compressed files of each extension type
            for ext in self._XTN:
                pb.compress(self._DIR_SOURCE, os.path.join(self._DIR_DESTINATION, 'COMPRESSED'), ext)



    @classmethod
    def tearDownClass(self):
        # delete test folders
        shutil.rmtree(self._DIR_SOURCE)
        shutil.rmtree(self._DIR_DESTINATION)
        print('Testing folders deleted.')

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_compressed(self):
        '''
        Test if compression was created for each extension type
        '''
        for ext in self._XTN:
            self.assertTrue(os.path.exists(os.path.join(self._DIR_DESTINATION, 'COMPRESSED.{}'.format(self._XTN[ext]))))

if __name__ == '__main__':
    unittest.main()
