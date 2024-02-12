#!/usr/bin/node

const num = process.argv[2];

if (!num || Number.isNaN(parseInt(num, 10))) {
  console.log('Missing number of occurrences');
} else {
  const x = parseInt(num, 10);
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
