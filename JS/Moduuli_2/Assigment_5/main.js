
let array = [];

while (true) {
    let number = parseInt(prompt(`Enter numbers`));
    if (array.includes(number)) {
        break
    }
    array.push(number);
}

array.sort((a, b) => a - b);
for (let i = 0; i < array.length; i++) {
    console.log(array[i]);
}