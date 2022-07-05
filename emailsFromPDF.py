import PyPDF2
import re
import json

pdfFileObj = open("ACIC06092011.pdf", 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

numPages = pdfReader.getNumPages()

dictemail = {}

for pagina in range(0, numPages):
    pageObj = pdfReader.getPage(pagina)
    textExtract = pageObj.extractText()
    match = re.findall(r'[\w\.-]+@[\w\.-]+', textExtract)
    dictemail["pagina"+str(pagina+1)] = match
    
file = open('resultadoemails.txt', 'w')
json.dump(dictemail, file, indent = 6)
file.close()
