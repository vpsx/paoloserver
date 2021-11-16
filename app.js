const { WebSocket, WebSocketServer } = require('ws');

const wss = new WebSocketServer({ port: 8080 });

wss.on('connection', function connection(ws) {
  ws.on('message', function message(data, isBinary) {
    console.log('received: %s', data);

    wss.clients.forEach(function each(client) {
      if (client !== ws && client.readyState === WebSocket.OPEN) {
        console.log('forwarding: %s', data);
        client.send(data, { binary: isBinary });
      }
    });
  });

  ws.send('Connection established; broadcasting messages');
});
