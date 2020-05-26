from application import web, views



routes = [
	web.get("/user", views.user), 
	web.post("/login", views.login), 
	web.post("/register", views.register), 


]