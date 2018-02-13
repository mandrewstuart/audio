from bottle import *

@get('/')
def index():
  return template('audio.tpl')


@get('/js/recorderjs/recorder.js')
def index():
  return template('recorder.js')



@get('/js/main.js')
def index():
  return template('main.js')



@get('/js/recorderjs/recorderWorker.js')
def index():
  return template('recorderWorker.js')



run(host='0.0.0.0', server='paste', port=80)
