import os
from flaskblog import create_app

app = create_app()

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 8000))
	app.run(debug=True, port=port)
