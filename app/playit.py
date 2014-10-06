import requests
import json
from app import app

@app.route('/play')
def play():
	url = 'http://127.0.0.1:6680/mopidy/rpc'
	payload = {'jsonrpc':'2.0', 'id':1,'method':'core.playback.play'}
	headers = {'content-type':'application.json'}

	r=requests.post(url,data=json.dumps(payload),headers=headers)
	return r

@app.route('/pause')
def pause():
	url = 'http://127.0.0.1:6680/mopidy/rpc'
	payload = {'jsonrpc':'2.0', 'id':1,'method':'core.playback.pause'}
	headers = {'content-type':'application.json'}

	r=requests.post(url,data=json.dumps(payload),headers=headers)
	return r

@app.route('/stop')
def stop():
	url = 'http://127.0.0.1:6680/mopidy/rpc'
	payload = {'jsonrpc':'2.0', 'id':1,'method':'core.playback.stop'}
	headers = {'content-type':'application.json'}

	r=requests.post(url,data=json.dumps(payload),headers=headers)
	return r	

@app.route('/resume')
def resume():
	url = 'http://127.0.0.1:6680/mopidy/rpc'
	payload = {'jsonrpc':'2.0', 'id':1,'method':'core.playback.resume'}
	headers = {'content-type':'application.json'}

	r=requests.post(url,data=json.dumps(payload),headers=headers)
	return r
