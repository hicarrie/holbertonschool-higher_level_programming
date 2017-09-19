#!/usr/bin/node
// prints a square
const size = parseInt(process.argv[2]);
if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
