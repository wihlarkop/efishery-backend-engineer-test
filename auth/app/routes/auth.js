const express = require("express");
const router = express.Router();
const AuthController = require('../api/authController');


router.post("/register", AuthController.register);

router.post("/login", AuthController.login);

router.get("/payload", AuthController.get_payload_data);


module.exports = router;