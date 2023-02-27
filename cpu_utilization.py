import psutil as ps
import platform as p
from datetime import datetime
from email.message import EmailMessage
import ssl
import smtplib
import time

class CheckCPUUsage():
    window_env = ""
    os_runing = ""
    def __init__(self):
        """
        This class is created to check the cpu utilization of my computer and triggered up an email telling my that my computer cpu has been overused. 
        """
    def ComputerProperties(self):
        print("\nYour computer informations\n")
        print(f'Run At: {datetime.now()}')
        os_type = p.system()
        os_version = p.version()

        return "Operating System: {}\nVersion: {}".format(os_type, os_version)


    def GetCPUUtilization(self):
        capture_usage = ps.cpu_percent(1)
        return capture_usage

    def Alert(self):
        sender = "crawlerd01@gmail.com"
        receiver = "femej95268@youke1.com"
        sender_pass = 'plgbamdxnxovxdun'
        sender_subject = "CPU Utilization Notification"
        body = f"Your Computer CPU has been running above 5min"

        em = EmailMessage()
        em['From'] = sender
        em['To'] = receiver
        em['Subject'] = sender_subject
        em.set_content(body)

        mailContext = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=mailContext) as smtp:
            smtp.login(sender, sender_pass)
            smtp.sendmail(sender,receiver, em.as_string())



#Create a while loop that monitors my CPU Utilization
while True:
    cpu_util = CheckCPUUsage()
    CPUWatcher = cpu_util.GetCPUUtilization()
    print(CPUWatcher, end="\r")

    #checking if cpu has gone above 5%
    if CPUWatcher > 5.0:
        print(f"CPU IOP is running at, ({CPUWatcher})\n")
        print("Checking if CPU usage has gone above '5.0%' minunte")

        countdown = 5
        for x in range(countdown, 0, -1):
            print(x)
            time.sleep(1)
            if x == 1:
                print("CPU Utilization has gone above 5min percent")
                alertMessage = CheckCPUUsage()
                alertMessage.Alert()
                break
