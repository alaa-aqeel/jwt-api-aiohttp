import jwt, datetime


def createToken(request, user):
	return jwt.encode({
			'iat': datetime.datetime.utcnow(),
			'sub': user.id 
		}, 
		request.app['config']['secret_key'],
		algorithm='HS256'
	).decode('utf-8')

def decodeToken(request, token):

	try:
		payload = jwt.decode(
			token.split(" ")[-1],
			request.app['config']['secret_key'],
			algorithm='HS256'
		)
		return True, payload
	except jwt.ExpiredSignatureError:
		return False, 'Signature expired. Please log in again.'

	except jwt.InvalidTokenError:
		return False, 'Invalid token. Please log in again.'

	return False, 'Some Error '
