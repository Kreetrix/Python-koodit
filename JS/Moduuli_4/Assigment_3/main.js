'use strict';

const form = document.querySelector('#form');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const value_from_input = document.querySelector('#query').value;

    try{
        const res = await fetch(`https://api.tvmaze.com/search/shows?q=${value_from_input}`)
        const resjson = await res.json()
        const p = document.querySelector('#p');
        p.innerHTML = '';
        resjson.forEach((item, index) => {
            const h2 = document.createElement('h2');
            const a = document.createElement('a');
            a.target = '_blank';
            const img = document.createElement('img');
            const div = document.createElement('div');
            div.id = 'results';
            const article = document.createElement('article');

            const show = item.show;

            div.innerHTML = show.summary;
            h2.textContent = show.name;
            a.href = show.url;
            img.src = show.image?.medium;
            img.alt = index;
            a.appendChild(img);
            article.appendChild(h2);
            article.appendChild(a);
            article.appendChild(div);
            p.appendChild(article);
        });
    }
    catch (e) {
        console.error("ERROR -> " ,e.message);
    }
})