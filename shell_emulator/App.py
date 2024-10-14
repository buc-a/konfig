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

        if ( len(args) > 0):
            if args[0] == "ls":
                self._print(self.ls(args[1:]))
            elif args[0] == "cd":
                self._print(self.cd(args[1:]))
            elif args[0] == "exit":
                self.exit()
            elif args[0] == "cp":
                self._print(self.cp(args[1:]))
            elif args[0] == "history":
                self._print(self.history())
            elif args[0] == "uniq":
                self._print(self.uniq(args[1:]))
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

    def isDir(self, str_path) :
        with zipfile.ZipFile(self._path, 'a') as zip_write:
            if str_path[-1] == '/':
                return 1
            else:
                fl = 0
                for name in zip_write.namelist():
                    if name.startswith(str_path):
                        fl = 1
                        if len(name) > len(str_path) and name[len(str_path)]=='/':
                            return 1
                if fl == 0:
                    return -1

        return 0


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
                        if name.startswith(path) and len(name) > len(path) and name[len(path)] == '/':
                            self._current_dir = path
                            self._index.add_column(2 + len(self._current_dir + self._hostname))
                            return ''

                    return "Некорректный путь\n"
        return ''




    def cp(self, args):
        
        if len(args) < 2:
            return "Недостаточно аргументов\n"

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
                return (f'{source_path} - не существует такого файла\n')

            with zip_read.open(source_path) as file:
                data = file.read()


        with zipfile.ZipFile(self._path, 'a') as zip_write:
            if self.isDir(destination_path) == 1:
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
            return "Необходимо указать файл\n"

        file_path = os.path.join(self._current_dir, args[0]).lstrip('/')

        with zipfile.ZipFile(self._path, 'r') as zip_ref:
            if file_path not in zip_ref.namelist():
                return f"Файл {file_path} не найден\n"

            uniq_lines = []
            with zip_ref.open(file_path, 'r') as file:
                lines = file.readlines()

                for line in lines:
                    line = line.rstrip(b'\r\n')
                    if line not in uniq_lines:
                        uniq_lines.append(line)

        result = ''
        for line in uniq_lines:
            result += line.decode('utf-8')+'\n'

        return result


    def exit(self):
        self._window.destroy()
        exit(0)


