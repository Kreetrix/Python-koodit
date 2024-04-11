 'use strict';

let value = parseInt(prompt("Enter a number"));


const prime_num_calc = () => {
    let sus = value % (1 && value) === 0;
    for (let i = 2; i < value; i++) {
        if (value !== i && value % i === 0) {
            return 'Luku ei ole alkuluku';
        }
    }
    if (sus) {
        return 'Luku on alkuluku';
    }
}

document.querySelector('#target').innerHTML = prime_num_calc();

