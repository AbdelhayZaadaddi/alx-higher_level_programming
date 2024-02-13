const { dict } = require('./101-data');

const newDict = {};

for (const userId in dict) {
  const occurrences = dict[userId];
  if (occurrences in newDict) {
    newDict[occurrences].push(userId);
  } else {
    newDict[occurrences] = [userId];
  }
}

console.log(newDict);
