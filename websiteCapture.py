import os
import time
import sys
from PIL import Image
import datetime
from datetime import date

sys.path.append("C:/Users/Switc/miniconda3/Lib/site-packages")                       # Change pt 1: install library location
from selenium import webdriver
import tkinter as tk
from tkinter import messagebox


def create_folder(folder_path, target_date):
    """Create a folder in the specified path"""
    folder_name = os.path.join(folder_path, target_date)                            # Change pt 2: create a folder named by today 's date
    os.makedirs(folder_name, exist_ok=True)                                          
    return folder_name

def take_screenshot(url, folder_path, target_date, i):
    """Take a screenshot of the webpage and save it to the specified folder"""l
    options = webdriver.ChromeOptions()
    options.add_argument(f"--window-size=900,900")  # Adjust the width and height as needed
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    time.sleep(5)
    screenshot_file_name = f"賽馬賠率-{target_date}_場次{i}.png"
    screenshot_path = os.path.join(folder_path, target_date, screenshot_file_name)
    driver.save_screenshot(screenshot_path)
    driver.quit()
    return screenshot_path

def capture_screenshots(folder_path, target_date):                                   # Change pt 4: if website URL have more than 1 , it can be adjust
    """Capture screenshots for all stages (1 to 11)"""
    for i in range(11, 0, -1):
        url = f"https://bet.hkjc.com/racing/pages/odds_wpq.aspx?lang=ch&date={target_date}&venue=ST&raceno={i}"
        take_screenshot(url, folder_path, target_date, i)

def main():
    folder_path = "G:\Mother\SynologyDrive\\4_Mum_個人\\6_JockeyClub"                # Change pt 5: Output location
    current_date = date.today()
    target_date = current_date.strftime("%Y-%m-%d")

    create_folder(folder_path, target_date)

    print("Today Date:", current_date)

    capture_screenshots(folder_path, target_date)

    print("Process is finished")
    messagebox.showinfo("Information", "The Process is finished!")

if __name__ == "__main__":
    file = open(r'G:\SynologyDrive\2_LifeGoalProject\2_programmingProject\1_python\3_codeProject\1_automation_Website_Capture\DAILY_WEBSITE_CAPTURE\taskLog','a')
    file.write(f'{datetime.datetime.now()} - The script ran \n')
    main()
    