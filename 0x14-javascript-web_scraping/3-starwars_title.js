#!/usr/bin/node

const request = require('request');
const episodeNumber = process.argv[2].toString();
const idUrl = 'https://swapi-api.alx-tools.com/api/films/' + episodeNumber;

request(idUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
