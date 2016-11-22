import webapp2
import jinja2
import os

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
		self.render("infra.html")

class PGHandler(Handler):
	def get(self):
		self.render("infra.html")

class partHandler(Handler):
	def get(self):
		self.render("infra.html")

class staffHandler(Handler):
	def get(self):
		self.render("infra.html")

class nStaffHandler(Handler):
	def get(self):
		self.render("infra.html")

class studentsHandler(Handler):
	def get(self):
		self.render("infra.html")

class workshopHandler(Handler):
	def get(self):
		self.render("infra.html")

class fvHandler(Handler):
	def get(self):
		self.render("infra.html")

class eceaHandler(Handler):
	def get(self):
		self.render("infra.html")

class placementsHandler(Handler):
	def get(self):
		self.render("infra.html")

class contactHandler(Handler):
	def get(self):
		self.render("infra.html")

class forumHandler(Handler):
	def get(self):
		self.render("infra.html")

app = webapp2.WSGIApplication([
    ('/', MainPage),('/infra',infraHandler),('/ug',UGHandler,),('/pg',PGHandler),('/part',partHandler),
    ('/staff',staffHandler),('/nstaff',nStaffHandler),('/students',studentsHandler),('/workshop',workshopHandler),
    ('/fv',fvHandler),('/ecea',eceaHandler),('/placements',placementsHandler),('/contact',contactHandler),('/forum',forumHandler)
], debug=True)