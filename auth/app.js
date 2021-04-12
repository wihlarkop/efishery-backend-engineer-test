const express = require('express');
const bodyParser = require('body-parser')
const cors = require('cors');
const path = require('path');


const app = express();
const port = 3000

const AuthRoutes = require('./app/routes/auth');

require('dotenv').config()

app.use(bodyParser.urlencoded({
    extended: true
}));
app.use(bodyParser.json());
app.use(cors());
app.use('/api/v1/auth/', AuthRoutes);

app.use((req, res, next) => {
    const error = new Error('Pages Not Found');
    error.status = 404;
    next(error);
});
app.use((error, req, res, next) => {
    res.json({
        error: {
            message: error.message
        }
    });
});


app.listen(port, () => {
    console.log(`Auth app running at http://localhost:${port}`)
})