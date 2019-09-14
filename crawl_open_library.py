import xlrd
import time
import requests
import shutil
import urllib.request

workbook = xlrd.open_workbook('stock_inventory.xls')
worksheet = workbook.sheet_by_name('Stock Inventory')

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

for i in range(61, 2556):
    isbn = worksheet.cell(i,8).value
    number = int(worksheet.cell(i,0).value)
    print('Downloading '+str(number)+'.jpg')
    url = 'http://covers.openlibrary.org/b/isbn/'+isbn+'-M'+'.jpg'
    try:
        res = requests.get(url, headers=headers)
        with open('images/'+str(number)+'.jpg', 'wb') as W:
            W.write(res.content)
    except:
        print('url not found')
    time.sleep(15)



