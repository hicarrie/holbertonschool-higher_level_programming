#!/usr/bin/node
// concatenates two files
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (err, file) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(process.argv[4], file, 'utf8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});

fs.readFile(process.argv[3], 'utf8', function (err, file) {
  if (err) {
    console.log(err);
  } else {
    fs.appendFile(process.argv[4], file, function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
