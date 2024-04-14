'use strict';

const array = [1, 5, 2, 67, 3, 77, 102];

function even(num_array) {
    return num_array.filter(num => {
        return num % 2 === 0;
    })
}
console.log(`New array: `);
console.log(even(array));
console.log(`Original array: `);
console.log(array);