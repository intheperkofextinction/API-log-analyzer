// server.js

const express = require(`express`);
const fs = require(`fs`);
const app = express();
const port = 3000;

// Middleware to log each request
app.use((req, res, next) => {
	const log = `${new Date().toISOString()} - ${req.method} ${req.url}\n`; // Log format
	fs.appendFileSync(`request.log`, log); // Write log to file
	next(); // Continue with the next middleware or route handler
});

// Home route
app.get(`/`,(req, res) => {
	res.send(`Welcome to the homepage!`);
});

// About route
app.get(`/about`, (req, res) => {
	res.send(`This is the about page!`);
});

// Start the server
app.listen(port, () => {
	console.log(`server running at http://localhost:${port}`);
});
