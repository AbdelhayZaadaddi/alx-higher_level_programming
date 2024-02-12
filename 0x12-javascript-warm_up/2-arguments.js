#!/usr/bin/node
const argv = process.argv.length;

if (argv > 2) {
  console.log('Argument' + (argv > 3 ? 's' : '') + ' found');
} else {
  console.log('No argument');
}
