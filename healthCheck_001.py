#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-05-12 10:15:29
# @Author  : Jian Y (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
'''
1、使用Chrome浏览器，需要添加chromedriver.exe
2、python要安装selenium
'''

from selenium import webdriver
import time
# =============================================================================================
# Login ZJU
def LoginZJU(url,zju_username,zju_password):

    # 创建driver对象并读取某网页：统一身份认证
    driver= webdriver.Chrome() #使用Chrome打开
    driver.get(url)
    # print driver.page_source

    # 获取网页上某元素并改内容：zju通行证
    name = driver.find_element_by_id("username") 
    name.send_keys(zju_username)
    name = driver.find_element_by_id("password") 
    name.send_keys(zju_password)

    # 按钮操作：登录
    # login_button = driver.find_element_by_class_name("submit-row")
    login_button = driver.find_element_by_id("dl") 
    login_button.click()

    print 'Success Log in Health Check.'

    return driver
# =============================================================================================
# Set Info
def SetInfo(driver, Province, City, Village):
    # 导入Select模块
    from selenium.webdriver.support.ui import Select
    #-------------------------------------------------------------------------------------
    # 1)下拉框选 -Your Location

    # 按钮操作：点击
    # login_button = driver.find_element_by_class_name("submit-row")
    Location = driver.find_element_by_name("area") 
    Location.click() #自动获取位置

    time.sleep(3) #等待获取位置

    Wapat_button = driver.find_element_by_class_name("wapat-btn-box") 
    Wapat_button.click() #确认自动获取失败

    #手动输入
    # 使用xpath定位方式获取select页面元素对象：省份
    select_element = Select(driver.find_element_by_xpath("//select[@class='hcqbtn hcqbtn-danger']"))
    # print select_element.first_selected_option.text # 打印默认选中项的文本

    # 获取所有选择项的页面元素对象
    all_options = select_element.options
    # 打印选项总个数
    # print len(all_options)
    # print all_options[2].text #查看第三个选项的文本
    # print all_options[2].get_attribute("value") #第三个选项的value

    '''
    is_enabled()：判断元素是否可操作
    is_selected()：判断元素是否被选中
    '''
    if all_options[1].is_enabled() and not all_options[1].is_selected():
        select_element.select_by_value(Province) #选择省份

  # 使用xpath定位方式获取select页面元素对象：城市
    select_element = Select(driver.find_element_by_xpath("//select[@class='hcqbtn hcqbtn-warning']"))
    # 获取所有选择项的页面元素对象
    all_options = select_element.options
    # print all_options[2].text #查看第三个选项的文本

    if all_options[1].is_enabled() and not all_options[1].is_selected():
        select_element.select_by_value(City) #选择城市

  # 使用xpath定位方式获取select页面元素对象：村镇
    select_element = Select(driver.find_element_by_xpath("//select[@class='hcqbtn hcqbtn-primary']"))
    # 获取所有选择项的页面元素对象
    all_options = select_element.options
    # print all_options[2].text #查看第三个选项的文本

    if all_options[1].is_enabled() and not all_options[1].is_selected():
        select_element.select_by_value(Village) #选择村镇
    #-------------------------------------------------------------------------------------
    # 2) 单选题
    # 2.01-今日是否在校
    sfzx_btn = driver.find_element_by_xpath("//div[@name='sfzx']/div/div[1]") #今日是否在校：是
    print "今日是否在校: "
    print sfzx_btn.text
    # print sfzx_btn.get_attribute('innerHTML') # 内部所有内容
    sfzx_btn.click()
    time.sleep(0.5) #等待

    # 2.02-是否危险地区返回杭州
    jrdqtlqk_btn = driver.find_element_by_xpath("//div[@name='jrdqtlqk']/div/div[9]") #危险地区返回：否
    print "是否危险地区返回: "
    print jrdqtlqk_btn.text
    # 获取jrdqtlqk_btn/span元素class属性值
    act = driver.find_element_by_xpath("//div[@name='jrdqtlqk']/div/div[9]/span").get_attribute('class')
    # 判断classs属性值是否为active
    if not (act == "active"):
        print '重新点击'
        jrdqtlqk_btn.click()
    elif (act == "active"):
        print '已经点击'  
    time.sleep(0.5) #等待 

    # 2.1-是否申请健康码及状态
    sfsqhzjkk_btn = driver.find_element_by_xpath("//div[@name='sfsqhzjkk']/div/div[1]") #是否已申请健康码：是
    print "是否已申请健康码: "
    print sfsqhzjkk_btn.text
    sfsqhzjkk_btn.click()
    time.sleep(0.5) #等待
 
    # 2.2-健康码颜色
    sqhzjkkys_btn = driver.find_element_by_xpath("//div[@name='sqhzjkkys']/div/div[1]") #健康码颜色：绿色
    print "健康码颜色："
    print sqhzjkkys_btn.text
    sqhzjkkys_btn.click()
    time.sleep(0.5) #等待
 
    # 2.3-境外返回
    sfymqjczrj_btn = driver.find_element_by_xpath("//div[@name='sfymqjczrj']/div/div[2]") #境外返回：否
    print "境外返回： "
    print sfymqjczrj_btn.text
    sfymqjczrj_btn.click()
    time.sleep(0.5) #等待
 
    # 2.4-本人承诺信息准确
    sfqrxxss_btn = driver.find_element_by_xpath("//div[@name='sfqrxxss']/div/div") #本人承诺
    print "确认承诺: "
    print sfqrxxss_btn.text
    sfqrxxss_btn.click()
    time.sleep(0.5) #等待
   #-------------------------------------------------------------------------------------
   # 3)-提交信息
    # submit_btn = driver.find_element_by_xpath("//div[@class='list_box']/div[@class='footers']") #提交信息
    submit_btn = driver.find_element_by_class_name("footers") 
    print "提交信息: "
    print submit_btn.text
    submit_btn.click()
    time.sleep(0.5) #等待

    # 确认提交
    conform_btn = driver.find_element_by_xpath("//div[@class='wapcf-btn-box']/div[2]") #确认提交：是
    # print "确认提交: "
    print conform_btn.text
    conform_btn.click()
    time.sleep(0.5) #等待
        
    # 4)-确认提交成功
    success_btn = driver.find_element_by_xpath("//div[@class='alert']/div") #提交成功
    print "提交成功: "
    print success_btn.text
    success_btn.click()    

   #-------------------------------------------------------------------------------------
    print 'Success Submit info.'
# =============================================================================================

#
if __name__ == '__main__':

    # 1-登录每日健康申报
    url = 'https://healthreport.zju.edu.cn/ncov/wap/default/index'
    
    # 浙大通行证
    zju_username =  'xxxxx'
    zju_password = 'xxxxxx'

    driver = LoginZJU(url, zju_username, zju_password)

    # 2-填写每日健康上报内容
    # 1)-Your Location
    Province = "浙江省"
    City = "杭州市"
    Village = "西湖区"
    # 2)-必选单选题
    # 3)-提交信息
    SetInfo(driver, Province, City, Village)


    print '----------------Finish !---------------'