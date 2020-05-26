from application import middleware
from application import web, json, 
from application.jwt_token import  createToken
from application.models import User


@middleware.auth
async def user(request):
	return json({
			'fullname' : request.user.fullname ,
			'email' : request.user.email ,
			'id' : request.user.id ,
		})


async def register(request):

	data = await request.post() 
	try:
		user = User.obj.create(data['fullname'], data['email'], data['password'])
		return json({
			'user' : user.id
		})
	except:
		return json({
				'message' : 'error data required {fullname, email, password}'
			})

async def login(request):
	
	data = await request.post()
	if not data.get('email') or not data.get('password'): 
		return json({ 'message' : 'required email/password'})

	user = User.obj.get(email=data.get('email'))
	if user :
		token = createToken(request, user)
		return json({
			'token' : token
		})

	return json({
			'message' : 'Not found user'
		})


	