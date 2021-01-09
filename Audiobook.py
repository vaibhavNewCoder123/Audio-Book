import pyttsx3# to import it Type "pip install pyttsx3" in Terminal
import PyPDF2# to import it Type "pip install pypdf2" in Terminal

# It will convert our Text in pdf to a speech.
engine = pyttsx3.init()
book = open('Call of The Wild.pdf', 'rb')# import your pdf here which you want this program to read for you.
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

# to adjust the speed of the reader.
rate = engine.getProperty("rate")
engine.setProperty("rate",110) # more the value you will put the faster he will read.
engine.runAndWait()

# to adjust the volume of the reader.
volume = engine.getProperty("volume")
engine.setProperty("volume",0.3)


speaker = pyttsx3.init()
for num in range(7, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()# it will extract the text of the pdf to read.
    speaker.say(text)
    speaker.runAndWait()
    
    # coded By Vaibhav Krishna 
    # commercial use is Prohibited.
    # only for new learners.
