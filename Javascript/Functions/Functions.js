// Functions

// Basic Function

function greet() {
    console.log("Hello");
}

greet();

// Function with arguments

function greet(name) {
    console.log(`Hello ${name}`);
}

greet("Shreyank");

// Return Function

function sum(a, b) {
    return a + b;
}

let result = sum(4, 5);
console.log(result);

// Function expression

const greet = function (name) {
    console.log(`Hello ${name}`);
};

greet("Shreyank");

// Arrow Function

const greet = (name) => {
    console.log(`Hello ${name}`);
};

greet("Shreyank");
