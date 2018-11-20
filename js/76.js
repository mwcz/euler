#!/usr/bin/env node

//  It is possible to write five as a sum in exactly six different ways:

//  4 + 1
//  3 + 2
//  3 + 1 + 1
//  2 + 2 + 1
//  2 + 1 + 1 + 1
//  1 + 1 + 1 + 1 + 1

//  How many different ways can one hundred be written as a sum of at least two positive integers?

const arrayEqual = (a1, a2) => {
    for(var i = 0; i < a1.length; ++i) {
        if (a1[i] !== a2[i]) return false;
    }
    return true;
};

const Ways = n => {
    const solns = [];
    let array = new Array(n).fill(1);
    solns.push(array);

    ways(solns, array);

    solns.sort();

    for(var i = 0; i < solns.length - 1; ++i) {
        if (arrayEqual(solns[i], solns[i+1])) {
            solns.splice(i, 1);
            i--;
        }
    }

    console.log(`\n--- ${n} sums ${solns.length} ways ---`);
    // console.log(solns.join('\n'));
    return solns.length;
};

const ways = (solns, array) => {
    if (array.length == 2) return;
    // make copies of the array
    const a1 = array.slice(0,array.length);
    const a2 = array.slice(0,array.length);
    const onepos = array.indexOf(1); // leftmost 1
    if (onepos > 0) {
        // add the leftmost one into the number to the left of it
        a1[onepos-1]++;
        a1.splice(onepos, 1);
        solns.push(a1);
        a1.sort().reverse();
        ways(solns, a1);

    }
    if (a2[onepos] === 1 && a2[onepos+1] === 1) {
        // add the two leftmost ones
        a2[onepos]++;
        a2.splice(onepos+1, 1);
        solns.push(a2);
        a2.sort().reverse();
        ways(solns, a2);
    }
};


var n = 20;
while(n >= 2) {
    Ways(n);
    n--;
}
