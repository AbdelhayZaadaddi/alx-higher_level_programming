#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let conut = 0;
  for (let element of list) {
    if (element === searchElement) {
      conut++;
    }
  }
  return conut;
};
