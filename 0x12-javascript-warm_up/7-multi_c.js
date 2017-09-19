#!/usr/bin/node
// prints 'C is fun' x times
const number = parseInt(process.argv[2]);
if (Number.isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
}
