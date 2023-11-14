#!/usr/bin/node
const { argv } = require('node:process');
let i = 0;
while (argv[i]) {
  i++;
}
if (i === 2) {
  console.log('No Argument');
}
else {
  i = 2;
  while (argv[i]) {
    console.log(argv[i]);
    i++;
  }
}
