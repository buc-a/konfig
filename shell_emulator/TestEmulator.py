import unittest

from App import App

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.emulator= App("user", "archive.zip")


if __name__ == '__main__':
    unittest.main()
