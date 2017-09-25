#!/usr/bin/node
// class that defines a rectangle
function Rectangle (w, h) {
  if (w > 0 && h > 0) {
    this.width = w;
    this.height = h;
  }
  this.print = function () {
    for (let i = 0; i < h; i++) {
      for (let j = 0; j < w; j++) {
        process.stdout.write('X');
      }
      console.log();
    }
  };
}

module.exports.Rectangle = Rectangle;
