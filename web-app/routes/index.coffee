_ = require 'lodash'
router = (require 'express').Router()
formidable = require('formidable')
util = require('util')
fs = require('fs-extra')
qt = require('quickthumb')
spawn = require("child_process").spawn;
request = require 'request'
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
  choice = req.query.choice
  request
    url: "https://c92353fc.ngrok.io/#{choice}"
    method: 'GET'
    json: true
    (error, response, worker) ->
      if error then console.log Error error
      else console.log "fireworked"
  res.render 'layout', title: 'Daily Sentiment', choice: choice

router.post '/upload', (req, res, next) ->
  choice = Number req.query.choice
  candidate = "clinton"
  if choice == 2 then choice = "trump"

  form = new (formidable.IncomingForm)
  form.parse req, (err, fields, files) ->
    res.render 'thankyou', title: 'Daily Sentiment', choice: choice

  form.on 'end', (fields, files) ->
    ### Temporary location of our uploaded file ###
    temp_path = @openedFiles[0].path
    ### The file name of the uploaded file ###
    file_name = @openedFiles[0].name
    ### Location where we want to copy the uploaded file ###
    new_location = 'uploads/'

    fs.copy temp_path, new_location + file_name, (err) ->
      if err then console.error err
      else
        process = spawn('python',["imageprocessor.py", new_location + file_name]);
        process.stdout.on 'data', (data) ->
          request
            url: "https://c92353fc.ngrok.io/#{candidate}pic?filename=#{file_name}"
            method: 'GET'
            json: true
            (error, response, worker) ->
              if error then console.log Error error
              else console.log "picked"

module.exports = router
