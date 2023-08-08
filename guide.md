# Guide

This file details all conventions and specifics of how to write code for the project. It is important to follow these 
conventions to ensure that the code is consistent and easy to read.

## Table of Contents


## General

### Naming Conventions

The following naming conventions should be followed when writing code for the project.

#### Variables

Variables should be named using `camelCase` and should be descriptive of what they are used for. For example, a variable
that stores the name of a person should be named `personName`.

#### Functions

Functions should be named using `camelCase` and should be descriptive of what they do. For example, a function that
prints a person's name should be named `printPersonName`.

#### Classes

Classes should be named using `PascalCase` and should be descriptive of what they are used for. For example, a class
that stores a person's name should be named `PersonName`.

#### Files

Files should be named using `kebab-case` and should be descriptive of what they are used for. For example, a file that
stores a person's name should be named `person-name.py`.

### Comments

Comments should be used to explain what a block of code does. Comments should be used sparingly and only when necessary.
Comments should be written in English and should be written in full sentences. Comments should be written in the
following format:

```python
# This is a comment.
```

### Imports

Imports should be written on separate lines and should be grouped in the following order:

1. Standard library imports
2. Third-party imports
3. Local application imports

Whole module imports should never be used. For example, the following is incorrect:

```python
from os import *
```
or 
```python
import os
```

Instead of importing the whole module, only import the specific functions or classes that are needed. For example, the
following is correct:

```python
from os import path
```

### Line Length

There is no limit to the length of a line. However, lines should be kept to a reasonable length to ensure that they are
easy to read. For example, a large `if` statement should be split at logical points to ensure good readability.

### Indentation

Indentation should be done using 4 spaces. Tabs should never be used for indentation.

### Whitespace

Whitespace should be used to improve readability. For example, the following is incorrect:

```python
if x==5:
```

Instead, the following is correct:

```python
if x == 5:
```

### Paths 

File paths should be written using \\ and be wrapped in a `Path` object from `pathlib` to ensure cross-platform
compatibility. For example, the following is incorrect:

```python
file = open("C:/Users/John/Documents/file.txt")
```

Instead, the following is correct:

```python
from pathlib import Path

file = open(Path("C:\\Users\\John\\Documents\\file.txt"))
```

Exceptions to this rule must be justified in the code review.

### Type Hints

Type hints should be used to indicate the type of a variable, function parameter, or function return value. Type hints
should be used for all variables, function parameters, and function return values. For example, the following is
incorrect:

```python
def add(x, y):
    return x + y
```

Instead, the following is correct:

```python
def add(x: int, y: int) -> int:
    return x + y
```

Type hints should be as specific as possible, except when recursion is involved (see below). Compatability with older 
versions of python is not needed, so using compatability layers in the `typing` library is not needed. For example, 
the following is incorrect:

```python
def add(x: int, y: int) -> int:
    return x + y
```

Instead, the following is correct:

```python
def add(x: int | float, y: int | float) -> int | float:
    return x + y
```
