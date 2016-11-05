_ = require 'lodash'
router = (require 'express').Router()
### FOR AUTHENTICATION
rek = require 'rekuire'
configs = rek 'config'
basicAuth = require 'basic-auth-connect'

# add authentication
router.use basicAuth configs.USERNAME, configs.PASSWORD

# only allow https
router.use (req,res,next) ->
  if req.headers['x-forwarded-proto'] != 'https' and process.env.NODE_ENV? then res.sendStatus 401
  else next()
###

router.get '/', (req, res, next) ->
  res.render 'index', title: 'project'

module.exports = router
