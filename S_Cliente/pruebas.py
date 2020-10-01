import smtplib
import os


server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login('s.cgrincon@gmail.com','Risas1998pip')
server.sendmail('s.cgrincon@gmail.com','diego.rincon.rosas@gmail.com',"respuesta_re")
server.quit()
print("Correo enviado")

