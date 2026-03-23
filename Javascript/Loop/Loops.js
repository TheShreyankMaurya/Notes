// Loops

// for loop
for (let i = 1; i <= 10; i++) {
    console.log(i);
}

// while
let i = 1;
while (i <= 10) {
    console.log(i);
    i += 1;
}

// for of
let fruits = ["apple", "banana", "cherry", "dragon fruit"];
for (fruit of fruits) {
    console.log(fruit);
}

// nested loops
for (let i = 1; i <= 10; i++) {
    console.log(`Outer Loop counter ${i}`);
    for (let j = 10; j <= 12; j++) {
        console.log(`   Inner Loop counter ${j}`);
    }
}
