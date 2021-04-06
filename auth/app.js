const express = require('express');
const cors = require('cors')
const app = express();

const AuthRoutes = require('./app/routes/auth');


require('dotenv').config()


app.get('/', (req, res) => {
    res.send("Alive");
})

app.use(cors());
app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-header', 'Origin, X-Requested-With,Content-Type, Accept, Authorization');
    res.header('Access-Control-Allow-Credentials', true);

    if (req.method === 'OPTIONS') {
        res.header('Access-Control-Allow-Methods', 'PUT, POST, PATCH, DELETE, GET');
        return res.status(200).json({});
    }
    next();
});

app.use((req, res, next) => {
    const error = new Error('Pages Not Found');
    error.status = 404;
    next(error);
});

app.use((error, req, res, next) => {
    res.status(error.status || 500);
    res.json({
        error: {
            message: error.message
        }
    });
});

app.listen(process.env.PORT)

app.use('/api/v1/auth', AuthRoutes);

module.exports = app;