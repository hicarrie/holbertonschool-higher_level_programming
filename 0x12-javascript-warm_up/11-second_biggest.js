#!/usr/bin/node
// searches for the second biggest integer in the list of arguments
const list = process.argv;
list.splice(0, 2);
const length = list.length;
let largest = 0;
let nextLargest = 0;

if (length === 2 || length === 3) {
  console.log('0');
} else {
  for (let i = 0; i < length; i++) {
    if (list[i] > nextLargest) {
      if (list[i] > largest) {
        nextLargest = largest;
        largest = list[i];
      } else {
        nextLargest = list[i];
      }
    }
  }
}
console.log(nextLargest);
