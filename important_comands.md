# Ver el código SQL que ejecuta python con django

```bash
python managa.py sqlmigrate members 0001
```

## Agregar valores en una tabla vacia

```bash 
python manage.py shell
```

- Estando dentro de shell ejeuctaremos lo siguiente:

```shell
from members.models import Member
```

```shell
Members.objects.all()
```

- Agregar un registo a la tabla, ejecutando estas dos lineas: 

```shell
member = Member(firstname = 'Victor Hugo', lastname='Martinez Gonzales')
member.save()
```

- Ejecuta para ver la tabla guardo algo

```shel
Member.objects.all().values()
```

## Agregar múltiples registros 

```shell
>>> member1 = Member(firstname='Tobias', lastname='Refsnes')
>>> member2 = Member(firstname='Linus', lastname='Refsnes')
>>> member3 = Member(firstname='Lene', lastname='Refsnes')
>>> member4 = Member(firstname='Stale', lastname='Refsnes')
>>> member5 = Member(firstname='Jane', lastname='Doe')
>>> members_list = [member1, member2, member3, member4, member5]
>>> for x in members_list:
>>>   x.save()
```

- Ver los miembros 

```shell
Member.objects.all().values()
```



## Actualizar un registro 

```shell
from members.models import Member
x = Member.objects.all()[4]
```

- **X** ahora representará al miembro en el índice 4, que es "Hugo", pero para esetar seguros, veamos si eso es correcto: 

```shell
x.firstname
```

- Cambiar su valor y guardarlo


```shell
x.firstname = 'Mich'
x.save()
```

## Eliminar un registro 

```bash 
x = Member.obejects.all()[1]
x.detelte()



