#!/usr/bin/node
// class that defines a square and inherits from Rectangle
const Rectangle = require('./4-rectangle').Rectangle;

function Square (size) {
  Rectangle.call(this, size, size);
}

module.exports.Square = Square;
