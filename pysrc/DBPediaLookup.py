import urllib.request
import xml.etree.ElementTree as Et

def word(s):
    first=0 # 0 no, 1 yes
    tempor=''
    s=' '.join(s.split())
    for i in range(0,len(s)):
        if s[i] != ' ' and first==0 :
           # tempor = tempor + str(s[i]).upper()
            t="".join(s[i].upper())
            tempor = tempor + t
            first = 1
        elif s[i]!=' ' and s[i-1]==' ' and first==0 :
            #tempor = tempor + str(s[i]).upper()
            t = "".join(s[i].upper())
            tempor = tempor + t
            first = 1
        elif s[i]==' ' and s[i-1]!=' ' and first==1 and i<len(s)-1:
            tempor = tempor + '_'
        elif s[i]!=' ' and first==1 :
            tempor = tempor + s[i]
    return(tempor)

def main():
	page = urllib.request.urlopen('http://lookup.dbpedia.org/api/search/KeywordSearch?QueryString=relationship')
	et = Et.parse(page)

	root = et.getroot()

	for child_of_root in root:
		print(child_of_root.tag)
		print(child_of_root[0].text)
	#	rootWord = (child_of_root.text)
	#	for child in child_of_root:
	#		for child2 in child:
	#			print(child2.text)
	
	return