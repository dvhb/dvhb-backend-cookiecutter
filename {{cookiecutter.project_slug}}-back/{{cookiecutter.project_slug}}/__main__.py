import argparse

from aiohttp import web

from .app import Application


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', '-p', type=int)
    parser.add_argument('--host', type=str, default='localhost')
    parser.add_argument('--no-debug', action='store_true')
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()

    debug = not args.no_debug
    app = Application(debug=debug)
    web.run_app(app, port=args.port, host=args.host)

main()
