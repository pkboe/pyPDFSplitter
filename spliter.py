import PyPDF2
pdfReader = PyPDF2.PdfReader("./hallTickets.pdf")
pdfWriter = PyPDF2.PdfFileWriter()
examDate = '12-Aug-2022'
examTime = '10:15'
# check each document of the pdfFile contains "12-Aug-2022, if yes then append the page into new pdf file"
for pageNum in range(pdfReader.numPages):
    print(pdfReader.numPages)

    pageObj = pdfReader.getPage(pageNum)
    pageText = pageObj.extractText()
    if examDate in pageText and examTime in pageText:
        pdfWriter.addPage(pageObj)
        print("Page {} is added to new pdf file".format(pageNum))
        # write the new pdf file
        with open(examDate+'-'+examTime.replace(':','-')+'.pdf', 'wb') as newPdfFile:
            pdfWriter.write(newPdfFile)
            print("New pdf file is created")
            newPdfFile.close()
    else:
        print("Page {} is not added to new pdf file".format(pageNum))
        continue
print("Program is completed")

