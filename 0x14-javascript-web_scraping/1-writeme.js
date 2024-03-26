#!/usr/bin/node

/**
 * Script that writes a string to a file
 * the first argument is the string to write
 * the content of the file in utf-8
 * if an error occurred during writing, print the error object
 */

const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf8', (err) => {
  if (err) { console.log(err); }
});
