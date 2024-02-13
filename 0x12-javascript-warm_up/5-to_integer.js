#!/usr/bin/node
let a = process.argv[2];
let b = parseInt(a);
if (process.argv === 2 && Number.isInteger(b)) {
  console.log('My number:', b);
} else {
  console.log('Not a number');
}
