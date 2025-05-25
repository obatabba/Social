import os
from waitress import serve
from social import wsgi

if __name__ == '__main__':
    port = os.environ.get('PORT_NUMBER', '8000')
    serve(wsgi.application, listen=f'*:{port}')