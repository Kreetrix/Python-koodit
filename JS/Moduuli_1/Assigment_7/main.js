 'use strict';

let rolls = parseInt(prompt("Insert your name"));


const roll = () => {
    let sum = 0;
    for (let i = 0; i < rolls; i++) {
         sum += Math.floor(Math.random() * 6);
    }
    return `Sum of rolls -> ${sum}`;
}


document.querySelector('#target').innerHTML = roll();
