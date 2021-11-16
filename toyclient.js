// Toy client for test purposes
const { WebSocket } = require('ws');

const ws = new WebSocket('ws://localhost:8080');

ws.on('open', function open() {
  ws.send('Hello from test client');
});

ws.on('message', function incoming(message) {
  console.log('received: %s', message);
});
