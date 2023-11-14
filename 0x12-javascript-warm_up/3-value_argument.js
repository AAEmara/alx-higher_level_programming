#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length === 2) {
  console.log('No argument');
} else {
  let i = 2;
  while (argv[i]) {
    console.log(argv[i]);
    i++;
  }
}
