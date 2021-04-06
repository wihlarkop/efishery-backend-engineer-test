const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser')
const app = express();
const port = 3000

const AuthRoutes = require('./app/routes/auth');

require('dotenv').config()

app.use(bodyParser.urlencoded({
    extended: true
}));
app.use(bodyParser.json());
app.use(cors());


app.get('/api/v1/auth/alive', (req, res) => res.json('alive'));
app.use('/api/v1/auth', AuthRoutes);


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