import unittest
from main import DependencyGraph


class TestDependencyGraph(unittest.TestCase):

    def test_get_dependencies_0(self):
        graph = DependencyGraph("react", max_depth=0)
        dependencies = graph.get_dependencies()
        self.assertIn("loose-envify", dependencies["react"])
        self.assertNotIn("loose-envify", dependencies)

    def test_get_dependencies_1(self):
        graph = DependencyGraph("react", max_depth=1)
        dependencies = graph.get_dependencies()
        self.assertIn("js-tokens", dependencies["loose-envify"])

    def test_generate_plantuml_code(self):
        graph = DependencyGraph("react", max_depth=1)
        graph.get_dependencies()
        plantuml_code = graph._generate_plantuml_code()
        self.assertIn("@startuml", plantuml_code)
        self.assertIn("react --> looseenvify", plantuml_code)
        self.assertIn("looseenvify --> jstokens", plantuml_code)
        self.assertIn("@enduml", plantuml_code)

    def test_visualize_text(self):
        import os
        graph = DependencyGraph("react", max_depth=1)
        graph.visualize(".\\plantuml.jar", "graph.png")
        self.assertTrue(not os.path.exists("graph.puml"))

    def test_visualize_png(self):
        import os
        graph = DependencyGraph("react", max_depth=1)
        graph.visualize(".\\plantuml.jar", "graph.png")
        self.assertTrue(os.path.exists("graph.png"))




