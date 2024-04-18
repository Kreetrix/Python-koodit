

let element = document.getElementById('trigger');
element.onmouseover = function () {
    document.getElementById('target').src = 'img/picB.jpg';
}
element.onmouseleave = function () {
    document.getElementById('target').src = 'img/picA.jpg';
}