'use strict';

const form = document.querySelector('#form');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const value_from_input = document.querySelector('#query').value;
    try{
        const res = await fetch(`https://api.tvmaze.com/search/shows?q=${value_from_input}`)
        const resjson = await res.json()
        console.log(resjson);
    }
    catch (e) {
        console.error("ERROR",e.message);
    }
})
