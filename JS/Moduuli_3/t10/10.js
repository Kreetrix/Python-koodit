
const form = document.querySelector('#source');
const p = document.querySelector('#target');
const f_name = document.querySelector('input[name=firstname]');
const l_name = document.querySelector('input[name=lastname]');

form.addEventListener('submit', (e) => {
    e.preventDefault();
    p.innerHTML = `Your name is ${f_name.value} ${l_name.value}`;
})