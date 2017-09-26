#!/usr/bin/node
// computes the number of tasks completed by user id
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const length = data.length;
    let count_dict = {}
    for (let i = 1; i <= 10; i++) { // loop through every userId
      let count = 0;
      for (let j = 0; j < length; j++) { // loop through every todo item
    	if (data[j].userId === i && data[j].completed === true) {
    	  count++;
    	}
      }
      count_dict[i] = count;
    }
    console.log(count_dict);
  }
});
