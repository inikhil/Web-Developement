import os
import webapp2
import jinja2
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name)


class Content(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
 
class newpost(Handler):

    def render_front(self, subject="", content="", error=""):
	#contents = db.GqlQuery("SELECT * FROM Content ORDER BY created DESC")
    	self.render("blogy1.html", subject=subject, content=content, error = error)
    def get(self):
        self.render_front()
    def post(self):
        subject = self.request.get("subject")
        content = self.request.get("content")
        if subject and content:
            a = Content(parent = blog_key(),subject = subject , content = content)
    	    a.put()
	    self.redirect('/%s' % str(a.key().id()))
        else:
            error = "we need both subject and content"
            self.render_front(subject,content,error)

class permalink(Handler):

 #   def render_front(self, subject="", content="", error="",contents=""):
	#contents = db.GqlQuery("SELECT * FROM Content ORDER BY created DESC")
    	#self.render("blogy.html", contents=contents)
	#contents = db.GqlQuery("SELECT * FROM Content ORDER BY created DESC")
    def get(self,post_id):
	key = db.Key.from_path('Content', int(post_id), parent=blog_key())
        a = db.get(key)
       # a = Content.get_by_id(int(post_id))
	if a:
            self.render("blogy2.html", subject=a.subject,content=a.content)


class MainPage(Handler):
    def render_front(self, subject="", content="", error=""):
	contents = db.GqlQuery("SELECT * FROM Content ORDER BY created DESC")
    	self.render("blogy.html", contents = contents)
    def get(self):
        self.render_front()

application = webapp2.WSGIApplication([('/', MainPage),('/newpost',newpost),('/(\d+)',permalink)], debug=True)
