import unittest
import imp
git_ftp = imp.load_source("git_ftp", "git-ftp.py")

class TestSequenceFunctions(unittest.TestCase):
    def testLoadFtpignore(self):
        self.assert_(['sass/', 'config.rb'] == git_ftp.loadFtpignore('test/ftpignore'))
    def testFileIgnore(self):
        ignoreLines = git_ftp.loadFtpignore('test/ftpignore')
        self.assert_(git_ftp.ignore('config.rb', ignoreLines))
    def testFileNotIgnore(self):
        ignoreLines = git_ftp.loadFtpignore('test/ftpignore')
        self.assert_(git_ftp.ignore('notignore', ignoreLines)==False)
    def testFileNotIgnore2(self):
        ignoreLines = git_ftp.loadFtpignore('test/ftpignore')
        self.assert_(git_ftp.ignore('sassa', ignoreLines)==False)
    def testDirIgnore(self):
        ignoreLines = git_ftp.loadFtpignore('test/ftpignore')
        self.assert_(git_ftp.ignore('sass/test.txt', ignoreLines))

if __name__ == '__main__':
    unittest.main()