import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

file = open('Final-Project/email.txt', 'r').read()
flx = file.split()

    
sender_email = "sulthan.a2.pilkom@gmail.com"
rec_email = flx
body = "Ini tugas terakhir\n coba"
msg = MIMEMultipart()
msg['Subcject'] = "Final_Project" 
msg['From'] = sender_email
msg['To'] = ', '.join(flx)



msg.attach(MIMEText(body, 'plain'))
password =input(str("Masukan Password :"))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
text = msg.as_string()
server.sendmail(sender_email, rec_email, text)
server.quit()