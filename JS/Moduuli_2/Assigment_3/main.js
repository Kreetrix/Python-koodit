
let array = [];

for (let i = 0; i < 6; i++) {
    let names = prompt(`Enter the name of a dog`);
    array.push(names);
}

array.sort().reverse();
for (let i = 0; i < array.length; i++) {
    let block = document.createElement("UL");
    block.innerHTML = array[i].toString();
    document.body.appendChild(block);
}