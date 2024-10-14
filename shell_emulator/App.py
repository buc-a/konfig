import tkinter as tk
import os
import zipfile

from Index import Index

__all__ = [
    "App",
]

class App:
    _ps1: str = "[{hostname} {_current_dir} ]$ "
    _command_input: tk.Text

    def __init__(self, hostname, path):
        self._hostname = hostname
        self._current_dir = '/'
        self._path = path

        self._window = tk.Tk()

        self._command_history = []
        self._history_index = 0

        self._index = Index(1,len(str(hostname)+str(self._current_dir))+2)

        self.configWindow()
        self._bindings()

    #начальная настройка окна
    def configWindow(self):
        self._window.title("Shell Emulator")
        self._command_input = tk.Text(master=self._window)
        self._command_input.insert(tk.END, f"{self._hostname}:{self._current_dir}$")

    def _bindings(self) -> None:
        def handle_keypress(event) -> None:
            if event.keysym == "Return":
                self._execute()

        self._window.bind("<Key>", handle_keypress)


    def _execute(self) -> None:
        cmd = self._command_input.get(self._index.to_str(), tk.END)[:-2]
        args = cmd.split()

        if args[0] == "ls":
            self._print(self.ls(args[1:]))
        elif args[0] == "cd":
            self._print(self.cd(args[1:]))
        elif args[0] == "exit":
            self.exit()
        elif args[0] == "cp":
            self.cp(args[1:])
        elif args[0] == "history":
            self._print(self.history())
        elif args[0] == "uniq":
            self.uniq(args[1:])
        else:
            self._print("Неизвестная команда\n")

        self._command_history.append(cmd)
        self._history_index = len(self._command_history)


        self._print(f"{self._hostname}:{self._current_dir}$")
        self._index.add_line(1)

    def _pack(self):
        self._command_input.pack()

    def run(self):
        self._pack()
        self._window.mainloop()


    def _print(self, str):
        self._command_input.insert(tk.END, str)

        if "\n" in str:
            self._index.add_line(str.count("\n") )



    def ls(self, args):
        if len(args) > 0:
            if args[0][0] == '/':
                path = args[0].strip('/')
            else:
                path = os.path.join(self._current_dir, args[0]).strip('/')

        else:
            path = self._current_dir.strip('/')


        result = ''
        with zipfile.ZipFile(self._path) as archive:

            list = set()
            for name in archive.namelist():
                print(name)
                if name.startswith(path):
                    if path == '':
                        ls_name = name
                    else:
                        ls_name = name[len(path) + 1:]


                    if '/' in ls_name:
                        ls_name = ls_name[:ls_name.index('/')]

                    list.add(ls_name)

            for name in list:
                result += name + '\n'
        return result

    def cd(self, args):
        if len(args) > 0:

            if args[0] == "/":
                self._current_dir = args[0]
                self._index.add_column(3 + len(self._hostname))
            elif args[0] == '..':
                if self._current_dir == '/':
                    return "Некорректное действие\n"

                else:
                    self._current_dir = os.path.dirname(self._current_dir)
                    self._index.add_column(2 + len(self._current_dir + self._hostname))
            else:
                if args[0][0]=='/':
                    path = os.path.join(args[0])

                else:
                    path = os.path.join(self._current_dir, args[0])

                if path[-1]!='/':
                    path+="/"
                path = path.strip('/')

                with zipfile.ZipFile(self._path) as zip_ref:

                    for name in zip_ref.namelist():
                        if name.startswith(path) and name[len(path)] == '/':
                            self._current_dir = path
                            self._index.add_column(2 + len(self._current_dir + self._hostname))
                            return ''

                return "Некорректный путь\n"
        return ''




    def cp(self, args):
        
        if len(args) < 2:
            self._print("Недостаточно аргументов\n")
            return

        if args[0][0] != '/':
            args[0] = os.path.join(self._current_dir, args[0])

        if args[1][0] != '/':
            args[1] = os.path.join(self._current_dir, args[1])

        source_path = args[0].lstrip('/')
        destination_path = args[1].lstrip('/')

        with (zipfile.ZipFile(self._path, 'r') as zip_read):
            fl = 0
            for names in zip_read.namelist():
                if names == source_path:
                    fl = 1
            if fl == 0:
                self._print(f'{source_path} - не существует такого файла\n')
                return

            with zip_read.open(source_path) as file:
                data = file.read()


        with zipfile.ZipFile(self._path, 'a') as zip_write:

            if destination_path[-1] == '/':
                destination_path = os.path.join(destination_path,os.path.basename(source_path))

            zip_write.writestr(destination_path, data)

    def history(self):
        result = ''
        if len(self._command_history) == 0:
            return "История команд пуста\n"

        for i, command in enumerate(self._command_history):
            result += f"{i + 1} {command}\n"

        return result

    def uniq(self, args):
        if len(args) == 0:
            self._print("Необходимо указать файл\n")
            return

        file_path = os.path.join(self._current_dir, args[0])[1:]

        with zipfile.ZipFile(self._path, 'r') as zip_ref:

            if file_path not in zip_ref.namelist():
                self._print(f"Файл {file_path} не найден\n")
                return

            uniq_lines = []
            with zip_ref.open(file_path, 'r') as file:
                lines = file.readlines()

                for line in lines:
                    line = line.rstrip(b'\r\n')
                    if line not in uniq_lines:
                        uniq_lines.append(line)


        for line in uniq_lines:
            self._print(line.decode('utf-8')+'\n')


    def exit(self):
        self._window.destroy()
        exit(0)


