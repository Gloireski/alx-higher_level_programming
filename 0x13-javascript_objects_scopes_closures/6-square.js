#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) { super.print(); }
    let i = 0;
    while (i < this.height) {
      console.log('C'.repeat(this.width));
      i++;
    }
  }
}

module.exports = Square;
