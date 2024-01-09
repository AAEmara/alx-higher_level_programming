#!/usr/bin/node
const count = Number(process.argv[2]);
let square = '';

if (!count) {
  console.log('Missing size');
} else {
  for (let i = 0; i < count; i++) {
    for (let j = 0; j < count; j++) {
      square += 'X';
    }
    console.log(square);
    square = '';
  }
}
