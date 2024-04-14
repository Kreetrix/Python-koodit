'use strict';

function roll () {
    return Math.floor(Math.floor((Math.random() * 6) + 1));
}


function main () {
    const parent = document.querySelector("#ul");
    while (true) {
        const dice_roll = roll();
        console.log("roll -> ", dice_roll);
        let li = document.createElement("li");
        li.innerHTML = dice_roll.toString();
        parent.appendChild(li);
        if (dice_roll === 6){
            break;
        }
    }
}

main();