#!/usr/bin/node
const args = process.argv;
const Arg1 = parseInt(args[2]);
const Arg2 = parseInt(args[3]);
exports.add = function add (a, b) {
  const sum = parseInt(a) + parseInt(b);
  return (sum);
}
