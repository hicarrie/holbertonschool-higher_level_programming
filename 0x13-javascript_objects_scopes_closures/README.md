# 0x13. Javascript - Objects, Scopes and Closures
## Project Requirements
### Javascript Scripts
- First line of all files should be `#!/usr/bin/node`
- Code should be `semistandard` compliant (version 11.0.0)

## File Descriptions
**0-rectangle.js:** an empty class `Rectangle` that defines a rectangle
- Must use the `function` notation for defining your class

**1-rectangle.js:** a class `Rectangle` that defines a rectangle
- Must use the `function` notation for defining your class
- The constructor must take 2 arguments `w` and `h`
- Initialize the instance attribute `width` with the value of `w`
- Initialize the instance attribute `height` with the value of `h`

**2-rectangle.js:** a class `Rectangle` that defines a rectangle
- Must use the `function` notation for defining your class
- The constructor must take 2 arguments `w` and `h`
- Initialize the instance attribute `width` with the value of `w`
- Initialize the instance attribute `height` with the value of `h`
- If `w` or `h` is equal to 0 or not a positive integer, create an empty object

**3-rectangle.js:** a class `Rectangle` that defines a rectangle
- Must use the `function` notation for defining your class
- The constructor must take 2 arguments `w` and `h`
- Initialize the instance attribute `width` with the value of `w`
- Initialize the instance attribute `height` with the value of `h`
- If `w` or `h` is equal to 0 or not a positive integer, create an empty object
- Create an instance method called `print()` that prints the rectangle using the character `X`

**4-rectangle.js:** a class `Rectangle` that defines a rectangle
- Must use the `function` notation for defining your class
- The constructor must take 2 arguments `w` and `h`
- Initialize the instance attribute `width` with the value of `w`
- Initialize the instance attribute `height` with the value of `h`
- If `w` or `h` is equal to 0 or not a positive integer, create an empty object
- Create an instance method called `print()` that prints the rectangle using the character `X`
- Create an instance method called `rotate()` that exchanges the `width` and the `height` of the rectangle
- Create an instance method called `double()` that multiples the `width` and the `height` of the rectangle by 2

**5-square.js:** a class `Square` that defines a square and inherits from `Square` of `5-square.js`
- You must use the `prototype` notation for adding a new method
- Create an instance method called `charPrint(c)` that prints the rectangle using the character `c`
 - If `c` is `undefined`, use the character `X`

**6-square.js:** a class `Square` that defines a square and inherits from `Rectangle` of `4-rectangle.js`

**7-occurrences.js:** a function that returns the number of occurrences in a list
- Prototype: `exports.nbOccurences = function (list, search_element)`

**8-esrever.js:** a function that returns the reversed version of a list:
- Prototype: `exports.esrever = function (list)`
- You are not allow to use the build-in method `reverse`

**9-logme.js:** a function that prints the number of argument already printed and the new argument value
- Prototype: `exports.logMe = function (item)`
- Output format: `<number arguments already printed>: <current argument value>`

**10-converter.js:** a function that converts a number from base 10 to another base passed as argument
- Prototype: `exports.converter = function (base)`
- You are not allowed to import any file
- You are not allowed to declare any new variable (`var`, `let`, etc..)

**100-map.js:** a script that imports an array and computes a new array
- Script must import list from the file `100-data.js`
- Must use a `map`
- A new list must be created with each value equal to the value of the initial list, multipled by the index in the list
- Print both the initial list and the new list

## Author
*Carrie Ybay* - [Twitter](http://twitter.com/hicarrie_)