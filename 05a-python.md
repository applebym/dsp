# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Python lists and tuples are different in the following
ways: their syntax (lists have brackets while tuples have 
parentheses), lists are mutable while tuples are immutable.

>>The two are similar in the following ways: you can refer
to each individual element by using an index, you can use the 
slice operator on both, both can handle multiple types in the 
same list/tuple.

>>The keys of a dictionary must be hashable, which also
requires them to be immutable. Thus keys of a dictionary can 
be tuples but not lists.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Python sets are unordered and do not contain any of the
sequence functions (element positions, order of insertion, 
slicing, indexing, etc.) that a list contains, which are 
ordered. Sets also must contain unique elements while lists 
can contain repeats. Sets cannot contain mutable data types, 
while lists can, unless you implement an ImmutableSet. Some 
similarities are that they both can use the length function, 
"in" function, < function and > function. However, sets have 
some added functions, including union, intersection, and 
difference. In terms of finding an element, sets are faster 
than lists. However, if you are iterating over the entire 
contents, then lists are faster. The reason for this is that 
sets are implemented using hash tables, whcih means that when 
testing for membership, the size of the set does not matter 
(O(1)) vs. in a list where the size of the list does matter 
(O(n)).

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python's `lambda` is a one-line, simple, anonymous function 
that is used in place of calling a seperate function, helping 
to simplify code. It is also refered to as a nested function 
and can refer to variables within its scope. It frequently 
comes in handy when using the map(), filter(), and reduce() 
functions or sorting functions. Below are three examples:

>> An example of using lamda to simplify code: 
>> `f = lambda x: x * 2 + 10`
>> `f(4)`
>> 18

>> An example of using lambda with filter(): 
>> `a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
>> `b = filter(lambda x: x % 2 == 0, a)`
>> `print b`
>> [2, 4, 6, 8, 10]

>> An example of using lambda with sorted(): 
>> `a = [('John',12),('Mary',13),('Alex',10),('Melanie',8)]`
>> `b = sorted(a, key=lambda x: x[1])`
>> `print b`
>> [('Melanie', 8), ('Alex', 10), ('John', 12), ('Mary', 13)]

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehension is a simple and fast way to create a list. 
>> For example, you can create a list of square numbers by writing `squares = [x**2 for x in range(1,10)]`. Using `map()` this would look like: `squares = map(lambda x: x**2, range(1,10))`. 
>> Another example could be finding only upper case words in a string `sentence = "The Metis Data Science program is located in New York City"` by writing `upper = [word for word in sentence.split() if word[0].isupper()]`. Using the `filter()` function would look like this: `upper = filter(lambda x: x[0].isupper(), sentence.split())`.
>> This can apply to sets as well: `a = {x for x in 'Alexander' if x in 'Alexandria'}`
>> Or a dictionary: `word = "Mississippi"` `{x:word.count(x) for x in list(word)}` 

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





