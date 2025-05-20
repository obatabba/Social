from waitress import serve
from social import wsgi

if __name__ == '__main__':
    serve(wsgi.application, listen='127.0.0.1:8080')