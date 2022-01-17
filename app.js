const express = require('express')
const app = express()
const port = 3000;

app.use('/', express.static(__dirname + '/FrontEnd'));



app.get('/', (req, res) => {
  //var pinky = require('../FrontEnd/index.html');
  console.log("Servidor prueba en el ge  dasdasdt");
  res.send("Hello world!");
  //res.send(pinky);
  //res.sendFile(__dirname + '/FrontEnd/index.html');
})

app.post('/', (req, res) => {
  //var pinky = require('../FrontEnd/index.html');
  console.log("Servidor prueba en el post");
  //res.send("Hello world!");
  //res.send(pinky);
  console.log(req.body)
  res.send('posttt')
})



app.listen(port, () => {
  console.log("Servidor prueba 1");
  console.log(`Example app listening at http://localhost:${port}`);
})

