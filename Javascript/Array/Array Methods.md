# Array Methods

Array : Linear collections of things.

Arrays are mutable means it can be change the original array.

Common Syntax for methods : arrName.methodName().

## Methods

- push : add element to the end.

- pop : remove element from the end.

- unshift : add element to the start.

- shift : remove element from the start.

- indexOf : return index of the element.

- includes : search for a value and return true or false on the basis of the value found.

- concat : merge two arrays together.

- reverse : reverse an array.

- slice(start,end) : copies a portion of an array.
    - (start,end) : end is exclusive.

    - (start) : goes till end.

    - (-ve) : same as indexing.

    - () : return a copy.

- splice(start, deleteCount, item1, ... , item2) : use to add, replace or remove an element. This made changes to original array.
    - (start, deleteCount) : start from starting index and remove no of elements(deleteCount).
    - (start, deleteCount, item1, item2) : start from starting index and remove element and add element at that place.

- sort : use to sort an array.
