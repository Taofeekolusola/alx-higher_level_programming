#!/usr/bin/node
const x = process.argv[2];
let i = 0;
while (i < x) {
  console.log('C is fun');
  i++;
}
if (!parseInt(x)) {
  console.log('Missing number of occurrences');
}
