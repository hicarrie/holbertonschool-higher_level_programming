#!/usr/bin/node
// prints the addition of 2 integers
function add (a, b) {
  const sum = a + b;
  console.log(sum);
}

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
add(a, b);
