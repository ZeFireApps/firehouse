import requests
import json
from flask import jsonify,request
from app import app

URL = 'http://127.0.0.1:6680/mopidy/rpc'

@app.route('/play',methods=['POST','GET'])
def play():
	payload = {'jsonrpc':'2.0', 'id':1,'method':'core.playback.play'}
	headers = {'content-type':'application.json'}

	r=requests.post(URL,data=json.dumps(payload),headers=headers)
	return jsonify({'message':'playing'})

@app.route('/pause',methods=['POST','GET'])
def pause():
	payload = {'jsonrpc':'2.0', 'id':1,'method':'core.playback.pause'}
	headers = {'content-type':'application.json'}

	r=requests.post(URL,data=json.dumps(payload),headers=headers)
	return jsonify({'message':'paused'})

@app.route('/stop',methods=['POST','GET'])
def stop():
	payload = {'jsonrpc':'2.0', 'id':1,'method':'core.playback.stop'}
	headers = {'content-type':'application.json'}

	r=requests.post(URL,data=json.dumps(payload),headers=headers)
	return jsonify({'message':'stopped'})	

@app.route('/resume',methods=['POST','GET'])
def resume():
	payload = {'jsonrpc':'2.0', 'id':1,'method':'core.playback.resume'}
	headers = {'content-type':'application.json'}

	r=requests.post(URL,data=json.dumps(payload),headers=headers)
	return jsonify({'message':'resumed'})

@app.route('/add_track',methods=['POST'])
def add_track(uri=None,at_position=None):
	if not uri: uri = request.json['uri']
	params = {'uri':uri,'at_position':at_position}
	payload = {'jsonrpc':'2.0', 'id':1,'method':'core.tracklist.add','params':params}
	headers = {'content-type':'application.json'}

	r=requests.post(URL,data=json.dumps(payload),headers=headers)
	return jsonify({'message':'track added'})

@app.route('/clear',methods=['POST'])
def clear():
	payload = {'jsonrpc':'2.0', 'id':1,'method':'core.tracklist.clear'}
	headers = {'content-type':'application.json'}
	r=requests.post(URL,data=json.dumps(payload),headers=headers)
	return jsonify({'mesage':'tracklist cleared'})

@app.route('/arrived',methods=['POST'])
def arrival():
	clear()
	add_track(uri=request.json['uri'],at_position=0)
	play()
	print request.json
	return jsonify({'message':'Welcome Home: '+str(request.json['username'])})