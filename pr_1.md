##1
```bash
cut -d: -f1 passwd | sort
```
<image src="https://github.com/user-attachments/assets/d9eea1ba-353d-4025-a4f9-334e2f2b80c8">

##2
```bash
$ sort -rnk2 /etc/protocols | head -5 | awk '{print $2,$1}`
```
<image src="https://github.com/user-attachments/assets/4dfcdaba-b567-4fd2-9d3d-93035c785983">

##3
```bash
#!/bin/bash
str=$1
echo -n '+-'
for((i=0; i<${#str}; i++))
do
echo -n '-'
done

echo '-+'
echo "| $1 |"
echo -n '+-'
for((i=0; i<${#str}; i++))
do
echo -n '-'
done

echo '-+'
```
<image src="https://github.com/user-attachments/assets/d684ea46-d96d-4aa3-9de7-72b732940d86">

##4
```bash
#!/bin/bash
grep -o "[a-zA-Z_][a-zA-Z0-9]*" "$1" | sort -u
```
<image src="https://github.com/user-attachments/assets/1142f093-c32e-48ba-be29-dc7f58ba6a19">

##5
```bash
!/bin/bash
chmod +x "$1"
sudo cp "$1" /usr/local/bin
```
<image src=https://github.com/user-attachments/assets/4c725572-3ca8-4d7c-a3d6-b443f083b544>

##6
```bash
#!/bin/bash
for file in *.c *.js *.py
do
str=$(head -n 1 $file)
if [[ "$str" == *"#"* || "$str" == *"//"* ]]
then 
echo "файл $file содержит комментарий строке $str"
else
echo "файл $file не содержит комментарий в первой строке"
fi
done
```
<image src="https://github.com/user-attachments/assets/b02034d1-5ca7-4335-9a47-f90661d38e7f">

##7
```bash
#!/bin/bash
#files -  каталог для временного хранения файлов
#заполняем его
for file in "$1"/*
do
if [ -f "$file" ]; then
cp "$file" files
elif [ -d "$file" ]; then
for file_2 in "$file"/*
do
if [ -f "$file_2" ]; then
cp "$file_2" files
fi
done
fi
done
find files -type f -exec md5sum {} + | sort | uniq -d --check-chars=32 | awk '{print $2}' | sed 's#.*/##'
#очищаем каталог
rm -f files/*
```
<image src="https://github.com/user-attachments/assets/b8f30268-d9ed-4bb3-9676-91bc02a7c8b7">

##8
```bash
#!/bin/bash
#здесь нужно ввести имя создаваемого архива
name=$1
tar cf $name *.$2
```
<image src="https://github.com/user-attachments/assets/7316d57f-46a9-4b5b-a67d-130d36c72415">

##9
```bash
#!/bin/bash
cat $1 > $2 | sed "s/    /\t/g"
```
<image src="https://github.com/user-attachments/assets/a95a945b-ac01-4ee7-8ea8-0aa45b00a1ed">

##10
```bash
#!/bin/bash
for file in "$1"/*
do
if [ -f "$file" ]
then
        if [ ! -s "$file" ]
        then
        echo "$file"
        fi
fi
done
```
<image src="https://github.com/user-attachments/assets/5660eec9-c210-4bdc-8d06-2ef1f00f8137">
