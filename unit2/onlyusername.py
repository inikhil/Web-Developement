import webapp2
import cgi

def escape_html(s):
    return cgi.escape(s, quote = True)

import re
user_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
#pass_re = re.compile(r"^.{3,20}$")
#email_re = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

def valid_username(username):
    return user_re.match(username)

def valid_password(password):
    return pass_re.match(password)

def valid_email(email):
    return email_re.match(email)

#<label>
 #       Password
  #      <input type="password" name="password" value="%(password)s">
#	<div style="color: red">%(pass_error)s</div>
 #   </label>
  #  <label>
   #     Verify Password
    #    <input type="password" name="verify" value="%(verify)s">
	#<div style="color: red">%(ver_error)s</div>
    #</label>
   # <label>
  #      Email(Optional)
 #       <input type="text" name="email" value="%(email)s">
#	<div style="color: red">%(email_error)s</div>
#    </label> 

form = """
<form method="post">
    Signup
    <br>
    <label>
        Username
        <input type="text" name="username" value="%(username)s"><div style="color: red">%(user_error)s</div>
    </label>
    <br><br>
    <input type="submit">
</form>
"""


class MainPage(webapp2.RequestHandler):

 #   def write_form(self, user_error="",pass_error="",ver_error="",
#email_error="",username="",password="",verify="",email=""):
#	self.response.out.write(form %{"user_error": user_error,
#					"pass_error":pass_error,
#					"ver_error":ver_error,
#					"email_error":email_error,
#					"username":escape_html(username),
#					"password":"","verify":"",
#					"email":escape_html(email)})

    def write_form(self,user_error="",username=""):
	self.response.out.write(form % {"user_error":user_error,"username":escape_html(username)})
    def get(self):
        self.write_form()
    def post(self):
        username = self.request.get('username')
  #      password = self.request.get('password')
   #     verify = self.request.get('verify')
#	email= self.request.get('email')

        user_name = valid_username(username)
#	pass_word = valid_password(password)
 #       ema_il = valid_email(email)

	inv_user="That's not a valid username."
	inv_pass="That wasn't a valid password."
	inv_veri="Your password's didn't match "
	inv_email="That's not a valid email"

    	if not user_name:
		self.write_form(inv_user,username);
  #      if user_name and pass_word and ema_il:
   #         self.write_form(inv_user,inv_pass,"",inv_email,username,password,verify,email)
	#elif  pass_word and ema_il:
    	#     self.write_form("",inv_pass,"",inv_email,username,password,verify,email)
	#elif (user_name and pass_word):
	 #    self.write_form(inv_user,inv_pass,"","",username,password,verify,email)
	#elif (user_name and ema_il):
	 #    if(password==verify):
	#	   self.write_form(inv_user,"","",inv_email,username,password,verify,email)
	 #    if(password!=verify):
	  #          self.write_form(inv_user,"",inv_veri,inv_email,username,password,verify,email)
     #   elif  user_name:
      #       if(password==verify):
       #            self.write_form(inv_user,"","","",username,password,verify,email)
        #     if(password!=verify):
                  #  self.write_form(inv_user,"",inv_veri,"",username,password,verify,email)
        #elif  ema_il:
	 #    if(password==verify):
          #         self.write_form("","","",inv_email,username,password,verify,email)
           #  if(password!=verify):
                  #  self.write_form("","",inv_veri,inv_email,username,password,verify,email)
	#elif pass_word:
	 #    self.write_form("",inv_pass,"","",username,password,verify,email)

    	else:
        	 self.redirect("/welcome")

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Welcome")

application = webapp2.WSGIApplication([('/', MainPage),
                              ('/welcome', WelcomeHandler)],
                             debug=True)
