#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];

try {
const content = fs.readFileSync(filePath, 'utf8');
console.log(`The content of the file ${filePath} is:`);
console.log(content);
} catch (error) {
console.error(`Error reading file ${filePath}:`, error);
}
