#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number
// matches a given integer
const request = require('request');
const url = 'http://swapi.co/api/films/';
const wedge = 'https://swapi.co/api/people/18/';

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    const data = JSON.parse(body).results;
    const length = data.length;
    for (let i = 0; i < length; i++) {
      if (data[i]['characters'].includes(wedge)) {
	count++;
      };
    }
    console.log(count);
  }
});
