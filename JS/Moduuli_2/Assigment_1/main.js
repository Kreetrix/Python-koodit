
let num_array = [];
for (let i = 1; i <= 5; i++) {
    let number = parseInt(prompt(`Enter number ${i}`));
    num_array.push(number);
}

for (let i = num_array.length - 1; i >= 0; i--) {
    console.log(num_array[i]);
}
