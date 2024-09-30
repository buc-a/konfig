## 1
```bash
apt show python3-matplotlib
```
<image src="https://github.com/user-attachments/assets/6024e619-ce15-496c-95b4-80e87fcd021c">

Получение пакета из репозитория

```bash
git clone https://github.com/matplotlib/matplotlib.git
cd matplotlib
pip install .      
```

## 2
```bash
npm show express
```

<image src="https://github.com/user-attachments/assets/4cd95b3f-587b-4b48-ad5e-8544ed73fab6">

Получение пакета из репозитория
```bash
git clone https://github.com/expressjs/express.git
cd express
npm install
```
## 3
### для matplotlib
Формирование dot файла 
```bash
echo "$(pipdeptree -p matplotlib --graph-output dot)" > matplot_deps.dot
```
<image src="https://github.com/user-attachments/assets/0ac6d7f4-5b7a-437a-9cac-21eeee158a73">

формирование png файла 
```bash
dot -Tpng matplot_deps.dot -o matplot_deps.png
```
<image src="https://github.com/user-attachments/assets/dee8bab5-6d2e-4aea-b947-eebe15259373">

### для express
Формирование dot файла 
```bash
npm ls -a --json | jq '{name: .name, dependencies: {express: .dependencies.express}}' | npm2dot > expresso_deps.dot
```
<image src="https://github.com/user-attachments/assets/9402a1f3-d20c-4b07-852e-abf1f673637a">

формирование png файла 
```bash
dot -Tpng expresso_deps.dot -o expresso_deps.png
```
<image src="https://github.com/user-attachments/assets/dc51809a-3ea3-4b58-9602-8d89aefc8c92">


## 4
```bash
include "alldifferent.mzn";

var 0..9: one; 
var 0..9: two;
var 0..9: three;
var 0..9: four;
var 0..9: five;
var 0..9: six;

constraint (one + two + three) == (four + five + six);

constraint all_different([one, two, three, four, five, six]);

solve minimize( 100000*one + 10000*two + 1000*three + 100*four + 10*five + six);

output [ show(one),show(two),show(three),show(four),show(five), show(six) ];
```
<image src="https://github.com/user-attachments/assets/197e6985-649e-4daa-bb77-8383483dc91f">

## 5
```bash
int: k_menu = 6; %кол-во различных версий menu
int: k_dropdowm = 5; %кол-во различных версий dropdown
int: k_icons = 2;%кол-во различных версий icons 

%вид записи версии
type type_version = var tuple(int,int,int);

%перечисление версий
array[1..k_menu] of type_version: v_menu = [(1,0,0),(1,1,0),(1,2,0),(1,3,0),(1,4,0),(1,5,0)];

array[1..k_dropdowm] of type_version: v_dropdowm = [(1,8,0),(2,0,0),(2,1,0),(2,2,0),(2,3,0)];

array[1..k_icons] of type_version: v_icons = [(1,0,0),(2,0,0)];

%какую версию из массива выбрать
var 1..k_menu: number_menu;
var 1..k_dropdowm: number_dropdowm;
var 1..k_icons: number_icons;

%перечисление условий

%зависимости root
constraint (v_menu[number_menu] == (1,0,0) \/ v_menu[number_menu] == (1, 5, 0) /\ v_icons[number_icons] == (1, 0, 0));

%зависимости menu
constraint (v_menu[number_menu].2 >= 1 /\ v_menu[number_menu].2 <= 5) -> (v_dropdowm[number_dropdowm] == (2, 3, 0) \/ v_dropdowm[number_dropdowm] == (2, 0, 0));

constraint v_menu[number_menu] == (1, 0, 0) -> v_dropdowm[number_dropdowm] == (1, 8, 0);

%зависимости dropdown
constraint (v_dropdowm[number_dropdowm].2 >= 0 /\ v_dropdowm[number_dropdowm].2 <= 3) -> v_icons[number_icons] == (2, 0, 0);

solve satisfy;

output ["version menu: ",show(v_menu[number_menu]),"\n",
        "version dropdown: ",show(v_dropdowm[number_dropdowm]),"\n",
        "version icons: ",show(v_icons[number_icons]),"\n"];
```
## 6
```bash
int: k_foo = 2; 
int: k_target = 2; 
int: k_left = 1;
int: k_right = 1; 
int: k_shared = 2; 


%вид записи версии
type type_version = var tuple(int,int,int);

%перечисление версий
array[1..k_foo ] of type_version: v_foo = [(1,0,0),(1,1,0)];
array[1..k_target] of type_version: v_target = [(1,0,0),(2,0,0)];
array[1..k_left] of type_version: v_left = [(1,0,0)];
array[1..k_right] of type_version: v_right = [(1,0,0)];
array[1..k_shared] of type_version: v_shared = [(1,0,0),(2,0,0)];

%какую версию из массива выбрать
var 1..k_foo: n_foo;
var 1..k_target: n_target;
var 1..k_left: n_left;
var 1..k_right: n_right;
var 1..k_shared: n_shared;

%перечисление условий

%зависимости root
constraint ( v_target[n_target].1 >= 2 /\ v_target[n_target].1<3 );
constraint ( v_foo[n_foo].1>=1 \/ v_foo[n_foo].1<2);

%зависимости foo 
constraint (v_foo[n_foo] == (1,1,0)) -> ( (v_left[n_left].1>=1 /\ v_left[n_left].1<2) \/ (v_right[n_right].1>=1 /\ v_right[n_right].1<2));

%зависимости left 
constraint ( v_left[n_left]==(1,0,0) ) -> ( v_shared[n_shared].1 >= 1 );

%зависимости right
constraint ( v_right[n_right]==(1,0,0) ) -> ( v_shared[n_shared].1 < 2);

%зависимости shared
constraint ( v_shared[n_shared]==(1,0,0) ) -> ( v_target[n_target].1 < 2 /\ v_target[n_target].1 >= 1);

solve maximize v_foo[n_foo].2;

output ["version target: ",show(v_target [n_target]),"\n",
        "version foo: ",show(v_foo[n_foo]),"\n",
        "version left: ",show(v_left[n_left]),"\n",
        "version right: ",show(v_right[n_right]),"\n",
        "version sharget: ",show(v_target[n_target]),"\n"];
```
<image src="https://github.com/user-attachments/assets/b802d0bb-c1a9-41e3-b250-00e396f37cde">
