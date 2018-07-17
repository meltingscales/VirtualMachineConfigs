const port = 8081;
const express = require('express');
var app = express();
app.use(express.static(__dirname + '/'));
app.listen(port, function() {
    console.log("Server running at 'http://localhost:" + port + "'.")
});
