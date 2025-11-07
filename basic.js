
// This code covers variables, data types, arithmetic, conditionals, loops, and functions.

// Variables and Data Types
let name = "Asmita";
let age = 21;
let isLearning = true;
let height = 5.2;

console.log("Name:", name);
console.log("Age:", age);
console.log("Learning JavaScript?", isLearning);
console.log("Height:", height, "ft");

// Arithmetic Operations
let a = 10;
let b = 3;

console.log("\nArithmetic Operations:");
console.log("Sum:", a + b);
console.log("Difference:", a - b);
console.log("Product:", a * b);
console.log("Quotient:", a / b);
console.log("Remainder:", a % b);

//Conditional Statements
if (age >= 18) {
  console.log("\nYou are an adult!");
} else {
  console.log("\nYou are still a teenager!");
}

//Functions
function greet(userName) {
  return `Hello, ${userName}! Welcome to JavaScript learning journey.`;
}

console.log("\n" + greet(name));

//Loops
console.log("\nCounting from 1 to 5:");
for (let i = 1; i <= 5; i++) {
  console.log(i);
}

// Arrays and Loops
let fruits = ["Apple", "Banana", "Mango"];
console.log("\nFruits list:");
for (let fruit of fruits) {
  console.log(fruit);
}

//Objects
let student = {
  name: "Asmita",
  course: "Computer Engineering",
  isActive: true
};

console.log("\nStudent Info:");
console.log(student);

// Function with Arithmetic Logic
function addNumbers(x, y) {
  return x + y;
}

console.log("\nSum using function:", addNumbers(5, 7));


