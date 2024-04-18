

const parent = document.querySelector('#target');
const array = ['First item', 'Second item', 'Third item'];


for (let i = 0; i < array.length; i++) {
    let li = document.createElement("li");
    li.innerHTML = array[i].toString();
    parent.appendChild(li);
}
