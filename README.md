# Month Checker

Check if a month lies between other two months.

## Problem

```
Does April lie between February and July? (Yes)
2 <= 4 <= 7; result is True/Yes.
This solution can work but will fail in cases like:
Does February lie between November and May? (Yes)
11 <= 2 <= 7; result is False/No,
which is mathematically/logically correct but not according to our requirement.
So, we need a solution that can return the correct answer. 
```

## Usage

There are two different modules to handle this problem with different techniques. Based on:
* Circular Doubly Linked List
```
python3 cdll_mc.py
```

* Date Object
```
python3 date_mc.py
```