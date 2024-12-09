import sys
import json
import re
from lark import Lark, Transformer, exceptions, LarkError

# Грамматика конфигурационного языка
grammar = """
start: (const_decl | COMMENT | COMMENT_MULT)* config

COMMENT: "NB." /.+/
COMMENT_MULT: "|#" /(.|\n)*?#\|/

config: NAME conf
conf: "{" [pair ("," pair)*] "}"

const_decl: NAME ":" value ";"
const_eval: "${" NAME "}"

value:  NUMBER | dict | const_eval | string | array

array: "'(" [value (" " value)*] ")" 
dict: "({" [pair ("," pair)*] "})"
pair: NAME ":" value
string: /@"[^"]*"/
NAME: /[a-zA-Z][_a-zA-Z0-9]*/

%import common.NUMBER
%import common.WS
%ignore WS
%ignore COMMENT
"""

# Инициализация Lark парсера
config_parser = Lark(grammar)

class ConfigTransformer(Transformer):
    def __init__(self):
        super().__init__()
        self.constants = {}  # Хранилище для констант

    # Обработка точки старта
    def start(self, value):
        return value[-1]

    # Обработка записи константы
    def const_decl(self, tupl):
        name, value = tupl
        if name in self.constants:
            raise LarkError(f"Константа {name} уже объявлена")
        self.constants[name] = value

    # Обработка вычисления константы
    def const_eval(self, value):
        name = value[0]
        if name not in self.constants:
            raise ValueError(f"В конфигурации использована неизвестная константа по имени {name}")
        return self.constants[name]

    # Обработка корневого узла
    def config(self, value):
        name, info = value
        info = info.children[0]
        #\"{name}\" :
        return f"{{ {info} }}"

    # Обработка пары ключ-значение в словаре
    def pair(self, value):

        key, val = value
        return f" \"{key}\": {val}  ,"

    #обработка массивов
    def array(self, items):
        result = "[ "
        for item in items:
            if item is not None:
                result += str(item) + ", "
        result += "]"
        return result

    # Обработка словаря
    def dict(self, items):
        result = "{ "
        # Словарь состоит из нескольких пар, каждая пара обработана через 'pair'
        for item in items:
            if item is not None:
                result += item
        result += " }"
        return result

    def string(self, string):
        return string[0][1:]
    # Обработка чисел
    def NUMBER(self, token):
        return int(token)

    # Обработка имён
    def NAME(self, token):
        return str(token)

    # Обработка значения (которое может быть числом или словарём)
    def value(self, tupl):
        return tupl[0]

    def COMMENT_MULT(self, comment):
        text = comment[0]
        cleaned_text = text[2:-2].strip()  # Удаляем "|#" и "#|" и лишние пробелы
        print(f"Многострочный комментарий:\n{cleaned_text}")
        return None

# Функция для парсинга и обработки ошибок
def parse_config(input_text):
    try:
        # Парсинг входного текста
        tree = config_parser.parse(input_text)

        # Преобразование дерева в XML
        transformer = ConfigTransformer()
        xml_output = transformer.transform(tree)
        return xml_output
    except exceptions.UnexpectedCharacters as uc:
        return f"Unexpected Characters:\n{str(uc)}"
    except exceptions.LarkError as le:
        return f"Ошибка при обработке:\n{str(le)}"



if __name__ == "__main__":
    input_text = sys.stdin.read()
    json_str = parse_config(input_text)


    fixed_json_string2 = re.sub(r'\s+', '', json_str)  # Убираем ВСЕ пробелы
    fixed_json_string2 = fixed_json_string2.replace(",]", "]")  # Удаляет запятую после 14
    fixed_json_string2 = fixed_json_string2.replace(",}", "}")
    try:
        data = json.loads(fixed_json_string2)
        print(json.dumps(data, indent=4))
    except json.JSONDecodeError as e:
        print(f"Ошибка JSON: {e}")

