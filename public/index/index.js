
document.getElementById("manageCrops").addEventListener("click", function() { // Crop Management
    window.location.href = "/crop/crop.html";
  });

document.getElementById("viewTasks").addEventListener("click", function() { // Task Management
    window.location.href = "https://agnidevbot.streamlit.app/";
});

document.getElementById("viewFinances").addEventListener("click", function() { // Financial Management
    window.location.href = "/finance/finance.html";
});

document.getElementById("logout").addEventListener("click", function () {
    // Check if the confirmation dialog already exists to avoid duplicates
    if (document.querySelector(".confirm")) return;

    // Create the confirmation dialog
    let confirmBox = document.createElement("div");
    confirmBox.classList.add("confirm");
    confirmBox.innerHTML = `
      <h2>Are you sure you want to logout?</h2>
      <div class="yes-no">
        <button id="yes">Yes</button>
        <button id="no">No</button>
      </div>
    `;

    // Append the confirmation box to the body
    document.body.appendChild(confirmBox);

    // Add event listener to the 'No' button to remove the confirmation box
    document.getElementById("no").addEventListener("click", function () {
        confirmBox.remove(); // Removes the confirmation dialog
    });

    // Optional: Add event listener to the 'Yes' button for actual logout logic
    document.getElementById("yes").addEventListener("click", function () {
        window.location.href = '/login.html';
        confirmBox.remove(); 
    });
});

document.getElementById("profile").addEventListener("click", () => {
  window.location.href = "/profile/profile.html"
})

document.getElementById("about").addEventListener("click", () => {
  window.location.href = "/about.html"
})