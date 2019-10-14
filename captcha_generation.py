from captcha.image import ImageCaptcha
from captcha_new import Claptcha
import CAPTCHA_ENCRY as enc
import random
import cv2
number_list = ['0','1','2','3','4','5','6','7','8','9']
alphabet_lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet_uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def createtext(captcha_string_size):
    captcha_string_list = []
    base_char = alphabet_lowercase + alphabet_uppercase + number_list
    for i in range(captcha_string_size):
        char = random.choice(base_char)
        captcha_string_list.append(char)
    captcha_string = ''   
    for item in captcha_string_list:
        captcha_string += str(item)
    return captcha_string
def create_image_captcha(captcha_text):
    c = Claptcha(captcha_text, "BLUELINES.ttf")
    text,image=c.image
    image_captcha = ImageCaptcha()
    image = image_captcha.generate_image(text)
    image_captcha.create_noise_curve(image, image.getcolors())
    image_captcha.create_noise_dots(image, image.getcolors())
    image_file = "./captcha_"+ ".png"
    image_captcha.write(captcha_text, image_file)
    img=cv2.imread(image_file)
    enc.CAPTHA_ENCRY.encry(img)
    cv2.imshow('out',img)
    print("done") 
if __name__ == '__main__':
    captcha_text = createtext(5)
    create_image_captcha(captcha_text)
