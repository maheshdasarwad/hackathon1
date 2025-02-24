document.getElementById("login-toggle").addEventListener("click", function () {
    document.getElementById("login-form").classList.remove("hidden");
    document.getElementById("register-form").classList.add("hidden");
    this.classList.add("active");
    document.getElementById("register-toggle").classList.remove("active");
});

document.getElementById("register-toggle").addEventListener("click", function () {
    document.getElementById("register-form").classList.remove("hidden");
    document.getElementById("login-form").classList.add("hidden");
    this.classList.add("active");
    document.getElementById("login-toggle").classList.remove("active");
});

// Redirect to another page on login (optional)
document.getElementById("login-btn").addEventListener("click", function () {
    window.location.href = "/index/index.html"; // Change to your main page
});
