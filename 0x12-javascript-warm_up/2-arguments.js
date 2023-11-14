#!/usr/bin/node

const x = process.argv.length;
console.log( x === 2 ? 'No argument': x === 3 ? 'Argument found' : 'Argument found');
