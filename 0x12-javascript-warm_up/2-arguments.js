#!/usr/bin/node
const { argv } = require('node:process');
const arg_len = argv.length
if (arg_len === 2) {
  console.log('No argument');
} else if (arg_len === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
