

let e = document.getElementById('operation');
let value = e.value;

function option() {
    value = e.value;
}
function calc() {
    let num1 = parseInt(document.getElementById('num1').value);
    let num2 = parseInt(document.getElementById('num2').value);
    let res = document.getElementById('result');
    switch (value) {
        case 'add':
            res.innerHTML = num1 + num2;
            break;
        case 'sub':
            res.innerHTML = num1 - num2;
            break;
        case 'multi':
            res.innerHTML = num1 * num2;
            break;
        case 'div':
            res.innerHTML = num1 / num2;
            break;
        default:
            res.innerHTML = 'bruh';
            break;
    }
}
e.onchange = option;
option();
