from django.shortcuts import render
from django.utils.html import escape
from django.http import HttpResponse
from selenium import webdriver
import lxml.html
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Bot(request):
    if request.method == "POST":
            url = request.POST.get('url')

            xpath_title = request.POST.get('xpath_title')

            xpath_des = request.POST.get('xpath_des')

            xpath_dur = request.POST.get('xpath_dur')

            xpath_intake = request.POST.get('xpath_intake')

            xpath_tui_fee = request.POST.get('xpath_tui_fee')


           
            driver = webdriver.Chrome(executable_path="C:\\Users\\ASUS\\Desktop\\drivers\\chromedriver.exe")
            driver.get(url)
         

            print(xpath_title)
            links = driver.find_element(By.XPATH, xpath_title).text
            print("data: ", links)



            data_des = driver.find_element(By.XPATH,xpath_des)
            data_des1 = data_des.get_attribute("outerHTML")
            print("Data in Html format",data_des1)


            data_dur = driver.find_element(By.XPATH,xpath_dur).text
            print("Duration of program", data_dur)


            data_intake = driver.find_element(By.XPATH, xpath_intake).text
            print("program intake ", data_intake)


            data_tui_fee = driver.find_element(By.XPATH, xpath_tui_fee).text
            print("program fee ", data_tui_fee)


            context={"links":links , "data_des1":data_des1, "data_dur":data_dur, "data_intake":data_intake, "data_tui_fee":data_tui_fee }
            return render(request,'result.html', context)
    else:
            return render(request, 'index.html')












//*[contains(@class,'media-body content')]//a/@href/ancestor::div//div[@class='']











{% if links %}
<h2>This is Title of Program </h2>
<hr>

{{links}}

<br>
<hr>
<br>
<h2>Description of "Program"</h2>
<hr>

{{data_des1}}

<hr>
<br>
<h2>Duration of Program</h2>
<hr>
{{data_dur}}

<hr>
<br>
<h2>Intake of Program</h2>
<hr>
{{data_intake}}

<hr>
<br>
<h2>Tuition fee of Program</h2>
<hr>
{{data_tui_fee}}


{% endif %} 