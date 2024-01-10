#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }
  print() {
    var i = 0;
    while (i < this.h) {
    console.log('hi');
    console.log('X'.repeat(this.w));
    i++;
    }
  }
}

module.exports = Rectangle;
