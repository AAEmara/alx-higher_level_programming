#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const usersTodo = {};

request(url, (error, data, body) => {
  if (error) {
    console.log(error);
  }
  const objs = JSON.parse(body);
  for (let i = 0; i < objs.length; i++) {
    if (objs[i].completed === true) {
      if (usersTodo[objs[i].userId] === undefined) {
        usersTodo[objs[i].userId] = 0;
      }
      usersTodo[objs[i].userId]++;
    }
    if (i === objs.length - 1) {
      console.log(usersTodo);
    }
  }
});
