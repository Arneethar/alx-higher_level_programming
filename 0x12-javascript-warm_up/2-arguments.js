#!/usr/bin/node
const count = process.argv.length - 1;
if (count === 1) {
  console.log('No argument');
} else if (count === 2) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
