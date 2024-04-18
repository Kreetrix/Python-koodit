'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

const parent = document.querySelector('#target');

students.forEach(student => {
  let option = document.createElement("option", `${student.id}`);
  option.innerHTML = student.name;
  parent.appendChild(option);
})
