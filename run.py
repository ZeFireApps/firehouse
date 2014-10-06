from app import app

app.host = '0.0.0.0'
app.debug = True

if __name__ == '__main__':
	app.run