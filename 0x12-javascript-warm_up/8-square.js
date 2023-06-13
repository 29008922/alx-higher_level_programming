#!/usr/bin/node
const num  = process.argv[2];

if (!parseInt(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let num2 = 0;
    let myVar = '';

    while (num2 < num) {
      myVar = myVar + 'num';
      num2++;
    }
    console.log(myVar);
  }
}
