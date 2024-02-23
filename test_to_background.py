# ************************************** These codes are old
# import winreg, ctypes, win32con
# from PIL import Image
# import requests
# import shutil
# import os
# import json

# url = "https://api.nasa.gov/planetary/apod"
# api_key = "3lnc7Eg8WQ2lju6IpP9YocCJQHsXMczTuw5RS4Pu"

# params = {
#     "api_key": api_key
# }

# response = requests.get(url, params=params)

# if response.status_code == 200:
#     data = response.json()
#     image_url = data["url"]
    
#     # Download the image
#     image_response = requests.get(image_url, stream=True)
#     if image_response.status_code == 200:
#         with open("c:/My_Projects/python_dars/apod.jpg", "wb") as file:
#             image_response.raw.decode_content = True
#             shutil.copyfileobj(image_response.raw, file)
# else:
#     print("API request failed with status code:", response.status_code)


# im = Image.open('apod.jpg').convert("RGB")
# im.save("apod.bmp", "bmp")
# os.remove("c:/My_Projects/python_dars/apod.jpg")
# FILL,FIT,STRETCH,TILE,CENTER,SPAN = 0,1,2,3,4,5
# MODES = (0,10),(0,6),(0,2),(1,0),(0,0),(0,22)
# value1,value2 = MODES[FILL] # choose mode here

# key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Control Panel\Desktop", 0, winreg.KEY_WRITE)
# winreg.SetValueEx(key, "TileWallpaper", 0, winreg.REG_SZ, str(value1))
# winreg.SetValueEx(key, "WallpaperStyle", 0, winreg.REG_SZ, str(value2))
# winreg.CloseKey(key)

# def setWallpaper(path):
#     changed = win32con.SPIF_UPDATEINIFILE | win32con.SPIF_SENDCHANGE
#     ctypes.windll.user32.SystemParametersInfoW(win32con.SPI_SETDESKWALLPAPER,0,path,changed)


# setWallpaper("c:/My_Projects/python_dars/apod.bmp")
# ************************************************* 


import winreg, ctypes, win32con
from PIL import Image
import speech_recognition as sr
import pyttsx3
import requests
from chatgpt_use import chatgpt_connection
import shutil
import os
import json
from deep_translator import GoogleTranslator
from dalle_image_downloader import get_image_from_dall_e

def speak(text):
    """Speaks the given text using pyttsx3."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    """Downloads and sets a new background image based on user prompt."""
    speak("What image do you want to set to your background? Describe it!")
    image_prompt = input("> ")
    generated_image_path = get_image_from_dall_e(image_prompt)

    try:
        im = Image.open(generated_image_path).convert("RGB")
        screen_width = 1920
        screen_height = 1080
        im = im.resize((screen_width, screen_height))
        im.save("c:/My_Projects/python_dars/dall-e_1.bmp", "bmp")
        os.remove(generated_image_path)

        FILL, FIT, STRETCH, TILE, CENTER, SPAN = 0, 1, 2, 3, 4, 5
        MODES = (0, 10), (0, 6), (0, 2), (1, 0), (0, 0), (0, 22)
        value1, value2 = MODES[FILL]

        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Control Panel\Desktop", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "TileWallpaper", 0, winreg.REG_SZ, str(value1))
        winreg.SetValueEx(key, "WallpaperStyle", 0, winreg.REG_SZ, str(value2))
        winreg.CloseKey(key)

        setWallpaper("c:/My_Projects/python_dars/dall-e_1.bmp")

        speak("Background image updated successfully!")
    except Exception as e:
        speak("An error occurred during background update:")
        print(e)

def setWallpaper(path):
    changed = win32con.SPIF_UPDATEINIFILE | win32con.SPIF_SENDCHANGE
    ctypes.windll.user32.SystemParametersInfoW(win32con.SPI_SETDESKWALLPAPER, 0, path, changed)

# Initialize the recognizer
# recognizer = sr.Recognizer()

# while True:
#     print("Listening...")
#     with sr.Microphone() as source:
#         audio = recognizer.listen(source)

    # try:

        # Use Google Speech Recognition for accuracy
text = input("Enter a prompt: ")


# Check for specific phrases (case-insensitive)
if GoogleTranslator(source='auto', target='en').translate(text.lower()) in ("update the background", "update the image", "change the background", "change the image"):
    main()
else:
    print(chatgpt_connection(text.lower()))

    # except sr.UnknownValueError:
    #     speak("Could not understand audio. Please try again.")
    # except sr.RequestError as e:
    #     speak("Could not request results from Google Speech Recognition service:")
    #     print(e)
    # except Exception as e:
    #     speak("An unknown error occurred. Please try again later.")
    #     print(e)


