var http = require('http').createServer(handler); //require http server, and create server with function handler()
var fs = require('fs'); //require filesystem module
var io = require('socket.io')(http) //require socket.io module and pass the http object (server)

const SerialPort = require('serialport');
const Readline = SerialPort.parsers.Readline;

const parser = new Readline();

const mySerial = new SerialPort('/dev/ttyUSB0', {
  baudRate: 9600
});

mySerial.pipe(parser);

mySerial.on('open', function () {
  console.log('Opened Port.');
});

mySerial.on('data', function (data) {
 
  console.log(data.toString());

});


http.listen(8080); 

function handler (req, res) { 
  fs.readFile(__dirname + '/public/p1.html', function(err, data) { 
    if (err) {
      res.writeHead(404, {'Content-Type': 'text/html'}); 
      return res.end("404 Not Found");
    }
    res.writeHead(200, {'Content-Type': 'text/html'}); 
    res.write(data); 
    return res.end();
  });
}

io.sockets.on('connection', function (socket) {
  
  parser.on('data', function(data) {
    
    socket.emit('data', data);
    
    
  });

});




