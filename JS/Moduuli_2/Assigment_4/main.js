
let array = [];

while (true) {
    let number = parseInt(prompt(`Enter numbers`));
    if (number === 0) {
        break
    }
    array.push(number);
}

array.sort((a, b) => b - a);
for (let i = 0; i < array.length; i++) {
    console.log(array[i]);
}