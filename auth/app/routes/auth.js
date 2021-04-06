const {Router} = require('express');
const AuthController = require('../api/authController');
const AuthJWT = require('../utils/dependency')

const router = Router();


router.post("/register", AuthController.register);

router.post("/login", AuthController.login);

router.get("/payload", AuthController.get_payload_data);


module.exports = router;