__all__ = [
    "Index"
]
class Index:

    def __init__(self, line, column):
        self.line = line
        self.column = column

    def add_column(self, k):
        self.column = k

    def add_line(self, k):
        self.line += k

    def to_str(self):
        return f"{self.line}.{self.column}"
