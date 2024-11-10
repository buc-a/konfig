import json
import subprocess
from typing import Dict, List, Set
import os

class DependencyGraph:
    def __init__(self, package_name: str, max_depth: int = 1):
        self.package_name = package_name
        self.max_depth = max_depth
        self.dependencies: Dict[str, Set[str]] = {}

    def get_dependencies(self) -> Dict[str, Set[str]]:

        dependencies = self._get_dependencies(self.package_name, 0, set())
        return dependencies

    def _get_dependencies(self, package: str, current_depth: int, visited: Set[str]) -> Dict[str, Set[str]]:

        if current_depth > self.max_depth:
            return self.dependencies

        if package in visited:
            return self.dependencies

        visited.add(package)
        self.dependencies[package] = set()

        try:
            json_deps = subprocess.check_output(['npm', 'view', package, 'dependencies', '--json'], shell=True).decode('utf-8')
            if json_deps:
                dependency_data = json.loads(json_deps)

                for dep_name, _ in dependency_data.items():
                    self.dependencies[package].add(dep_name)
                    self._get_dependencies(dep_name, current_depth + 1, visited)

        except subprocess.CalledProcessError:
            pass

        return self.dependencies

    def visualize(self, plantuml_path: str, output_path: str) -> None:

        plantuml_code = self._generate_plantuml_code()

        file_name = output_path.split('.')[0] + ".puml"

        with open(file_name, "w") as f:
            f.write(plantuml_code)

        subprocess.run(["java", "-jar", plantuml_path, "-tpng", file_name])

        os.remove(file_name)


    def _generate_plantuml_code(self) -> str:

        self.dependencies = self.get_dependencies()
        plantuml_code = "@startuml\n"

        for package, deps in self.dependencies.items():
            for dep in deps:
                plantuml_code += f"{package.replace('-','')} --> {dep.replace('-','')}\n"

        plantuml_code += "@enduml\n"
        return plantuml_code

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Визуализатор графа зависимостей npm-пакетов.")
    parser.add_argument("plantuml_path", help="Путь к исполняемому файлу PlantUML.")
    parser.add_argument("package_name", help="Имя анализируемого пакета.")
    parser.add_argument("output_path", help="Путь к файлу с изображением графа.")
    parser.add_argument(
        "-d", "--max_depth", type=int, default=1, help="Максимальная глубина анализа зависимостей."
    )

    args = parser.parse_args()

    graph = DependencyGraph(args.package_name, args.max_depth)

    graph.visualize(args.plantuml_path, args.output_path)

    print(f"Граф зависимостей для пакета '{args.package_name}' сохранен в '{args.output_path}'.")

if __name__ == "__main__":
    main()
