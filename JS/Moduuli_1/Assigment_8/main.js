 'use strict';

let start = parseInt(prompt("Enter the start year"));
let end = parseInt(prompt("Enter the end year"));


const parent = document.querySelector("#ul");

const roll = () => {
    const years = end - start;
    console.log(years)
    for (let i = 0; i <= years; i++) {
        let li = document.createElement("li");
        li.innerHTML = (start + i).toString();
        parent.appendChild(li);
    }
}
roll();