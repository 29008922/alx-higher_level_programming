#!/usr/bin/node

const myNumber = Math.floor(Number(process.argv[2]));
if (isNaN(myNumber)){
console.log('missing number of occurence');
}else {
 for (let i = 0; i < myNumber; i++) {
  console.log('C is fun');
 }
}
