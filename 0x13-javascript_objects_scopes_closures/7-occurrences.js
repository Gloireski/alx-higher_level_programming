#!/usr/bin/node

exports.nbOccurences = (list, searchElement) => {
  let c = 0;
  list.forEach((el) => {
    if (el === searchElement) { c++; }
  });
  return c;
};
