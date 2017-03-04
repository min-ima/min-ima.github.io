import os,io,sys,re
from lxml import etree
import xml.dom.minidom

# captions = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
oneliners_true_chron = open("oneline/_oneliners.txt","r", encoding='utf-8')
index = 0
chron_dict = {}

for line in oneliners_true_chron:
	index += 1
	key = re.findall('.+?:',line)[0]
	caption = line.replace(key,'')
	chron_dict[key[:-1]] = [caption.strip(),str(index)]


html = etree.Element("html")
head = etree.SubElement(html, "head")
head.append(etree.Element("meta", name="viewport", content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"))
head.append(etree.Element("link" ,rel="stylesheet", type="text/css" ,href="minima.css"))
head.append(etree.Element("title"))
head[2].text = "MIN-IMA | oneliners"

body = etree.SubElement(html,"body")
templist = []
for subdir, dirs, files in os.walk("oneline/posts"):
	for oneline in files:
		name = oneline[:-4]
		try:
			cap = chron_dict[name]
		except KeyError:
			continue

		div = etree.Element("div",id=chron_dict[name][1], name="oneline")
		text = etree.Element("div",name = "textbox")
		t = etree.Element("div",name="title")
		t.text = name
		caption = etree.Element("div",name="caption")
		caption.text = chron_dict[name][0]
		text.append(t)
		text.append(caption)
		temp="background-image:url('oneline/posts/"+oneline+"')"
		imgDiv = etree.Element("div",name="image",id="overlay", style=temp)
		imgDiv.text=' '
		div.append(text)
		div.append(imgDiv)
		div.append(etree.Element("hr"))
		# div.append(caption)
		templist.append((div, chron_dict[name][1]))
		# body.append(div)
		# body.append(etree.Element("hr"))


templist_sorted = sorted(templist,key=lambda x: int(x[1]))

for div in templist_sorted:
	body.append(div[0])
	# body.append(etree.Element("hr", style="width:60vmin;"))



final = etree.ElementTree(html)
final.write('oneliners_temp.html')
xml = xml.dom.minidom.parse('oneliners_temp.html')
pretty = xml.toprettyxml()
final_pretty = open('oneliners.html','w')
final_pretty.write(pretty)
final_pretty.close() 