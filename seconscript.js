// Select all buttons
const buttons = document.querySelectorAll(".color-btn");

// Add event listener to each button
buttons.forEach(btn => {
    btn.addEventListener("click", () => {
        const color = btn.getAttribute("data-color");
        document.body.style.backgroundColor = color;
    });
});
