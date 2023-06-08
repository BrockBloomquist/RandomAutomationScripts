import pyttsx3, PyPDF2

pdfreader = PyPDF2.PdfFileReader(open("book.pdf", "rb"))
speaker = pyttsx3.init()
for page_num in range(pdfreader.numPages):
    text = pdfreader.getPage(page_num).extractText()
    clean_text = txt.strip().replace("\n", " ")
    print(clean_text)

speaker.save_to_file(clean_text, "story.mp3")
