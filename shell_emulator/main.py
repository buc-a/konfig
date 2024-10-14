from pathlib import Path
import argparse

from App import App

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("hostname", help="Имя компьютера для приглашения")
    parser.add_argument("vfs_path", help="Путь к архиву виртуальной файловой системы")
    args = parser.parse_args()
    app = App(args.hostname, Path(args.vfs_path))
    app.run()

if __name__ == "__main__":
    main()