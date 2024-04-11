
'use strict';


const answer = confirm("Should I calculate the square root?");

const sqrt = () => {
    if(answer){
        const number = parseInt(prompt("Insert number"));
        if(number < 0) {
            return "The square root of a negative number is not defined";
        }
        const root = Math.sqrt(number);
        return `Square root -> ${root}`;
    }
    return `Bruh`;
}

document.querySelector('#target').innerHTML = sqrt();