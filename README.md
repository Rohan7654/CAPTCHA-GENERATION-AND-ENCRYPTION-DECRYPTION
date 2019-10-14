# CAPTCHA-GENERATION-AND-ENCRYPTION-DECRYPTION

# CAPTCHA GENERATION
CAPTCHA is an image that contains alphanumeric value. CAPTCHA can be generated in diﬀerent ways, here we've used a popular libraray in python 
for creation of CAPTCHA image. Firstly create blank image. Select alphanumeric value randomly that are in an array previously. 
Write selected values on the blank image. Add some distortion or noise to it which makes diﬃcult to identify values. 
Now an image is ready that we call as CAPTCHA.

# CAPTCHA ENC/DEC
CAPTCHA that is generated will be in image format. 
CAPTCHA encryption is a process of encrypting an image using a key generated using BBS algorithm (128 bit key is generated which passed all of the 15 NIST tests). 
For encryption there is number of algorithms/techinques. 
But here we used some simple techniques like altering pixel position, pixel value and XORing the pixel value with key. 
At ﬁrst image is selected an divided into block of each with 64 pixels. 
Pixel value inversion based on key value and changing pixel position according to key value is applied to the blocks alternatively. 
Then by selecting each pixel and converting pixel into bits format, bit-xor operation is done between pixel value and key value.
Similarly decryption is done using same operations as mentioned above in encryption.
