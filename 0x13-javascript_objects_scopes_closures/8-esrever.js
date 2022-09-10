#!/usr/bin/node

exports.esrever = function (list) {
  const arrayLength = list.length;
  const reverseArray = [];

  for (let index = arrayLength - 1; index >= 0; index--) {
    reverseArray.push(list[index]);
  }
  return (reverseArray);
};
