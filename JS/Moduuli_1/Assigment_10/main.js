 'use strict';

let dice_num = parseInt(prompt("Enter the number of dice"));
let eye_sum= parseInt(prompt("Enter the number of dice"));

const dice = [1, 2, 3, 4, 5, 6];

function calc() {
    let count = 0;
    let success = 0;
    for (let i = 0; i < 10000; i++) {
        count++;
        let res = 0;
        for (let i = 0; i < dice_num; i++) {
            res += dice[Math.floor(dice.length * Math.random())];
        }
        if (res === eye_sum){
            success++;
        }
        let probability = Number(success / count).toLocaleString(undefined,{style: 'percent', minimumFractionDigits:2})
        document.querySelector('#target').innerHTML = `Probability to get sum ${eye_sum} with ${dice_num} dice is ${probability}`;
    }
}
calc()

