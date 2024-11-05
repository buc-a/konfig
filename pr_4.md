## Задание 1
```bash
git commit
git branch first
git branch second
git commit
git commit
git checkout first
git commit
git commit
git checkout master
git merge first
git checkout second
git commit
git commit
git rebase master
git checkout master
git merge second
git checkout 368c81f
```

<image src="https://github.com/user-attachments/assets/d93efa87-98cd-46c2-9fc7-c64466d07bbb">

## Задание 2
<image src="https://github.com/user-attachments/assets/796f8461-80a9-409a-8d13-ebbb6a7207cf">

## Задание 3
>Cоздадим bare-репозиторий, загрузим туда содержимое локального репозитория, созданного в предыдущем задании
<image src="https://github.com/user-attachments/assets/2655e8f9-c245-4011-8f7a-f556df27505d">

>Склонируем репозиторий в новую папку, от имени пользователя coder2 добавим файл readme.md, отправим изменения на сервер
<image src="https://github.com/user-attachments/assets/187dbfb7-8aff-448f-b1e2-c841232682fc">
<image src="https://github.com/user-attachments/assets/2c59b391-a873-4444-a988-eccf0cd218a1">

>Обновим данные у пользователя Coder1, внесем измененения в readme.md, отправим изменения на удаленный репозиторий
<image src="https://github.com/user-attachments/assets/95fadd24-1233-4031-a67b-6fa88b962be2">
<image src="https://github.com/user-attachments/assets/ca018c40-2422-496d-8fc1-be3a715d7844">

>Обновим данные у пользователя Coder2, внесем измененения в readme.md, отправим изменения на удаленный репозиторий
<image src="https://github.com/user-attachments/assets/273f9bd4-178f-45de-8425-eb98ad9751d6">
<image src="https://github.com/user-attachments/assets/9c55b739-e842-42e1-a79c-607692358300">

## Задание 4
```python
from os import listdir
from subprocess import call

if __name__ == '__main__':
    path = ".git/objects"
    lst = listdir(path)
    for dr in lst:

        if dr != 'info' and dr != 'pack':
            sum = listdir(f'{path}/{dr}')[0]
            file = dr + sum
            print(sum)
            call(['git', 'cat-file', '-p', file])
            print()
```
<image src="https://github.com/user-attachments/assets/018df202-9383-4b6c-a377-0225399c7ca7">




