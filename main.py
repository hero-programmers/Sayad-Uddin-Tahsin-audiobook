import pyttsx3
import PyPDF2
import os.path

name = str(input("Enter the PDF Name\n>>> "))
if not os.path.exists(name):
    raise FileNotFoundError(f"{name} not found!")

from_page = int(input("Enter the Page Number where it'll start reading\n>>> "))
book = open(name, 'rb')
pdfReader = PyPDF2.PdfReader(book)
pages = len(pdfReader.pages)
if from_page > pages:
    raise IndexError("Page Number is greater than the total page number!")

to_page = int(input("Enter the Page Number where it'll end reading (0 for Last Page)\n>>> "))
if to_page == 0:
    pass
else:
    pages = to_page
if to_page > pages:
    raise IndexError("Page Number is greater than the total page number!")

print(pages)
speaker = pyttsx3.init()
speaker.setProperty('rate', 150)
voice = speaker.getProperty('voices')
speaker.setProperty('voice', voice[1].id)

for i in range(from_page, pages):
    page = pdfReader.pages[i]
    text = str(page.extract_text()).strip()
    speaker.say(text)
    speaker.runAndWait()
