#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
fs.readFile(filePath, 'utf8', function (error, content) {
  console.log(error || content);
});
