#!/usr/bin/node

const a = parseInt(process.argv[2]);
const squareLen = a;
let i;
let j;
for (i = 0; i < squareLen; i++) {
  let row = '';
  for (j = 0; j < squareLen; j++) {
    row += 'x';
  }
  console.log(row);
}
if (isNaN(a)) {
  console.log('Missing size');
}
