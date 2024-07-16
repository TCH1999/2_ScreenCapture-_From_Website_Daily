import os
import time
import sys
from PIL import Image
from datetime import date

"""Program : Screen Capture from website and save in target location and organize with current date folder"""
# Writer : Chiron
# Date : 16/07/2024
# it can be combine with task scheduler in window to perform daily screencap task on target website

sys.path.append("C:/Users/Switc/miniconda3/Lib/site-packages")                       # Change pt 1: change to python library installation location
from selenium import webdriver
import tkinter as tk
from tkinter import messagebox

def create_folder(folder_path, target_date):
    """Create a folder in the specified path"""
    folder_name = os.path.join(folder_path, target_date)                            # Change pt 2: create a folder named by today 's date
    os.makedirs(folder_name, exist_ok=True)                                          
    return folder_name

def take_screenshot(url, folder_path, target_date, i):
    """Take a screenshot of the webpage and save it to the specified folder"""
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    screenshot_file_name = f"{target_date}_Screencapture{i}.png"                      # Change pt 3: The output name can be change
    screenshot_path = os.path.join(folder_path, target_date, screenshot_file_name)
    driver.save_screenshot(screenshot_path)
    driver.quit()
    return screenshot_path

def capture_screenshots(url,folder_path, target_date):                               # Change pt 4: if website URL have more than 1 , it can be adjust
    """Capture screenshots for all NO."""
    for i in range(11, 0, -1):
        url = f"https://XXX.com/date={target_date}&no={i}"                           # Change pt 5: Target URL
        take_screenshot(url, folder_path, target_date, i)

def main(url,debug):
    folder_path = "C:/User/../"                                                      # Change pt 6: Output location
    current_date = date.today()
    target_date = current_date.strftime("%Y-%m-%d")

    create_folder(folder_path, target_date)

    if debug: print("Today Date:", current_date)

    capture_screenshots(url,folder_path, target_date)

    if debug: print("Process is finished")
    messagebox.showinfo("Information", "The Process is finished!")

if __name__ == "__main__":
   debug = True
   main(debug)