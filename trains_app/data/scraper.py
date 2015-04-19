import requests
from scrapy.selector import HtmlXPathSelector
import re, sys, json

pnr = sys.argv[1]

res = requests.post( 'http://www.getpnrstatus.co.in?pnrno=' + str(pnr) )
page = res.text.encode('utf8')

sel = HtmlXPathSelector( text = page )
#response = Selector( text = page )
p = sel.select('//td/text()').extract()
#p = response.xpath('//td/text()').extract()

train_num = p[1].strip()
res = requests.get('http://runningstatus.in/status/'+train_num+'-today')
page = res.text.encode('utf8')

sel = HtmlXPathSelector( text = page)
#response = Selector( text = mypage )

train_list = []
for row in sel.select('//tbody/tr'):
	col = row.select('.//td/text()').extract()
	train_list.append(str(re.search(r'(.*)[(]',col[0]).group(1)))

train_file = open("train_route_mod.txt", "w+");
train_file.write(json.dumps(train_list))
train_file.close()

#print(json.dumps(train_list))
#print(train_list)

#pnr = 4519282568
