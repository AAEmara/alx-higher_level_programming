#!/usr/bin/node
const num = parseInt(process.argv[2]);
function factorial (FactNum) {
  if (FactNum === 1 || isNaN(FactNum)) {
    return (1);
  }
  const result = FactNum * factorial(FactNum - 1);
  return (result);
}
console.log(factorial(num));
