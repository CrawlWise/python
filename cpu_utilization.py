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

    def get_cpu_utilization(self):
        capture_usage = ps.cpu_percent(1)
        return capture_usage

    def alert(self):
        sender = "crawlerd01@gmail.com"
        receiver = "crawlerd01@gmail.com"
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
            smtp.sendmail(sender, receiver, em.as_string())


# Create awhile loop that monitors my CPU Utilization

check = CheckCPUUsage()
print(check.ComputerProperties())
while True:
    cpu_util = CheckCPUUsage()
    CPUWatcher = cpu_util.get_cpu_utilization()
    print(CPUWatcher, end="\r")

    # checking if cpu has gone above 5%
    if CPUWatcher > 5.0:
        print(f"CPU IOP is running at, ({CPUWatcher}%)\n")
        for x in range(5, 0, -1):
            time.sleep(1)
            print(f'Countdown Timer: {x}')

        if cpu_util.get_cpu_utilization() > 5:
            print(f'CPU iOPs has gone above 50% for more than 5min\nSending a mail to admin\n')
            alertMessage = CheckCPUUsage()
            alertMessage.alert()
            print("Message sent Successfully")
        else:
            print("CPU Usage has return to Normal")
