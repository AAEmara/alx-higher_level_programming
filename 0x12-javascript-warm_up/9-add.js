#!/usr/bin/node
const args = process.argv;
const Arg1 = parseInt(args[2]);
const Arg2 = parseInt(args[3]);
function add (a, b) {
  const sum = parseInt(a) + parseInt(b);
  console.log(sum);
}
add(Arg1, Arg2);
