# python-utils-list

Python list 增强

## 1. 增加foreach()方法

```python
l = UtilsList()
l.append(1)
l.append(2)
l.append(3)
l.foreach(print)
```

```
1
2
3
```

## 2. 增加map()方法

```python
l = UtilsList()
l.append(1)
l.append(2)
l.append(3)
new_list = l.map(lambda x: x ** 2)
print(new_list)
```

```
[1,4,9]
```