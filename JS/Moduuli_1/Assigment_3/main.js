'use strict';

let number_1 = parseInt(prompt("Write a number"));
let number_2 = parseInt(prompt("Write a second number"));
let number_3 = parseInt(prompt("Write a third number"));

const sum = number_1 + number_2 +number_3;
const product = number_1 * number_2 * number_3;
const average = sum / 3;

document.querySelector('#target').innerHTML = `sum -> ${sum} product -> ${product} average -> ${average}`;
