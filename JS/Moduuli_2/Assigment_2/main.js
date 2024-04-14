
let participants = parseInt(prompt(`Enter the number of participants`));
let array = [];

for (let i = 0; i < participants; i++) {
    let names = prompt(`Enter names`);
    array.push(names);
}

array.sort();
for (let i = 0; i < array.length; i++) {
    let block = document.createElement("OL");
    block.innerHTML = array[i].toString();
    document.body.appendChild(block);
}