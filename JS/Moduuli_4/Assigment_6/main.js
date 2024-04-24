'use strict';

const form = document.querySelector('#form');
const div = document.querySelector('div');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const value_from_input = document.querySelector('#query').value;
    try{
        const res = await fetch(`https://api.chucknorris.io/jokes/search?query=${value_from_input}`)
        const resjson = await res.json()
        div.innerHTML = '';
        resjson.result.forEach((item, index) => {
            const p = document.createElement('p');
            const article = document.createElement('article');
            p.style = `color: #${Math.floor(Math.random() * 16777215).toString(16)}`;
            p.textContent = item.value;
            article.appendChild(p);
            div.appendChild(article);

        })
    }
    catch (e) {
        console.error("ERROR -> " ,e.message);
    }
})