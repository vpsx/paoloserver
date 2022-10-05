// Serve a silly "where is Paolo" page for fun and for tradition

const fs = require('fs');
const http = require('http');
const https = require('https');

// Not 127.0.0.1, unless you do mean accessible from localhost only
const hostname = '0.0.0.0';

// To run this program as a non-root user and bind to port 80
// since authbind is not an (easy) option for the current machine image
// we will do it the easy way: redirect port 80 to port 3000
// run this before running the program the first time.
// (And do it for 443 too!)
// sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 3000
const http_port = 3000;
const https_port = 3001;

const options = {
  //key: fs.readFileSync('key.pem'),
  //cert: fs.readFileSync('cert.pem')
};

const app = (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/html');
  res.end(`
<!DOCTYPE html>

<html lang="en">
<head>
    <title>Where's Paolo?</title>
</head>
<body>

  <div id="stuff" align="center">
  <h1>He's right here!</h1>
  <img src="https://raw.githubusercontent.com/vpsx/paoloserver/master/templates/paolo_smol.jpg" alt="(500 paolo did not load.)" style="width:786px;height:1048px;"></img>
  </div>

</body>
</html>
`);
};


http.createServer(app).listen(http_port, hostname, () => {
  console.log(`HTTP server running at ${hostname}:${http_port}/`);
});
https.createServer(options, app).listen(https_port, hostname, () => {
  console.log(`HTTPS server running at ${hostname}:${https_port}/`);
});
