#!/usr/bin/node

const size = process.argv[2];

if (!size || isNaN(size)) {
  console.log('Missing size');
} else {
  const squareSize = parseInt(size, 10);
  if (squareSize > 0) {
    for (let i = 0; i < squareSize; i++) {
      let row = '';
      for (let j = 0; j < squareSize; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}
