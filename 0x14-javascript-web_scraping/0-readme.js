#!/usr/bin/node
/*
 * read the content of a file
 * print the content of the file
 * pint an error if the file does not exist
 */

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  } else {
    console.log(data);
  }
});
