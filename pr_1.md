##1
```bash
cut -d: -f1 passwd | sort
```

##2
```bash
$ sort -rnk2 /etc/protocols | head -5 | awk '{print $2,$1}`
```

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
##5
```bash
!/bin/bash
chmod +x "$1"
sudo cp "$1" /usr/local/bin
```
##6
```bash
#!/bin/bash
for file in *.c *.js *.py
do
str=$(head -n 1 $file)
if [[ "$str" == *"#"* || "$str" == *"//"* ]]
then 
echo "файл $file содержит комментарий в первой строке"
else
echo "файл $file не содержит комментарий в первой строке"
fi
done
```

##8
```bash
#!/bin/bash
#здесь нужно ввести имя создаваемого архива
name=$1
tar cf $name *.$2
```
##9
```bash
#!/bin/bash
cat $1 > $2 | sed "s/    /\t/g"
```
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
