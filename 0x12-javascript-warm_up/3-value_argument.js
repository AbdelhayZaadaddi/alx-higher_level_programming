#!/usr/bin/node

if (process.argv.legth > 2) {
    for (let i = 1; i < process.argv.length; i++) {
        console.log(process.argv[i]);
    }
} else {
    console.log('No argument');
}
