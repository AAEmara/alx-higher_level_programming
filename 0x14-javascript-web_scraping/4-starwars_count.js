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
  for (let i = 0; i < dataResults.length; i++) {
    for (let j = 0; j < dataResults[i].characters.length; j++) {
      request(dataResults[i].characters[j], (error, response, body) => {
        if (error) {
          console.log(error);
          return;
        }
        let characterData = JSON.parse(body);
        let characterName = characterData.name
        console.log(characterName);
        if (characterName === "Wedge Antilles") {
          count ++;
        }
      });
    }
  }
});
console.log(count);
