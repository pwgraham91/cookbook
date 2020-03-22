#!flask/bin/python
from app import app

if app.env == 'docker_local':
    app.run(host='0.0.0.0', debug=True)
elif app.env == 'production':
    app.run(host='0.0.0.0', threaded=True)
else:
    app.run(debug=True)
