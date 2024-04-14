'use strict';


let number_of_candidates = parseInt(prompt("Enter the number of candidates"));
let array = [];

const obj_constructor = (name) => {
    let doc = {
        name: name,
        votes: 0
    }
    array.push(doc);
}

function print_candidates() {
    return array.map((candidate) => {
        return candidate.name;
    })
}

function main(){
    for (let i = 0; i < number_of_candidates; i++) {
        let names = prompt(`Enter candidate ${i}`);
        obj_constructor(names);
    }

    let number_of_voters = parseInt(prompt("Enter the number of voters"));
    for (let i = 0; i < number_of_voters; i++) {
        let candidate_name = prompt(`
            Candidates -> ${print_candidates()} 
            Enter candidate name: 
        `);
        array.forEach((candidate) => {
            if (candidate.name === candidate_name) {
                candidate.votes += 1;
            }
        })
    }
    array.sort((a, b) => a - b);
    console.log(`The winner is ${array[0].name} with ${array[0].votes}.`);
    console.log('Results: ');
    array.forEach((candidate) => {
        console.log(`${candidate.name}: ${candidate.votes} votes`);
    });
}




main();


