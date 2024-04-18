

let elem = document.getElementById("calculation");
let p = document.getElementById('result');
function calc() {
    let value = elem.value;
    value = value.split(" ");
    let numbers = value.filter(Number);
    p.innerHTML = math(value, parseInt(numbers[0]), parseInt(numbers[1]));
}

function math(value, x, y) {
    if (value.includes('+')) return x + y;
    else if (value.includes('-')) return x - y;
    else if (value.includes('*')) return x * y;
    else if (value.includes('/')) return x / y;
}