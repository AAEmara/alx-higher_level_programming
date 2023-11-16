#!/usr/bin/node
const Square2 = require('./5-square.js');
module.exports = class Square extends Square2 {
  constructor (size) {
    super(size, size);
    this.num = size;
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.num; i++) {
      console.log(c.repeat(this.num));
    }
  }
};
