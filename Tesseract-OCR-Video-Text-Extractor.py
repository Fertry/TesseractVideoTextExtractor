from PIL import Image
import pytesseract
import os
import cv2 as cv

# Tesseract-OCR installation path:
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'


def files(video):

    src_vid = cv.VideoCapture(1)
    src_vid = cv.VideoCapture(video)
    return(src_vid)


def process(video, directory):

    index = 0
    print("Processing...")
    
    # While videos is open:
    while video.isOpened():
        ret, frame = video.read()
        # cv.imshow('Video', frame)
        if not ret:
            break

        name = directory + str(index) + '.png'

        # Each 300 frames:
        if index % 300 == 0:
            print('Extracting frame... ' + name)
            cv.imwrite(name, frame)
            rescale(name)
        
        index += 1
        # Manually stop when pressing 'E' key:
        if cv.waitKey(1) & 0xFF == ord('E'):
            print("Manually stopped")
            break

    video.release()
    cv.destroyAllWindows()

# Rescale the frame:
def rescale(name):

    # open = cv.imread(name)
    # openResized = open[-1080:-700, -1920:300]   
    # cv.imwrite(name, openResized)

    get_text(name)


def get_text(image):
    
    # Define language for Tesseract-OCR:
    text = pytesseract.image_to_string(image, lang='eng')
    print(text)


if __name__ == '__main__':
    
    print("Starting...")
    directory = input("Enter directory for frames storage: ")
    video = input("Enter video path: ")

    vid = files(video)
    process(vid, directory)
   