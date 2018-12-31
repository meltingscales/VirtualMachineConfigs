'use strict';

let list = [1, 2, 3, 4, 5]

function is_odd(number) {
    if (number % 2 === 1) {
        return true;
    } else {
        return false;
    }
}

console.log(list)
console.log(list.filter(is_odd))
