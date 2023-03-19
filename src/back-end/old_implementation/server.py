from gevent.pywsgi import WSGIServer
from api import app

http_server = WSGIServer(('', 8888), app)
http_server.serve_forever()