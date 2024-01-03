#!/usr/bin/node
const y = require('y');
y.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
