from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import sys
import threading
import selenium.webdriver.support.ui as ui


class ClassType:
    yibanzhuanye = 1
    hexinzhuanye = 2
    hexintongshi = 3
    yibanttongshi = 4

class CourseSelect:
    def __int__(self):
        pass

    def loginToSelectCource(self, username, pwd, className, classType):
        print("start")
        url="http://jwxt.buaa.edu.cn:7001/ieas2.1/"
        brower =webdriver.Edge("C:/Users/ziyuc/.conda/envs/pytorch/msedgedriver.exe")
        brower.get(url)
        brower.maximize_window()
        brower.find_element_by_xpath("/html/body/div/div[2]/div[1]/p[2]/input").click()

        frame = brower.find_element_by_id("loginIframe")
        brower.switch_to.frame(frame)

        brower.find_element_by_id("unPassword").send_keys(username)
        brower.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/input").send_keys(pwd)
        brower.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[1]/div[7]/input").click()


        brower.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/div/a[6]").click()
        time.sleep(1)

        if classType == ClassType.hexintongshi:
            brower.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[1]/div[6]/div[1]/a[3]").click()
            frame_C = brower.find_element_by_id("iframename")
            brower.switch_to.frame(frame_C)
            brower.find_element_by_xpath("/html[1]/body[1]/div[7]/div[1]/div[3]/table[1]/tbody[1]/tr[1]/td[1]/ul[1]/li[3]/a[1]").click()

        elif classType == ClassType.yibanzhuanye:
            brower.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[1]/div[6]/div[1]/a[4]").click()
            frame_C = brower.find_element_by_id("iframename")
            brower.switch_to.frame(frame_C)
            brower.find_element_by_xpath("/html[1]/body[1]/div[7]/div[1]/div[3]/table[1]/tbody[1]/tr[1]/td[1]/ul[1]/li[2]/a[1]").click() #一般专业

        elif classType == ClassType.hexinzhuanye:
            brower.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[1]/div[6]/div[1]/a[4]").click()
            frame_C = brower.find_element_by_id("iframename")
            brower.switch_to.frame(frame_C)

        elif classType == ClassType.yibanttongshi:
            brower.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[1]/div[6]/div[1]/a[3]").click()
            frame_C = brower.find_element_by_id("iframename")
            brower.switch_to.frame(frame_C)
            brower.find_element_by_xpath("/html[1]/body[1]/div[7]/div[1]/div[3]/table[1]/tbody[1]/tr[1]/td[1]/ul[1]/li[4]/a[1]").click()

        while 1:
            brower.find_element_by_xpath("/html[1]/body[1]/div[7]/div[1]/div[4]/form[1]/ul[1]/li[4]/input[1]").send_keys(className) #class

            brower.find_element_by_xpath("/html[1]/body[1]/div[7]/div[1]/div[4]/form[1]/ul[1]/li[6]/div[1]/a[1]").click() #search

            brower.find_element_by_xpath("/html[1]/body[1]/div[7]/div[1]/div[6]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/a[1]").click() #choose

            time.sleep(1)
            a = brower.switch_to.alert
            str = a.text
            print(str)
            a.accept()
            if str == '选课成功':
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                break

        time.sleep(100)
if __name__ == '__main__':
    username = ''  # 登录账号
    pwd = ''  # 登录账号对应密码
    className = '1'  # 选择课程 注意一定要是搜出来第一个选择的课程
    classType = ClassType.yibanttongshi

    xk =CourseSelect()

    xk.loginToSelectCource(username, pwd, className, classType)

