import smtplib
sender_email="manimalathi6384@gmail.com"
password="qqcr jvte pepv npnl"
to_email="thirthapriyan@gmail.com","kavincj007@gmail.com","mahendranselvam30@gmail.com","babuthala2003@gmail.com","satsiv464@gmail.com","senmyanbu@gmail.com","mughilanece2k@gmail.com","gokilavanim1998@gmail.com"
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(sender_email,password)
print("login successful")
server.sendmail(sender_email,to_email,"thursday onwards full days class")
print("email sent to ",to_email)
server.quit()