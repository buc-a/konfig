class TestConfigConverter(unittest.TestCase):

    def setUp(self):
        self.parser = Lark(grammar)  # Создаем парсер один раз для всех тестов
        self.transformer = ConfigTransformer()

    def test_simple_config(self):
        input_text = """
config {
  param1 = 10,
  param2 = "test"
}
"""
        expected = {"config": {"param1": 10, "param2": "test"}}
        self.assertEqual(self.transformer.transform(self.parser.parse(input_text)), expected)

    def test_config_with_constants(self):
        input_text = """
NB. Конфигурация базы данных
max_conn : 100 ;
timeout : @"30" ;
config {
  host : 19216801,
  port : 5432,
  max_connections : ${max_conn},
  connection_timeout : ${timeout}
}
"""
        expected = {"config": {"host": 19216801, "port": 5432, "max_connections": 100, "connection_timeout": "30"}}
        self.assertEqual(self.transformer.transform(self.parser.parse(input_text)), expected)

    def test_config_with_array(self):
        input_text = """
config {
  arr: '(1 2 3)'
}
"""
        expected = {"config": {"arr": [1, 2, 3]}}
        self.assertEqual(self.transformer.transform(self.parser.parse(input_text)), expected)

    def test_config_with_nested_dict(self):
        input_text = """
config {
  nested: {
    a: 1,
    b: "hello"
  }
}
"""
        expected = {"config": {"nested": {"a": 1, "b": "hello"}}}
        self.assertEqual(self.transformer.transform(self.parser.parse(input_text)), expected)

    def test_config_with_multi_line_comment(self):
        input_text = """
|#
Многострочный комментарий
#|
config {
  param1: 1
}
"""
        expected = {"config": {"param1": 1}}
        self.assertEqual(self.transformer.transform(self.parser.parse(input_text)), expected)

    def test_error_handling_unexpected_char(self):
        input_text = "config { param1 = 10, param2 = @@test }"
        result = parse_config(input_text)
        self.assertTrue("Unexpected Characters" in result)

    def test_error_handling_lark_error(self):
        input_text = "config { param1 = 10, param2 = test }"  # Missing quotes
        result = parse_config(input_text)
        self.assertTrue("Ошибка при обработке" in result)
    def test_error_handling_json_decode_error(self):
        input_text = """
config {
  param1: 10,
  param2: 'invalid json'
}
"""
        result = parse_config(input_text)
        # Проверка на наличие ошибки JSONDecodeError, так как мы  не обрабатываем ошибку здесь
        self.assertTrue("Ошибка JSON" in result)


    def test_duplicate_constant(self):
        input_text = """
max_conn : 100;
max_conn : 200;
config {}
"""
with self.assertRaises(LarkError):
            self.parser.parse(input_text)


    def test_undefined_constant(self):
        input_text = """
config {
  param: ${undefined}
}
"""
        with self.assertRaises(ValueError) as context:
          self.transformer.transform(self.parser.parse(input_text))
        self.assertTrue("неизвестная константа" in str(context.exception))

    def test_empty_config(self):
        input_text = "config {}"
        expected = {"config": {}}
        self.assertEqual(self.transformer.transform(self.parser.parse(input_text)), expected)

    def test_config_with_only_comments(self):
        input_text = """
NB. Only comments
|# multiline comment
#|
"""
        result = self.transformer.transform(self.parser.parse(input_text))
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
