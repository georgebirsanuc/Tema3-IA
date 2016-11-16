# Tema3-IA
Citiți un text  (in limba engleza)  dintr - un fișier .txt. Segmentați textul în cuvinte (separați  inclusiv semnele de punctuați e) folosind  API - ul Stanford. Marcați cu eticheta <word> fiecare cuvint. 
Pentru cuvintele care pot fi identificate în DBpedia, adăugați fiecărei etichete <word> un atribut „class” care să aibă ca valoare categoria (clasa) identificată pentru cuvantul respectiv in DBPedia (de ex. pentru cuvantul România clasa country). Outputul trebuie sa fie un XML valid.

# Requirements
- JDK 1.8
- Python 3
- Eclipse
- Internet connection

# Usage

- the input file must be src/main/resources/sample-content.txt or change the path for the inputFile in src/main/java/tema3/SplitToWords.java
- run SplitToWords.java
- the output file can be found in src/main/resources/nlp.xml
- run pysrc/DBPediaSparql.py (open cmd, go to pysrc folder, enter the command python DBPediaSparql.py (must have Python in enviroment variables))
- the final output file is src/main/resources/nlp.xml
