#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number
// matches a given integer
const request = require('request');
const url = process.argv[2];
const wedge = 'https://swapi.co/api/people/18/';

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body).results;
    const length = data.length;
    let count = 0;
    for (let i = 0; i < length; i++) {
      if (data[i]['characters'].includes(wedge)) {
        count++;
      }
    }
    console.log(count);
  }
});
