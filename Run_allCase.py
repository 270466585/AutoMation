# coding:utf-8
import HTMLTestRunner,unittest,os,time
#用例路径
case_path=os.path.join(os.getcwd(),"TestCase1")
#报告路径
report_path=os.path.join(os.getcwd(),"Result")

def all_case():
    discover=unittest.defaultTestLoader.discover(case_path,
                                                 pattern="test*.py",
                                                 top_level_dir=None)
    return discover

if __name__=="__main__":
    now_time = time.strftime('%Y_%m_%d %H_%M_%S', time.localtime(time.time()))
    repore_abspath=os.path.join(report_path,now_time+"result.html")
    fp=open(repore_abspath,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
                                         title='供应链管理系统自动化测试报告：',
                                         description=u'用例执行情况')
    runner.run(all_case())
    fp.close()