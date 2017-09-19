#!/usr/bin/node
// prints 'My number: __' if the first arg can be converted to int
let number = parseInt(process.argv[2]);
if (Number.isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
