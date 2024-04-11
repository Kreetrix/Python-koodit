'use strict';

let name = prompt("Insert your name");
const array = ['Gryffindor', 'Slytherin', 'Hufflepuff', 'Ravenclaw'];
const draw = () => {
    const random_class = array[Math.floor(Math.random() * array.length)]
    return `${name}, you are ${random_class}`;
}


document.querySelector('#target').innerHTML = draw();
