## 1
```jsonnet
local groups = [
  "ИКБО-1-20",
  "ИКБО-2-20",
  "ИКБО-3-20",
  "ИКБО-4-20",
  "ИКБО-5-20",
  "ИКБО-6-20",
  "ИКБО-7-20",
  "ИКБО-8-20",
  "ИКБО-9-20",
  "ИКБО-10-20",
  "ИКБО-11-20",
  "ИКБО-12-20",
  "ИКБО-13-20",
  "ИКБО-14-20",
  "ИКБО-15-20",
  "ИКБО-16-20",
  "ИКБО-17-20",
  "ИКБО-18-20",
  "ИКБО-19-20",
  "ИКБО-20-20",
  "ИКБО-21-20",
  "ИКБО-22-20",
  "ИКБО-23-20",
  "ИКБО-24-20"
];

local students = [
  {
    "age": 19,
    "group": "ИКБО-4-20",
    "name": "Иванов И.И."
  },
  {
    "age": 18,
    "group": "ИКБО-5-20",
    "name": "Петров П.П."
  },
  {
    "age": 18,
    "group": "ИКБО-5-20",
    "name": "Сидоров С.С."
  },
 {
    "age": 18,
    "group": "ИКБО-10-23",
    "name": "Буц А.Е."
  },
];

{
  "groups": groups,
  "students": students,
  "subject": "Конфигурационное управление"
}
```
<image src="https://github.com/user-attachments/assets/65e2352d-3286-48ce-8615-c16413e954ec">
  
## 2
```dhall
let groups = [
  "ИКБО-1-20",
  "ИКБО-2-20",
  "ИКБО-3-20",
  "ИКБО-4-20",
  "ИКБО-5-20",
  "ИКБО-6-20",
  "ИКБО-7-20",
  "ИКБО-8-20",
  "ИКБО-9-20",
  "ИКБО-10-20",
  "ИКБО-11-20",
  "ИКБО-12-20",
  "ИКБО-13-20",
  "ИКБО-14-20",
  "ИКБО-15-20",
  "ИКБО-16-20",
  "ИКБО-17-20",
  "ИКБО-18-20",
  "ИКБО-19-20",
  "ИКБО-20-20",
  "ИКБО-21-20",
  "ИКБО-22-20",
  "ИКБО-23-20",
  "ИКБО-24-20"
]
let Student = { age : Natural , group : Text, name : Text }

let students
	: List Student
  = [ { age = 19, group = "ИКБО-4-20", name = "Иванов И.И."}
  , { age = 18, group = "ИКБО-5-20", name = "Петров П.П."}
  , { age = 18, group = "ИКБО-5-20", name = "Сидоров С.С."}
  , { age = 20, group = "ИКБО-1-20", name = "Васильев В.В."}
  , { age = 18, group = "ИКБО-10-20", name = "Буц А.Е."}
	]

let subject = "Конфигурационное управление"

in {
  groups = groups,
  students = students,
  subject = subject
}
```
<image src=https://github.com/user-attachments/assets/a03e357d-2f1d-4a88-994d-78dd6f218677>
<image src=https://github.com/user-attachments/assets/856f1934-6326-4a18-aff9-058884a05a55>
<image src=https://github.com/user-attachments/assets/fce7665b-a370-4c4c-98df-107921c0a6a3>
<image src=https://github.com/user-attachments/assets/f371f9bb-45e0-4d62-a4ec-01bcc58b71ed>

## 3
```python
BNF = '''
E = 0 E | 1 E | 0 | 1
'''
```
<image src=https://github.com/user-attachments/assets/da9b5860-d864-46f1-b13a-a6915034d876>

## 4
```python
BNF = '''
E = [ ] | { } | [ E ] | { E }
'''
```
<image src=https://github.com/user-attachments/assets/2559fe37-dadf-4b20-ab87-3f016e1b51f5>

## 5
```python
BNF = '''
E = x | y | E & E | E V E | ~ E | ( E )
'''
```
<image src=https://github.com/user-attachments/assets/e3a19951-2edd-4f26-a27c-5301d586cb66>






