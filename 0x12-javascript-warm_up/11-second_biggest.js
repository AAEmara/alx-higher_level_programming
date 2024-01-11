#!/usr/bin/node
let maxFirst;
let maxSecond;
const args = process.argv;
if (args.length < 3 || args.length === 3) {
  console.log(0);
} else {
  for (let i = 2; i < args.length; i++) {
    if (i === 2) {
      maxFirst = Number(args[i]);
      maxSecond = Number(args[i + 1]);
      continue;
    } else {
      if (Number(args[i]) > maxFirst) {
        const tmp = maxFirst;
        maxSecond = tmp;
        maxFirst = Number(args[i]);
      } else if (Number(args[i]) > maxSecond) {
        maxSecond = args[i];
      }
    }
  }
  console.log(maxSecond);
}
