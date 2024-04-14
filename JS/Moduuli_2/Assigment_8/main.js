'use strict';

const array = ['Johnny', 'DeeDee', 'Joey','Marky'];

function concat(array) {
    let concatted = '';
    for (let i = 0; i < array.length; i++) {
        concatted = concatted + array[i];
    }
    console.log(concatted);
    let block = document.createElement("P");
    block.innerHTML = concatted;
    document.body.appendChild(block);
}

concat(array);