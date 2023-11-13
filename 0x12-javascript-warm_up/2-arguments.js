#!/usr/bin/node

const number = process.argv.len;
console.log(number === 2 ? 'No argument': number === 3 ? 'Argument found' : 'Argument found');
