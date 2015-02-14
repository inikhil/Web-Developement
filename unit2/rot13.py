import webapp2
import cgi

def escape_html(s):
     return cgi.escape(s,quote = True)
form="""
<form method="post">
    Enter some text to ROT13
    <br>
    <label>
    <textarea name="text">%(text)s</textarea>
    </label>
    <br>
    <input type="submit">
</form>
"""

def rot13imp(s):
    s=list(s)
    for i in range(0,len(s)):
	if((ord(s[i]) >= 65 and ord(s[i])<=77) or(ord(s[i]) >= 97 and ord(s[i])<=109)):
		s[i]=chr(ord(s[i])+13)
	elif((ord(s[i]) >= 78 and ord(s[i])<=90)or(ord(s[i]) >= 110 and ord(s[i])<=122)):
		s[i]=(chr(ord(s[i])-13))
    return s



class MainPage(webapp2.RequestHandler):
    def write_form(self,text=""):
	self.response.out.write(form %{"text":escape_html(text)})

    def get(self):
	self.write_form()
    def post(self):
	user_entry = self.request.get('text')
	user_entry = rot13imp(user_entry)
	user_entry=''.join(user_entry)
	self.write_form(user_entry)


application = webapp2.WSGIApplication([('/', MainPage)],debug=True)	
