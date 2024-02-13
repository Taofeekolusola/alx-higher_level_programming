#!/usr/bin/node
const a = process.argv[2];
const b = process.argv[3];
if (process.argv.length > 3) {
  console.log(a + ' is ' + b);
} else if (process.argv.length > 2) {
  console.log(a + ' is ' + 'undefined');
} else {
  console.log('undefined' + ' is ' + 'undefined');
}
