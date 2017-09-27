#!/usr/bin/node
// returns the reversed version of a list without using reverse built-in
exports.esrever = function (list) {
  let length = list.length - 1;
  for (let i = 0; i < length; i++, length--) {
    let swap = list[i];
    list[i] = list[length];
    list[length] = swap;
  }
  return list;
};
