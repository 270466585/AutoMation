# coding:utf-8
import HTMLTestRunner,unittest,os,time,smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#用例路径
case_path=os.path.join(os.getcwd(),"testCase1")
#报告路径
report_path=os.path.join(os.getcwd(),"Result")

###--------定义发送邮件函数-----------##
def send_mail(report_file):
    # 发送邮箱
    sender = "15002838657@163.com"
    # 接收邮箱
    receiver = "270466585@qq.com"
    # 发送邮件服务器
    smtpserver = "smtp.163.com"
    # 发送邮箱账号和密码
    username = "15002838657@163.com"
    password = "980660765a"
    # 读取测试报告的内容
    with open(report_file, "rb") as f:
        mail_body = f.read()
    #定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body,_subtype='html', _charset='utf-8')
    msg['Subject'] = u"自动化测试报告"
    msg['from'] = sender
    msg['to'] = receiver
    #加上时间戳，好像没什么卵用
    msg["date"] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    msg.attach(body)
    #添加附件
    att = MIMEText(open(report_file).read(), "base64", "gbk")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename= "report.html"'
    msg.attach(att)
    #登录邮箱
    smtp = smtplib.SMTP()
    #连接邮箱服务器
    smtp.connect(smtpserver)
    #用户名密码
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print ('邮件已发送至对应账号！！')

#########--------发送最新的测试报告----------###
def send_report():
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(report_path+"/"+fn))
    print (u'最新测试生成的报告： '+lists[-1])
    #找到最新生成的报告文件
    report_file = os.path.join(report_path, lists[-1])
    #调用发邮件函数
    send_mail(report_file)

def all_case():
    testunit = unittest.TestSuite()
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern="test*.py",
                                                   top_level_dir=None)
    # discover方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
    return testunit


if __name__=="__main__":
    now_time = time.strftime('%Y_%m_%d %H_%M_%S', time.localtime(time.time()))
    repore_abspath=os.path.join(report_path,now_time+"result.html")
    fp=open(repore_abspath,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
                                         title=u'供应链管理系统自动化测试报告：',
                                         description=u'用例执行情况')
    runner.run(all_case())
    fp.close()
    #send_report()
