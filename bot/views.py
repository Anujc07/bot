from django.shortcuts import render
from django.utils.html import escape
from django.http import HttpResponse
from selenium import webdriver
import lxml.html
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def Bot(request):
    if request.method == "POST":
        url = request.POST.get('url')

        xpath_title = request.POST.get('xpath_title')

        xpath_des = request.POST.get('xpath_des')

        xpath_dur = request.POST.get('xpath_dur')

        xpath_intake = request.POST.get('xpath_intake')

        xpath_tui_fee = request.POST.get('xpath_tui_fee')


    


        driver = webdriver.Chrome(
            executable_path="C:\\Users\\ASUS\\Desktop\\drivers\\chromedriver.exe")
        driver.get(url)

        if xpath_title:
            print(xpath_title)
            links = driver.find_element(By.XPATH, xpath_title).text
            print("data: ", links)
        else:
            links = "No data"

        if xpath_des:
            print(xpath_des)
            data_des1 = driver.find_element(By.XPATH, xpath_des).get_attribute("outerHTML")
            # data_des1 = data_des.get_attribute("outerHTML")
            print("Data in Html format", data_des1)
        else:
            data_des1 = "No Data"

        if xpath_dur:
            print(xpath_dur)
            data_dur = driver.find_element(By.XPATH, xpath_dur).text
            print("Duration of program", data_dur)
        else:
            data_dur = "No Data"

        if xpath_intake:
            print(xpath_intake)
            data_intake = driver.find_element(By.XPATH, xpath_intake).text
            print("program intake ", data_intake)
        else:
            data_intake = "No Data"

        if xpath_tui_fee:
            print(xpath_tui_fee)
            data_tui_fee = driver.find_element(By.XPATH, xpath_tui_fee).text
            print("program fee ", data_tui_fee)
        else:
            data_tui_fee = "No Data"

        context = {"links": links, "xpath_ti":xpath_title , "data_des1": data_des1 , "xpath_desc":xpath_des , "data_dur": data_dur,
                   "xpath_dura":xpath_dur ,"data_intake": data_intake, "xpath_inta":xpath_intake ,"data_tui_fee": data_tui_fee,"xpath_tuition":xpath_tui_fee }
        return render(request, 'result.html', context)
    else:
        return render(request, 'index.html')


