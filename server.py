from waitress import serve
from social import wsgi

if __name__ == '__main__':
    serve(wsgi.application, listen='*:8080')