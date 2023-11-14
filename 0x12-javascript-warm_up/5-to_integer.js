#!/usr/bin/node
const number_1 = Math.floor(Number(process.argv[2]));
console.log(isNaN(number_1) ? 'Not a number' : `My number: ${number_1}`);
