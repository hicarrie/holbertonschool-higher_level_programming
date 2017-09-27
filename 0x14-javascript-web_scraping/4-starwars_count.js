#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number
// matches a given integer
const request = require('request');
const url = process.argv[2];
const wedge = '18';

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body).results;
    let count = 0;
    for (let film of data) {
      for (let character of film['characters']) {
        if (character.includes(wedge)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
