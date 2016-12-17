import webapp2
import jinja2
import time
import os
from google.appengine.ext import db
from google.appengine.api import memcache
from user import *

desig = {1:"Professor", 2:"Associate Professor", 3:"Assistant Professor Sr.Gr", 4:"Assistent Professor", 5:"Teaching Fellow"}

def top_staff(update = False):
	key = "top"
	staffs = memcache.get(key)
	if staffs is None or update:
		staffs = db.GqlQuery("SELECT * FROM staff ORDER BY des ASC")
		staffs = list(staffs)
		memcache.set(key,staffs)
	return staffs

class staff(db.Model):
	staff_id = db.StringProperty(required = True)
	name = db.StringProperty(required = True)
	des = db.IntegerProperty(required = True)
	designation = db.StringProperty(required = True)
	created = db.DateTimeProperty(auto_now_add = True)

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

class adminLoginHandler(Handler):
	def render_front(self):
		self.render("admin_login.html")
	def get(self):
		self.render_front()
	def post(self):
		password = self.request.get("password")
		pass_word = valid_password(password)
		if pass_word and password == "darthvader":
			cookie_user_id = make_secure_val("krishna")
			self.response.headers.add_header('Set-Cookie', 'user_id=%s; Path=/'%cookie_user_id)
			self.redirect("/admin")
		else:
			self.render_front()

class adminHandler(Handler):
	def get(self):
		cookie_id = self.request.cookies.get("user_id")
		if cookie_id:
			id = check_secure_val(cookie_id)
			if id and id == "krishna":
				staffs = top_staff()
				self.render("admin.html", staffs = staffs)
			else:
				self.redirect('/admin-login')
		else:
			self.redirect('/admin-login')
	def post(self):
		name = self.request.get("name")
		des = self.request.get("des")
		staff_id = self.request.get("staffid")
		dele = self.request.get("del")
		if name and des and staff_id:
			a = staff(staff_id = staff_id, name = name, des = int(des), designation = desig[int(des)])
			a.put()
			time.sleep(2)
			staffs = top_staff(update = True)
			self.render("admin.html",staffs = staffs)
		elif dele:
			a = db.GqlQuery("SELECT * FROM staff where staff_id='%s'"%dele)
			a = a.get()
			a.delete()
			time.sleep(2)
			staffs = top_staff(update = True)
			self.render("admin.html",staffs = staffs)

class editPageHandler(Handler):
	def get(self,id):
		a = db.GqlQuery("SELECT * FROM staff WHERE staff_id='%s'"%id)
		a = a.get()
		self.render("edit_page.html",staff = a)
	def post(self,id):
		name = self.request.get("name")
		des = self.request.get("des")
		staff_id = self.request.get("staffid")
		if name and des and staff_id:
			b = db.GqlQuery("SELECT * FROM staff WHERE staff_id='%s'"%id)
			b = b.get()
			b.delete()
			time.sleep(2)
			a = staff(staff_id = staff_id, name = name, des = int(des), designation = desig[int(des)])
			a.put()
			time.sleep(2)
			staffs = top_staff(update = True)
			self.redirect('/admin')




app = webapp2.WSGIApplication([
    ('/', MainPage),('/infra',infraHandler),('/ug',UGHandler,),('/pg',PGHandler),('/part',partHandler),('/research',researchHandler),
    ('/staff',staffHandler),('/nstaff',nStaffHandler),('/students',studentsHandler),('/workshop',workshopHandler),
    ('/fv',fvHandler),('/ecea',eceaHandler),('/placements',placementsHandler),('/contact',contactHandler),('/forum',forumHandler),
    ('/staff-login',staffLoginHandler),('/admin-login',adminLoginHandler),('/admin',adminHandler),('/admin-(\d+)',editPageHandler)
], debug=True)
