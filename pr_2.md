##1
```bash
apt show python3-matplotlib
```

##2
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
