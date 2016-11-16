from SPARQLWrapper import SPARQLWrapper, JSON
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

def sparqlQuerry (sparql, tempor):
    sparql.setQuery("""
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                PREFIX dbo: <http://dbpedia.org/ontology/>
                SELECT ?label
                WHERE { <http://dbpedia.org/resource/""" + tempor + """> rdf:type  ?label }
            """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    return results

def mergeTags(et, root, i, j):
    tagContent = ''
    for k in range(i, i + j):
        tagContent += root[k].text + ' '

    for k in range(i + 1, i + j):
        root.remove(root[k])
    root[i].text = tagContent;
    et.write('../src/main/resources/nlp.xml')
    return

def mainul():
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")

    et = Et.parse('../src/main/resources/nlp.xml')
    root = et.getroot()

    for i in range(0, len(root) - 1):
        rootWord = (root[i].text)

        # TO DO check multiple words
        j = 0
        expression = root[i].text
        oldExpresseion = ""
        while j <= 3:
            j += 1
            expression += " " + root[i + j].text
            # print("### EXPRESSTION: " + word(expression))
            resultss = sparqlQuerry(sparql, word(expression))
            try:
                a = str(resultss["results"]["bindings"][0])
            except IndexError:
                continue
            oldExpresseion = expression

        if (oldExpresseion != ''):
            print(oldExpresseion, i, j)
        if (rootWord != oldExpresseion):
            mergeTags(et, root, i, j)
        # rootWord = oldExpresseion

        tempor = word(rootWord)

        results = sparqlQuerry(sparql, tempor)

        # print(tempor)

        dbpedia=''
        for result in results["results"]["bindings"]:
            #print(result)
            
            dbpedia=str(result["label"]["value"])
            if dbpedia and "umbel" in dbpedia:
             #   print(dbpedia)
                break
            #print(dbpedia)
            
        if dbpedia:
            root[i].attrib['class'] = str(dbpedia[dbpedia.rfind('/') + 1:])
            et.write('../src/main/resources/nlp.xml')

et = Et.parse('../src/main/resources/nlp.xml')
mergeTags(et, et.getroot(), 0, 4)
