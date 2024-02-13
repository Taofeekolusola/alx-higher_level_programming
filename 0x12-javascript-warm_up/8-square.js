#!/usr/bin/node
const x = process.argv[2];
const squareLen = x;
let i;
let j;
for (i = 0; i < squareLen; i++) {
  let row = '';
  for (j = 0; j < squareLen; j++) {
    row += 'x';
  }
  console.log(row);
}
if (!parseInt(x)) {
  console.log('Missing size');
}
