#sending mail using python



import smtplib
try:
	s=smptib.SMPT('smpt.gmail.com','587')
	s.starttls()
	sender='Rittikaraj111@gamil.com'
	receiver='rajrittika690@gmil.com'
	msg="hii"
	s.login(sender,'9119984225')
	s.sendmail(sender,receiver,msg)
except:
	print("some error occured")
else:
	print("msg sent sucessfully")
	s.quit()			