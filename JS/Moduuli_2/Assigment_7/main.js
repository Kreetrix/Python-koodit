'use strict';

function roll (dice_sides) {
    return Math.floor(Math.floor((Math.random() * dice_sides) + 1));
}


function main () {
    const parent = document.querySelector("#ul");
    let dice_sides = parseInt(prompt("Enter number of dice sides"));
    while (true) {
        const dice_roll = roll(dice_sides);
        console.log("roll -> ", dice_roll);
        let li = document.createElement("li");
        li.innerHTML = dice_roll.toString();
        parent.appendChild(li);
        if (dice_roll === dice_sides){
            break;
        }
    }
}

main();