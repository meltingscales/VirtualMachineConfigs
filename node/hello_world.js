var http = require('http');
print = console.log;

http.createServer(function (req, res) {

  res.write('Hello World!'); //write a response to the client

  res.end(); //end the response
  
  res.write({'a':'b'})

}).listen(80);