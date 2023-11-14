#!/usr/bin/node
const args = process.argv;
let i = 0;
while (args[i]) {
  i++;
}
if (i === 2) {
  console.log('No Argument');
} else {
  i = 2;
  while (args[i]) {
    console.log(args[i]);
    i++;
  }
}
