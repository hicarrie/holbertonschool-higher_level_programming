#!/usr/bin/node
// class that defines a rectangle
function Rectangle (w, h) {
  if (w > 0 && h > 0) {
    this.width = w;
    this.height = h;
  }
  this.print = function () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      console.log();
    }
  };
  this.rotate = function () {
    let temp = this.width;
    this.width = this.height;
    this.height = temp;
  };
  this.double = function () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  };
}

module.exports.Rectangle = Rectangle;
