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

def mainul():
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")

    et = Et.parse('../src/main/resources/nlp.xml')
    root = et.getroot()

    for child_of_root in root:
        rootWord = (child_of_root.text)
        tempor=word(rootWord)
        sparql.setQuery("""
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX dbo: <http://dbpedia.org/ontology/>
            SELECT ?label
            WHERE { <http://dbpedia.org/resource/"""+tempor+"""> rdf:type  ?label }
        """)

        print(tempor)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        dbpedia=''
        for result in results["results"]["bindings"]:
            print(result)
            
            dbpedia=str(result["label"]["value"])
            if dbpedia and "umbel" in dbpedia:
                print(dbpedia)
                break
            print(dbpedia)
            
        if dbpedia:
            child_of_root.attrib['class'] = str(dbpedia[dbpedia.rfind('/') + 1:])
            et.write('../src/main/resources/nlp.xml')
mainul()

