#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const str = process.argv[3];
fs.writeFile(filePath, str, error => {
  if (error) console.log(error);
});
