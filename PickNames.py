#提取名字
from selenium import webdriver
import re,time

wait_time1 = 3

def _extract_names(html):
    time.sleep(wait_time1)
    reobj = re.compile(r'</td><td class=""><div title="[\s\S]*?" class="ivu-table-cell ivu-table-cell-ellipsis"><!----> <!----> <!----> <!----> <!----> <a title="([\s\S]*?)"><span>[\s\S]*?</span></a></div></td>', re.MULTILINE)
    names = [match.group(1) for match in reobj.finditer(html)]
    return names

def cnt_qinjia_peoples():
    html = driver.page_source
    li = _extract_names(html)
    print(li)
    print("人数：",len(li))

if __name__ == "__main__":
    cnt_qinjia_peoples()#task1