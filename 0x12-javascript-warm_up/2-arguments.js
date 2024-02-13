#!/usr/bin/node
const arglen = process.argv.length;
const argslen = arglen - 2;

if (argslen === 0) {
  console.log('No argument');
} else if (argslen === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
