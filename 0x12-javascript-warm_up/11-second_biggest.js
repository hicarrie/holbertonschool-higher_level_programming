#!/usr/bin/node
// searches for the second biggest integer in the list of arguments
const list = process.argv
list.splice(0, 2);
const length = list.length;
let largest = 0;
let next_largest = 0;

if (length === 2 || length === 3) {
  console.log('0');
} else {
  for (let i = 0; i < length; i++) {
    if (list[i] > next_largest) {
      if (list[i] > largest) {
	next_largest = largest;
	largest = list[i];
      }
      else {
	next_largest = list[i];
      }
    }
  }
}
console.log(next_largest);
