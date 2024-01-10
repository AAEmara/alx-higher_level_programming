#!/usr/bin/node
exports.esrever = function (list) {
  let j = list.length;
  const count = Math.floor(j / 2);
  for (let i = 0; i < count; i++) {
    j--;
    const tmp = list[j];
    list[j] = list[i];
    list[i] = tmp;
  }
  return list;
};
