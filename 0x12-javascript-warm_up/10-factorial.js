#!/usr/bin/node

function fact (a) {
  if (isNaN(a) || a === 0) {
    return 1;
  } else {
    return a * fact(a - 1);
  }
}

if (process.argv.length === 3) {
  const inputNumber = parseInt(process.argv[2]);
  console.log(fact(inputNumber));
}
