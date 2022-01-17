import './FrontEnd/estilos.css';
const {loadImg} = require('canvas');
var express = require('express');
var app = express();
app.get('/', function(req, res){
  res.render('layout', {title: 'frontpage'});
});
module.exports = app;