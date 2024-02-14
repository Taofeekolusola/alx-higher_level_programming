#!/usr/bin/node
const args = process.argv.slice(2);
const numbers = args.map(arg => parseInt(arg));
const validNumbers = numbers.filter(num => !isNaN(num));

if (validNumbers.length >= 2) {
  const sortedNumbers = validNumbers.sort((a, b) => b - a);
  const secondHighestNumber = sortedNumbers[1];
  console.log(secondHighestNumber);
} else if (validNumbers.length === 1) {
  console.log(0);
} else {
  console.log(0);
}
