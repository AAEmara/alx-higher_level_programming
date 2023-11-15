#!/usr/bin/node
if (process.argv[2] === undefined || process.argv[3] === undefined) {
  console.log(0);
} else {
  let Num1 = parseInt(process.argv[2]);
  let Num2 = parseInt(process.argv[3]);
  let i = 3;
  while (parseInt(process.argv[i])) {
    if (process.argv[i] > Num1) {
      Num2 = Num1;
      Num1 = process.argv[i];
    } else if (process.argv[i] > Num2) {
      Num2 = process.argv[i];
    }
    i++;
  }
  console.log(Num2);
}
