#!/usr/bin/node
// gets the contents of a webpage and stores it in a file
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const path = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(path, body, 'utf8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
