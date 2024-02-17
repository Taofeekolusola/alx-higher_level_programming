#!/usr/bin/node
exports.esrever = function (list) {
  const reversedList = list.sort((a, b) => b - a);
  return reversedList;
};
