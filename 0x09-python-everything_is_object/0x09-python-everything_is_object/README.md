# 0x09. Python - Everything is object

### [0. Who am I?](./0-answer.txt)
* What function would you use to print the type of an object?


### [1. Where are you?](./1-answer.txt)
* How do you get the variable identifier (which is the memory address in the CPython implementation)?


### [2. Right count](./2-answer.txt)
* In the following code, do a and b point to the same object?
Answer with Yes or No.
```
>>> a = 89
>>> b = 100
```


### [3. Right count =](./3-answer.txt)
* In the following code, do a and b point to the same object?
Answer with Yes or No.
```
>>> a = 89
>>> b = 89
```


### [4. Right count =](./4-answer.txt)
* In the following code, do a and b point to the same object?
Answer with Yes or No.
```
>>> a = 89
>>> b = a
```


### [5. Right count =+](./5-answer.txt)
* In the following code, do a and b point to the same object?
Answer with Yes or No.
```
>>> a = 89
>>> b = a + 1
```


### [6. Is equal](./6-answer.txt)
* What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```

### [7. Is the same](./7-answer.txt)
* What do these 3 lines print?
```
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```


### [8. Is really equal](./8-answer.txt)
* What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```


### [9. Is really the same](./9-answer.txt)
* What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```


### [10. And with a list, is it equal](./10-answer.txt)
* What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```


### [11. And with a list, is it the same](./11-answer.txt)
* What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```


### [12. And with a list, is it really equal](./12-answer.txt)
* What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```


### [13. And with a list, is it really the same](./13-answer.txt)
* What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```


### [14. List append](./14-answer.txt)
* What does this script print?
```
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```


### [15. List add](./15-answer.txt)
* What does this script print?
```
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```


### [16. Integer incrementation](./16-answer.txt)
* What does this script print?
```
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```


### [17. List incrementation](./17-answer.txt)
* What does this script print?
```
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```


### [18. List assignation](./18-answer.txt)
* What does this script print?
```
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```

### [19. Copy a list object](./19-copy_list.py)
* Write a function def copy_list(l): that returns a copy of a list.
```
guillaume@ubuntu:~/0x09$ ./19-main.py
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
True
False
guillaume@ubuntu:~/0x09$ wc -l 19-copy_list.py 
3 19-copy_list.py
guillaume@ubuntu:~/0x09$ 
```


### [20. Tuple or not?](./20-answer.txt)
Is `a` a tuple? Answer with `Yes` or `No`.
* a = ()


### [21. Tuple or not?](./21-answer.txt)
* a = (1, 2)



### [22. Tuple or not?](./22-answer.txt)
* a = (1)



### [23. Tuple or not?](./23-answer.txt)
* a = (1, )



### [24. Who I am?](./24-answer.txt)
* What does this script print?
```
a = (1)
b = (1)
a is b
```


### [25. Tuple or not](./25-answer.txt)
* What does this script print?
```
a = (1, 2)
b = (1, 2)
a is b
```

### [26. Empty is not empty](./26-answer.txt)
* What does this script print?
```
a = ()
b = ()
a is b
```

### [27. Still the same?](.27-answer.txt)
```
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```


### [28. Same or not?](./28-answer.txt)
```
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```


### [29. #pythonic](./100-magic_string.py)
* Write a function `magic_string()` that returns a string “BestSchool” n times the number of the iteration (see code):
```
guillaume@ubuntu:~/0x09$ ./100-main.py | cat -e
BestSchool$
BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
guillaume@ubuntu:~/0x09$ wc -l 100-magic_string.py 
4 100-magic_string.py
guillaume@ubuntu:~/0x09$
```


### [30. Low memory cost](./101-locked_class.py)
* Write a class `LockedClass` with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name.
```
guillaume@ubuntu:~/0x09$ ./101-main.py
[AttributeError] 'LockedClass' object has no attribute 'last_name'
guillaume@ubuntu:~/0x09$
```

### [31. int 1/3](./103-line1.txt)
```
julien@ubuntu:/python3$ cat int.py 
a = 1
b = 1
julien@ubuntu:/python3$ 
```
File: [`103-line1.txt`](./103-line1.txt), [`103-line2.txt`](./103-line2.txt)


### [32. int 2/3](./104-line1.txt)
```
julien@ubuntu:/python3$ cat int.py 
a = 1024
b = 1024
del a
del b
c = 1024
julien@ubuntu:/python3$ 
```
Assuming we are using a CPython implementation of Python3 with default options/configuration:

* How many int objects are created by the execution of the first line of the script? [104-line1.txt](./104-line1.txt)
* How many int objects are created by the execution of the second line of the script [104-line2.txt](./104-line2.txt)
* After the execution of line 3, is the int object pointed by a deleted? Answer with Yes or No [104-line3.txt](./104-line3.txt)
* After the execution of line 4, is the int object pointed by b deleted? Answer with Yes or No [104-line4.txt](./104-line4.txt)
* How many int objects are created by the execution of the last line of the script [104-line5.txt](./104-line5.txt)


### [34. int 3/3](./105-line1.txt)
```
julien@twix:/tmp/so$ cat int.py 
print("I")
print("Love")
print("Python")
julien@ubuntu:/tmp/so$ 
```
Assuming we are using a CPython implementation of Python3 with default options/configuration:

* Before the execution of line 2 (`print("Love")`), how many int objects have been created and are still in memory? (`105-line1.txt`)


34. [Clear strings](./106-line1.txt)
```
guillaume@ubuntu:/python3$ cat string.py 
a = "SCHL"
b = "SCHL"
del a
del b
c = "SCHL"
guillaume@ubuntu:/python3$ 
```
Assuming we are using a CPython implementation of Python3 with default options/configuration (For answers with numbers use integers, don’t spell out the word):

* How many string objects are created by the execution of the first line of the script? [106-line1.txt](./106-line1.txt)
* How many string objects are created by the execution of the second line of the script [106-line2.txt](./106-line2.txt)
* After the execution of line 3, is the string object pointed by a deleted? Answer with Yes or No [106-line3.txt](./106-line3.txt)
* After the execution of line 4, is the string object pointed by b deleted? Answer with Yes or No [106-line4.txt](./106-line4.txt)
* How many string objects are created by the execution of the last line of the script [106-line5.txt](./106-line5.txt)
