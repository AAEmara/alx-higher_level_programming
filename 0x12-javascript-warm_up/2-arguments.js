#!/usr/bin/node
const ArgLen = process.argv.length - 2;
if (ArgLen === 0) {
  console.log('No argument');
} else if (ArgLen === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
