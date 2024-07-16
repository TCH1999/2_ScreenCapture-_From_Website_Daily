# Screen Capture README Documentation

This documentation provides an overview and usage instructions for the "Screen Capture" program, which captures screenshots from a website and saves them in a target location organized by the current date.

## Program Overview

The "Screen Capture" program is designed to automate the process of capturing screenshots from a website and organizing them in a specific folder structure based on the current date. The program utilizes the Selenium library to interact with a web browser and capture the screenshots.

## Prerequisites

Before running the program, ensure that the following requirements are met:

1. **Python**: The program requires Python to be installed on your system.
2. **Python libraries**: Install the required libraries by running the following command:
pip3 install selenium pillow

livecodeserver
Copy
3. **Chrome WebDriver**: Download and install the Chrome WebDriver from the official website downloads. Make sure to choose the appropriate version based on your installed Chrome browser version.

## Usage Instructions

Follow the steps below to use the "Screen Capture" program:

1. Clone or download the program files from the repository.
2. Open a terminal or command prompt and navigate to the program directory.
3. Install the required Python libraries by running the following command:
pip install selenium pillow

livecodeserver
Copy
4. Download and install the Chrome WebDriver from the official website
5. Update the program code with the necessary configurations:
- Modify the `folder_path` variable to specify the target location where the screenshots will be saved.
- Adjust any other relevant parameters based on your requirements (e.g., screenshot file name format, website URL).
6. Save the code changes and execute the program by running the following command:
python screen_capture.py

livecodeserver
Copy

Upon execution, the program will perform the following tasks:

1. Create a folder with the current date in the specified `folder_path`.
2. Capture screenshots from the specified website for all stages (1 to 11).
3. Save the screenshots in the created folder with appropriate file names.
4. Display the current date in the console.
5. Show a message box indicating that the process is finished.

Please note that the program is designed to capture screenshots from a specific website URL. If you need to capture screenshots from a different website or adjust any other parameters, modify the relevant parts of the code accordingly.

## Conclusion

The "Screen Capture" program simplifies the process of capturing screenshots from a website and organizing them based on the current date. It utilizes the Selenium library and Chrome WebDriver to automate the screenshot capture process. By following the usage instructions provided in this documentation, you can easily capture and save screenshots from the desired website.