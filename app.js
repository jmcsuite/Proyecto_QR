const express = require('express')
const app = express()
const port = 3000;

const multer  = require('multer')
const upload = multer({ dest: 'uploads/' })

app.use('/static', express.static(__dirname + '/FrontEnd'));

//const bodyParser = require('body-parser');
//app.use(bodyParser.urlencoded({ extended: true, limit: '50mb'}));

//app.use(express.json({limit: '50mb'}))

app.get('/', (req, res) => {
  //var pinky = require('../FrontEnd/index.html');
  console.log("Servidor prueba en el ge  dasdasdt");
  //res.send("Hello world!");
  //res.send(pinky);
  res.sendFile(__dirname + '/FrontEnd/index.html');
})

app.post('/', upload.single('imagen'), (req, res) => {
  //var pinky = require('../FrontEnd/index.html');
  console.log("Servidor prueba en el post");
  //res.send("Hello world!");
  //res.send(pinky);
  console.log(req.file)
  let a = "poooss"
  res.json(a)
})



app.listen(port, () => {
  console.log("Servidor prueba 1");
  console.log(`Example app listening at http://localhost:${port}`);
})

