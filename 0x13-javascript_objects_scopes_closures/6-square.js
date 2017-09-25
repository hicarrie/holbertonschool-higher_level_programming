#!/usr/bin/node
// class that defines a square and inherits from Square
const Square = require('./5-square').Square;

Square.prototype = Object.create(Square.prototype);
Square.prototype.constructor = Square;
Square.prototype.charPrint = function (c = 'X') {
  for (let i = 0; i < this.height; i++) {
    for (let j = 0; j < this.width; j++) {
      process.stdout.write(c);
    }
    console.log();
  }
};

module.exports.Square = Square;
