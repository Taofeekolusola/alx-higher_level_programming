#!/usr/bin/node
function isAlphabetic(value) {
  return isNaN(value) && /^[a-zA-Z]+$/.test(value);
}

let a = process.argv[2];
if (process.argv.length < 2) {
  console.log('Not a number');
} else if (isAlphabetic(a)) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(a));
}
