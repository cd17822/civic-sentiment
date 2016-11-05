_ = require 'lodash'
router = (require 'express').Router()
formidable = require('formidable')
util = require('util')
fs = require('fs-extra')
qt = require('quickthumb')
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
  choice = Number req.query.choice
  res.render 'layout', title: 'Daily Sentiment', choice: choice

router.post '/upload', (req, res, next) ->
  console.log req.files
  console.log req.file
  console.log req.param.photo
  console.log req.query.photo
  choice = Number req.query.choice

  form = new (formidable.IncomingForm)
  form.parse req, (err, fields, files) ->
    res.writeHead 200, 'content-type': 'text/plain'
    res.write 'received upload:\n\n'
    res.end util.inspect fields: fields, files: files

  form.on 'end', (fields, files) ->
    ### Temporary location of our uploaded file ###
    temp_path = @openedFiles[0].path
    ### The file name of the uploaded file ###
    file_name = @openedFiles[0].name
    ### Location where we want to copy the uploaded file ###
    new_location = 'uploads/'

    fs.copy temp_path, new_location + file_name, (err) ->
      if err then console.error err
      res.render 'thankyou', title: 'Daily Sentiment', choice: choice

module.exports = router
