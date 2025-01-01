console.log(`hello ok`, `hey`);

const multiline_message = `This is a template string without any variable injection. 
It can span multiple lines 
easily.`;

console.log(multiline_message);

const name = "Alice";
const age = 25;
const city = "Paris";

// Using template strings
const injection_message = `Hello, my name is ${name}. I am ${age} years old and I live in ${city}.`;

console.log(injection_message);
