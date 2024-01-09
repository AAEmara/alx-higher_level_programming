#!/usr/bin/node
const number = Number(process.argv[2]);

function factorial (num) {
  if (num === 0 || num === 1) {
    return (1);
  }
  return (num * factorial(num - 1));
}

if (!number) {
  console.log(1);
} else {
  console.log(factorial(number));
}
