#!/usr/bin/node

/**
 * Script that prints the title of a Star Wars movie where the episode number matches a given integer.
 * The first argument is the movie ID
 * You must use the Star wars API with the endpoint https://swapi-api.alx-tools.com/api/films/:id
 * You must use the module request
 */

const request = require('request');

if (process.argv.length < 3) {
  console.log(`Usage: ./${process.argv[1]} <ID>`);
  process.exit(1);
}

const id = process.argv[2];

request.get(`https://swapi-api.alx-tools.com/api/films/${id}`, (err, response, body) => {
  if (err) {
    console.error('Error:', err.message);
    process.exit(1);
  }
  console.log(JSON.parse(body).title);
});
