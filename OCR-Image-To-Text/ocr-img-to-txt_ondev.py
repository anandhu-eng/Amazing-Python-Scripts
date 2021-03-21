import pytesseract
from PIL import Image
import cv2

# path to the Tessaract
pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"


def convert():
    img = Image.open(r"Sample-interview-quotes.png")
    text = pytesseract.image_to_string(img)
    list_text=list(text.split("\n"))
    
    print(list_text)


convert()

#the file has been saved upto a stage where it can display the words that are in a line and ignoring the other blank lines.
