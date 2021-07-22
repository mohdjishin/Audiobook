import pyttsx3
import PyPDF2
def read():
    a = int(input("enter page number:"))
    b = (a - 1)
    file = str(input("path to your pdf file:"))
    book = open(file, "rb")
    pdfreader = PyPDF2.PdfFileReader(book)
    pages = pdfreader.numPages
    print("total pages:", pages)
    speaker = pyttsx3.init()
    voices = speaker.getProperty("voices")
    speaker.setProperty("voice", voices[1].id)
    for num in (b, pages):
        page = pdfreader.getPage(b)
        text = page.extractText()
        speaker.say(text)
        print("Reading..")
        speaker.runAndWait()

read()