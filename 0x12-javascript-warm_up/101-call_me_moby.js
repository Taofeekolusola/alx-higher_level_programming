#!/usr/bin/node
const callMeMoby = (x, func) => {
  for (let i = 0; i < x; i++) {
    func();
  }
};

module.exports = { callMeMoby };
