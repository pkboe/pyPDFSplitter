import PyPDF2

def pdfCSVSplitter(filePath, keys):
    pdfReader = PyPDF2.PdfReader(filePath)
    pdfWriter = PyPDF2.PdfFileWriter()
    # examDate = '12-Aug-2022'
    # examTime = '10:15'
    # check each document of the pdfFile contains "12-Aug-2022, if yes then append the page into new pdf file"
    for pageNum in range(pdfReader.numPages):
        print(pdfReader.numPages)

        pageObj = pdfReader.getPage(pageNum)
        pageText = pageObj.extractText()
        # if each key in keys array is found in the pageText then append the page into new pdf file
        for key in keys:
            if key in pageText:
                pdfWriter.addPage(pageObj)
                with open(key+'.pdf', 'wb') as newPdfFile:
                    pdfWriter.write(newPdfFile)
                    print("New pdf file is created")
                    newPdfFile.close()
                
    #     if examDate in pageText and examTime in pageText:
    #         pdfWriter.addPage(pageObj)
    #         print("Page {} is added to new pdf file".format(pageNum))
    #         # write the new pdf file
            # with open(examDate+'-'+examTime.replace(':','-')+'.pdf', 'wb') as newPdfFile:
            #     pdfWriter.write(newPdfFile)
            #     print("New pdf file is created")
            #     newPdfFile.close()
    #     else:
    #         print("Page {} is not added to new pdf file".format(pageNum))
    #         continue
    # print("Program is completed")

def pdfADDSplitter(filePath, keys):
    pdfReader = PyPDF2.PdfReader(filePath)
    pdfWriter = PyPDF2.PdfFileWriter()

    for pageNum in range(pdfReader.numPages):
        print(pdfReader.numPages)
        pageObj = pdfReader.getPage(pageNum)
        pageText = pageObj.extractText()
        # if each key in keys array is found in the pageText then append the page into new pdf file
        # 
                
    #     if examDate in pageText and examTime in pageText:
    #         pdfWriter.addPage(pageObj)
    #         print("Page {} is added to new pdf file".format(pageNum))
    #         # write the new pdf file
            # with open(examDate+'-'+examTime.replace(':','-')+'.pdf', 'wb') as newPdfFile:
            #     pdfWriter.write(newPdfFile)
            #     print("New pdf file is created")
            #     newPdfFile.close()
    #     else:
    #         print("Page {} is not added to new pdf file".format(pageNum))
    #         continue
    # print("Program is completed")