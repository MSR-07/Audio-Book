import PyPDF2
import pyttsx3

# Read Specific PDF file
pdfReader = PyPDF2.PdfFileReader(open('----', 'rb'))

speaker = pyttsx3.init()

# Split Pages
for page_num in range(pdfReader.numPages):
    text = pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
# Stop Speaker
# speaker.stop()

# Save Audio Book
engine = pyttsx3.init()
engine.save_to_file(text, '------')
engine.runAndWait()
