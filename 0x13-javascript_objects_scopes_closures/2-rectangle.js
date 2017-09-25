#!/usr/bin/node
// class that defines a rectangle
function Rectangle (w, h) {
  if (w > 0 && h > 0) {
    this.width = w;
    this.height = h;
  }
}

module.exports.Rectangle = Rectangle;
