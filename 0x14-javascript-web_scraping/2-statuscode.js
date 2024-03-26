#!/usr/bin/node

/**
 * Script that display the status code of a Get request
 * The first argument is the URL to request (GET)
 * The status code must be printed like this: code: <status code>
 * You must use the module request
 */

const request = require('request');

if (process.argv.length < 3) {
  console.log(`Usage: ./${process.argv[1]} <URL>`);
  process.exit(1);
}

const url = process.argv[2];

request(url, (err, response) => {
  if (err) {
    console.error('Error:', err.message);
    process.exit(1);
  }
  console.log('code:', response.statusCode);
});
