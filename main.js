const express = require("express");
const path = require("path");
const bodyParser = require("body-parser");

const app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: true })); // Middleware to parse form data

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "login.html"));
});

app.use(express.static(path.join(__dirname, "public")));


app.get("/index/index.html", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "index/index.html"));
});


// Start Server
const PORT = 3000;
app.listen(PORT, () => console.log(`Server running at http://localhost:${PORT}`));
