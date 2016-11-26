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

app = webapp2.WSGIApplication([
    ('/', MainPage),('/infra',infraHandler),('/ug',UGHandler,),('/pg',PGHandler),('/part',partHandler),
    ('/staff',staffHandler),('/nstaff',nStaffHandler),('/students',studentsHandler),('/workshop',workshopHandler),
    ('/fv',fvHandler),('/ecea',eceaHandler),('/placements',placementsHandler),('/contact',contactHandler),('/forum',forumHandler)
], debug=True)
