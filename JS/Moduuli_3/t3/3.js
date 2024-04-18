"use strict";

const parent = document.querySelector('#target');
const array = ['John', 'Paul', 'Jones'];

for (let i = 0; i < array.length; i++) {
    let li = document.createElement("li").innerHTML = array[i].toString();
    parent.appendChild(li);
}
