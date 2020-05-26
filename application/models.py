



class User:

	def __init__(self, id, fullname, email, password, role):
		self.id = id
		self.fullname = fullname
		self.email = email 
		self.password = password
		self.role = role 

	def __rept__(self):
		return "<User %s>"%self.fullname

	class obj:
		_storage = []
		_id = 0

		@classmethod
		def create(cls, fullname, email, password, role='user'):
			cls._id += 1
			user = User(cls._id, fullname, email, password, role)
			cls._storage.append(user)
			return user

		@classmethod
		def all(cls):
			return cls._storage

		@classmethod
		def filter(cls, **kwargs):
			users = cls._storage
			for k, v in kwargs.items():
				if v:
					users = [u for u in users if getattr(u, k, None) == v]
			return users


		@classmethod
		def get(cls, email=None , id=None):
			user = cls.filter(id=id, email=email)
			return user[0] if len(user) >= 1 else None 