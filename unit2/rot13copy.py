import webapp2
import cgi
import re
class Rot13Handler(webapp2.RequestHandler):
    def get(self):
        self.write_out()

    def post(self):
        txt = self.request.get('text') # Extract text from textarea
        rot13txt = self.rot13(txt)

        self.write_out(escape(rot13txt))

    def rot13(self, s):
        """Return ROT13 converted string. Punctuations left untouched."""
        res=''
        for chr in s:
            if chr.isalpha():
                if chr.isupper(): # Character is uppercase
                    if ord(chr) + 13 > 90:
                        res += unichr(ord(chr) - 13)
                    else:
                        res += unichr(ord(chr) + 13)
                else: # Character is lowercase
                    if ord(chr) + 13 > 122:
                        res += unichr(ord(chr) - 13)
                    else:
                        res += unichr(ord(chr) + 13)
                continue
            res += chr
        return res

    def write_out(self, name=''):
        self.response.out.write(rot13_form % {'name': name})

def escape(txt):
    """Escape out special HTML characters in string"""
    return cgi.escape(txt, quote=True);

application = webapp2.WSGIApplication([('/unit2/rot-13', Rot13Handler)], 
                                debug=True)

rot13_form = """
<h2>Enter some text to ROT13 - :-):</h2>
<form method="post">
    <textarea name="text" 
        style="height: 100px; width: 400px;">%(name)s</textarea>
    <br>
    <input type="submit">
</form>
"""
