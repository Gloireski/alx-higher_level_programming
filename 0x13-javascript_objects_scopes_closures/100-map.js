#!/usr/bin/node

const list = require('./100-data').list;
const newList = [];
list.map((ind, el) => newList.push(el * ind));
console.log(list);
console.log(newList);
