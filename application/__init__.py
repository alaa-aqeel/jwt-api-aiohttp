import base64
from aiohttp import web
from cryptography import fernet
from application.jwt_token import decodeToken


def json(data, status=200):

	return web.json_response(data)


@web.middleware
async def authorization(request, handler):

	request.auth = False, 'need login'
	token = request.headers.get('authorization', None)

	if token:
		request.auth = decodeToken(request, token)

	response = await handler(request)
	return response


def create_app(config={}):	

	app = web.Application(middlewares=[authorization])

	fernet_key = fernet.Fernet.generate_key()
	config.update({
		'secret_key': base64.urlsafe_b64decode(fernet_key)
	})

	# set config 
	app['config'] = config

	# add routes 
	from application.routes import routes 
	app.add_routes(routes)

	return app
