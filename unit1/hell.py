import webapp2
import cgi

def escape_html(s):
    return cgi.escape(s, quote = True)

form = """
<form method="post">
    What is your birthday?
    <br>
    <label>
        Month
        <input type="text" name="month"  value="%(month)s">
    </label>
    <br><br>
    <input type="submit">
</form>
"""
months=['January','February','March','April','May','June','July','August',
'September','October','November','December']

class MainPage(webapp2.RequestHandler):
    def write_form(self,month=""):
        self.response.out.write(form %{"month":escape_html(month)})
    def get(self):
        self.write_form()
    def post(self):
        user_month = self.request.get('month')
        self.write_form(user_month)

class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Thanks! That's a totally valid day!")

application = webapp2.WSGIApplication([('/', MainPage),
                              ('/thanks', ThanksHandler)],
                             debug=True)

