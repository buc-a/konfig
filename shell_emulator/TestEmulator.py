import unittest

from App import App

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.emulator= App("user", "user_root.zip")

    def test_history_1(self):
        self.assertIn("История команд пуста", self.emulator.history())

    def test_ls_1(self):
        self.assertIn ("directory1", self.emulator.ls('/'), "ls_test_1")
        self.assertIn("file.txt", self.emulator.ls('/'), "ls_test_1")
        self.assertIn("directory2", self.emulator.ls('/'), "ls_test_1")

    def test_ls_2(self):
        self.assertIn ("directory1", self.emulator.ls(''), "ls_test_2")
        self.assertIn("directory2", self.emulator.ls(''), "ls_test_2")
        self.assertIn("file.txt", self.emulator.ls(''), "ls_test_2")

    def test_ls_3(self):
        self.assertIn("file1.txt", self.emulator.ls(['directory1']), "ls_test_3")

    def test_history_2(self):
        self.assertIn("ls /", self.emulator.history())
        self.assertIn("ls", self.emulator.history())
        self.assertIn("ls directory1", self.emulator.history())

    def test_cd_1(self):
        self.assertIn("Некорректный путь", self.emulator.cd('..'), "cd_test_1")


    def test_uniq_1(self):
        self.assertIn("Необходимо указать файл\n", self.emulator.uniq(''), "uniq_test_1")

    def test_uniq_2(self):
        self.assertIn("repeat1\nno_rep_1\nno_rep_2\nrepeat2\n", self.emulator.uniq(['file.txt']), "uniq_test_2")

    def test_uniq_3(self):
        self.assertIn("Файл noname.txt не найден\n", self.emulator.uniq(['noname.txt']), "uniq_test_3")

    def test_cp_1(self):
        self.assertIn("Недостаточно аргументов", self.emulator.cp(['file.txt']), "cp_test_1")

    def test_cp_2(self):
        self.assertIn("noname.txt - не существует такого файла", self.emulator.cp(['noname.txt', 'dir2']), "cp_test_1")


if __name__ == '__main__':
    unittest.main()
