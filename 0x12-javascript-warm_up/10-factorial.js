#!/usr/bin/node

function factorial (n) {
  if (isNaN(parseInt(n))) {
    return 1;
  } else if (parseInt(n) < 0) {
    return Infinity;
  } else if (parseInt(n) === 0 || parseInt(n) === 1) {
    return 1;
  } else {
    return parseInt(n) * factorial(parseInt(n) - 1);
  }
}

const num = process.argv[2];
console.log(factorial(num));
