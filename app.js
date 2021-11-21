const { WebSocket, WebSocketServer } = require('ws');

const wss = new WebSocketServer({ port: 8080 });

wss.on('connection', function connection(ws, req) {
  const ip = req.socket.remoteAddress;

  ws.on('message', function message(data, isBinary) {
    console.log(`received from ${ip}: ${data}`);

    wss.clients.forEach(function each(client) {
      if (client !== ws && client.readyState === WebSocket.OPEN) {
        console.log(`forwarding: ${data}`);
        client.send(data, { binary: isBinary });
      }
    });
  });

  ws.send('Connection established; broadcasting messages');
});
