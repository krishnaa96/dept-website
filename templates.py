import webapp2
import jinja2
import os
from google.appengine.ext import db
from user import *

staff_list = [{"user":"muttan", "pass":"ina103"},{"user":"meenakshi", "pass":"mcp23008"}]
def db_init():
	for staff in staff_list:
		username = staff["user"]
		password = staff["pass"]
		hash_pw = make_pw_hash(username, password)
		a = users(username = username, password = hash_pw)
		a.put()

class users(db.Model):
	username = db.StringProperty(required = True)
	password = db.StringProperty(required = True)
	created = db.DateTimeProperty(auto_now_add = True)


template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),autoescape=True)

class Handler(webapp2.RequestHandler):
	def write(self,*a,**kw):
		self.response.write(*a,**kw);
	def render_str(self,template,**params):
		t = jinja_env.get_template(template)
		return t.render(params)
	def render(self,template,**kw):
		self.write(self.render_str(template,**kw))

class MainPage(Handler):
	def get(self):
		self.render("index.html")

class infraHandler(Handler):
	def get(self):
		self.render("infra.html")

class UGHandler(Handler):
	def get(self):
		self.render("ug.html")

class PGHandler(Handler):
	def get(self):
		self.render("pg.html")

class partHandler(Handler):
	def get(self):
		self.render("part.html")

class staffHandler(Handler):
	def get(self):
		self.render("staff.html")

class nStaffHandler(Handler):
	def get(self):
		self.render("nstaff.html")

class studentsHandler(Handler):
	def get(self):
		self.render("students.html")

class workshopHandler(Handler):
	def get(self):
		self.render("workshop.html")

class fvHandler(Handler):
	def get(self):
		self.render("fv.html")

class eceaHandler(Handler):
	def get(self):
		self.render("ecea.html")

class placementsHandler(Handler):
	def get(self):
		self.render("placements.html")

class contactHandler(Handler):
	def get(self):
		self.render("contact.html")

class forumHandler(Handler):
	def get(self):
		self.render("forum.html")

class researchHandler(Handler):
	def get(self):
		self.render("research.html")

class staffLoginHandler(Handler):
	def render_front(self,username="",password=""):
		self.render("staff_login.html",username = username, password = password)
	def get(self):
		self.render_front()
	def post(self):
		username = self.request.get("username")
		password = self.request.get("password")
		user_name = valid_username(username)
		pass_word = valid_password(password)
		if user_name and pass_word:
			a = db.GqlQuery("SELECT * FROM users WHERE username='%s'"%username)
			user = a.get()
			if user:
				valid = valid_pw(username, password, user.password)
				if valid:
					id = user.key().id()
					cookie_user_id = make_secure_val(str(id))
					self.response.headers.add_header('Set-Cookie', 'user_id=%s; Path=/'%cookie_user_id)
					self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', MainPage),('/infra',infraHandler),('/ug',UGHandler,),('/pg',PGHandler),('/part',partHandler),('/research',researchHandler),
    ('/staff',staffHandler),('/nstaff',nStaffHandler),('/students',studentsHandler),('/workshop',workshopHandler),
    ('/fv',fvHandler),('/ecea',eceaHandler),('/placements',placementsHandler),('/contact',contactHandler),('/forum',forumHandler),
    ('/staff-login',staffLoginHandler)
], debug=True)
