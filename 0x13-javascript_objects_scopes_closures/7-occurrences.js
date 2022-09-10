#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurrence = 0;
  for (let index = 0; index < list.length; index++) {
    if (searchElement === list[index]) {
      occurrence = occurrence + 1;
    }
  }
  return (occurrence);
};
