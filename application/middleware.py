import functools
from application import json  
from application.models import User



def auth(func):
	@functools.wraps(func)

	async def wrapper(request):
		ok, auth = request.auth
		if ok :
			request.user = User.obj.get(id=auth['sub'])
			return await func(request)

		return json({'message': auth}, status=401)

	return wrapper