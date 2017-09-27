#!/usr/bin/node
// imports an array and computes a new array
const list = require('./100-data').list;

const factors = list.map(function (x, i) {
  return x * i;
});

console.log(list);
console.log(factors);
