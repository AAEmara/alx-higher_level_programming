#!/usr/bin/node

const request = require('request');
const idUrl = 'https://swapi-api.alx-tools.com/api/films/';
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
      request(dataResults[i].characters[j], (error, response, body) => {
        if (error) {
          console.log(error);
          return;
        }
        const characterData = JSON.parse(body);
        const characterName = characterData.name;
        if (characterName === 'Wedge Antilles') {
          count++;
        }
        if (i === (dataResults.length - 1) && j === (charactersTotal - 1)) {
          console.log(count);
        }
      });
    }
  }
});
