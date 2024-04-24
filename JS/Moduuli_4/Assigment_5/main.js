'use strict';

const button = document.querySelector('#button');
const p = document.querySelector('p');

button.addEventListener('click', async (e) => {
    try{
        const res = await fetch(`https://api.chucknorris.io/jokes/random`)
        const resjson = await res.json()
        console.log(resjson)
        p.textContent = resjson.value
    }
    catch (e) {
        console.error("ERROR -> " ,e.message);
    }
})