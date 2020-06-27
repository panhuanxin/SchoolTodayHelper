#通过审核
from selenium import webdriver
import re,time

wait_time = 1
wait_time1 = 3
ordername = input("需要指定人的在此项填入名字：\n")

def _shenpi():
    """
    模拟审批
    """
    list1 = []
    html = driver.page_source
    #判断是否需要选择下一位审批人，请假详情有需要选择下一位审批人和不需要两种情况
    reobj = re.compile(r'<div data-v-6dc7dd24="" class="form-group mb-10"><label data-v-6dc7dd24="" class="label">下一级([\s\S]*?)人：</label> <div data-v-6dc7dd24="" class="ivu-select ivu-select-single" style="width: 200px;"><div class="ivu-select-selection"><input type="hidden">  <span class="ivu-select-placeholder">请([\s\S]*?)择', re.MULTILINE)
    list1 = [match.group(1) for match in reobj.finditer(html)]
    if len(list1)>0:    
        driver.find_element_by_xpath("//span[contains(text(),'请选择')]").click()
        driver.find_element_by_xpath("//li[6]").click()
        time.sleep(wait_time)
        driver.find_element_by_xpath("//button[@type='button']").click()
        time.sleep(wait_time)
        driver.find_element_by_xpath("//button[@class='ivu-btn ivu-btn-primary ivu-btn-large']").click()
    else:
        time.sleep(wait_time)
        driver.find_element_by_xpath("//button[@type='button']").click()
        time.sleep(wait_time)
        driver.find_element_by_xpath("//button[@class='ivu-btn ivu-btn-primary ivu-btn-large']").click()

def piga_qingjia(ordername):
    """
    批改请假审批
    """ 
    i = 0
    html = driver.page_source
    if ordername not in _extract_names(html):
        if ordername != "":
            print("没有此人请假信息")
        else:
            pass
    else:
        for x in _extract_names(html):
            i = i+1
            if x == ordername:
                a = "/html/body/div[4]/div[2]/div[2]/div/div[2]/div[1]/div/div[3]/div/div/div[5]/div[2]/table/tbody/tr[" + str(i) + "]/td[1]/div"
                driver.find_element_by_xpath(a).click()
                time.sleep(wait_time)
                _shenpi()
                time.sleep(wait_time)
                driver.get("https://zjiet.cpdaily.com/wec-counselor-leave-apps/leaveadmin/pcAdmin/index.html#/list")
                time.sleep(wait_time)
                print(x,"的请假批改完毕")
                break
    while ordername == "":
        html = driver.page_source
        names = _extract_names(html)
        if len(names) == 0:
            print('请假批改完毕')
            break 
        time.sleep(2)
        #模拟点击查看详情
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div/div[2]/div[1]/div/div[3]/div/div/div[5]/div[2]/table/tbody/tr[1]/td[1]/div").click()
        time.sleep(wait_time)
        _shenpi()
        time.sleep(wait_time)
        driver.get("https://zjiet.cpdaily.com/wec-counselor-leave-apps/leaveadmin/pcAdmin/index.html#/list")
        time.sleep(wait_time)
if __name__ == "__main__":
    piga_qingjia(ordername)