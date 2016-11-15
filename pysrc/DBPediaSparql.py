from SPARQLWrapper import SPARQLWrapper, JSON
import xml.etree.ElementTree as Et

def mainul():
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")

    et = Et.parse('../src/main/resources/nlp.xml')
    root = et.getroot()

    for child_of_root in root:
        print(child_of_root.tag, child_of_root.text)

        horse = (child_of_root.text)
        tempor=''


        for c in horse:
            if c!=' ':
                tempor=tempor+c


        sparql.setQuery("""
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX dbo: <http://dbpedia.org/ontology/>
            SELECT ?label
            WHERE { <http://dbpedia.org/resource/"""+tempor+"""> dbo:class  ?label }
        """)

        # JSON example
        sparql.setReturnFormat(JSON)

        results = sparql.query().convert()
        dbpedia=''
        for result in results["results"]["bindings"]:
            dbpedia=str(result["label"]["value"])
            print(dbpedia)
        if dbpedia:
            child_of_root.attrib['CLASS'] = str(dbpedia)
            print(str(dbpedia))
            et.write('../src/main/resources/nlp-out.xml')
    return
mainul()