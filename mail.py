import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def mail(recipitent, message):
	me = 'jeevu.g1@gmail.com'
	you = recipitent
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "Link"
	msg['From'] = me
	msg['To'] = you

	# Create the body of the message (a plain-text and an HTML version).
	text = "Hi! " + recipitent + '\n'
	html = '''\
	<html>
	  <head></head>
	  <body>
	  ''' + text +'''
	    <p><br>
	       ''' + message + '''
	    </p>
	    <br>
	    <a href="http://0.0.0.0:2251/unsubscribe/'''+ recipitent +'''">unsubscribe</a>
	  </body>
	</html>
	'''

	# Record the MIME types of both parts - text/plain and text/html.
	part1 = MIMEText(text, 'plain')
	part2 = MIMEText(html, 'html')

	# Attach parts into message container.
	# According to RFC 2046, the last part of a multipart message, in this case
	# the HTML message, is best and preferred.
	msg.attach(part1)
	msg.attach(part2)
	
	try:
	    s = smtplib.SMTP('smtp.gmail.com:587')
	    s.ehlo()
	    s.starttls()
	    s.login('jeevu.g1@gmail.com',password_here)
	    s.sendmail(me, you, msg.as_string())
	    s.quit()        
	    print "Successfully sent email"
	except SMTPException:
	   print "Error: unable to send email"
