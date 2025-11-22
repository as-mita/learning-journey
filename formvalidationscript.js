const form = document.getElementById("signupForm");
const nameInput = document.getElementById("name");
const emailInput = document.getElementById("email");
const passwordInput = document.getElementById("password");
const successMessage = document.getElementById("successMessage");

form.addEventListener("submit", function (e) {
    e.preventDefault();

    let valid = true;

    // Name validation
    if (nameInput.value.trim() === "") {
        setError(nameInput, "Name is required");
        valid = false;
    } else {
        setSuccess(nameInput);
    }

    // Email validation
    if (emailInput.value.trim() === "") {
        setError(emailInput, "Email is required");
        valid = false;
    } else if (!emailInput.value.includes("@")) {
        setError(emailInput, "Invalid email format");
        valid = false;
    } else {
        setSuccess(emailInput);
    }

    // Password validation
    if (passwordInput.value.length < 6) {
        setError(passwordInput, "Password must be at least 6 characters");
        valid = false;
    } else {
        setSuccess(passwordInput);
    }

    // If all fields valid
    if (valid) {
        successMessage.textContent = "Account Created Successfully!";
        form.reset();
    }
});

// Helper functions
function setError(input, message) {
    const parent = input.parentElement;
    parent.querySelector(".error").textContent = message;
    input.style.borderColor = "red";
}

function setSuccess(input) {
    const parent = input.parentElement;
    parent.querySelector(".error").textContent = "";
    input.style.borderColor = "green";
}
