#!/usr/bin/node

const request = require('request');
const idUrl = process.argv[2];
let count = 0;

request(idUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const data = JSON.parse(body);
  const dataResults = data.results;
  let charactersTotal = 0;

  for (let i = 0; i < dataResults.length; i++) {
    charactersTotal = dataResults[i].characters.length;
    for (let j = 0; j < charactersTotal; j++) {
      if (dataResults[i].characters[j].endsWith('18/')) {
        count++;
      }
      if (i === (dataResults.length - 1) && j === (charactersTotal - 1)) {
        console.log(count);
      }
    }
  }
});
