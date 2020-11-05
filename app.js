const express = require("express");
const {Board, Servo} = require("johnny-five");
const keypress = require("keypress");


const app = express();
const board = new Board();


board.on("ready", () => {

    const servo = new Servo.Continuous(10);

    app.set('view engine', 'ejs');
    app.set('views', 'html');

    app.listen(3001);

    app.use(express.static('static'));

    app.use((req, res, next) => {
        console.log('----new request made----');
        console.log('host: ' + req.hostname);
        console.log('path: ' + req.path);
        console.log('method: ' + req.method);
        next();
    });

    app.get('/', (req,res) => {
        res.render('index');
    });

    app.get('/drehen', (req, res) => {
        servo.ccw();
        setTimeout(function() {
            servo.stop();
            servo.cw();
        }, 1000);
        setTimeout(function() {
            servo.stop();
        }, 1000);
    });
});