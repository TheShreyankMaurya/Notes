# File I/O Operations

Python can be used for performing operations on a file.

## Reading a file

We have to open a file before reading or writing.

Flow - Open > Read > Close(If not using 'with').

Syntax :

```py
f = open("fileName","mode").
data = f.read()
f.close()
```

- read() : used for read the entire file.
- readline() : used to read one line at a time.

## Modes

There are different modes in which a file can be open.

| Character |                         Meaning                         |
| :-------: | :-----------------------------------------------------: |
|     r     |                open for reading(default)                |
|     w     |       open for writing, truncating the file first       |
|     x     |       creating a new file and open it for writing       |
|     a     | open file for writing and append to the end of the file |
|     b     |                       binary mode                       |
|     t     |                   text mode(default)                    |
|     +     |   open a disk file for updating(reading and writing)    |

## Writing to a file

In similar way, first we have to open the file for reading.

Flow - Open > Read > Close(If not using 'with').

Syntax :

```py
f = open("filename","mode")
f.write("text here")
f.close()
```

- if mode was "w", it will overwrite the entire file.
- if mode was "a", it will adds to the file.

## with Syntax

with is a reserved keyword used for file operations. We do not need to close the file if we use with.

Syntax :

```py
with open("filename","mode") as "variable":
    #operations
```

## Deleting a file

We need 'os' module to perform delete operation on any file.

Syntax :

```py
import os
os.remove("filename")
```
