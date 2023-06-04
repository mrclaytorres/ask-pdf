# ask-pdf

This Python script automates AskYourPDF.com and retrieves PDF IDs in bulk. It uses Selenium and AutoIt to simulate file uploading. This script only runs in Windows since it uses AutoIt to interact with the GUI on file upload.

## Requirements
1. [Selenium](https://selenium-python.readthedocs.io/)  

2. AutoIT
- [AutoIt Docs](https://www.autoitscript.com/site/)
- [Selenium with AutoIt Tutorial](https://www.youtube.com/watch?v=3nPFjfpDwGU)

3. [Chrome Webdriver](https://chromedriver.chromium.org/) - Check the version of your Google Chrome and download the appropriate version and save it on your project root folder.

## Install Dependencies
`$ pip install -r requriements.txt`

## Required Folders
You need to create these folders (if not yet present) as they are required by the script.  
- /pdf - This is where you store your PDF files
- /uploads - This is where PDF moves when they are `READY FOR UPLOAD`
- /uploaded - This is where PDF moves when they are `ALREADY UPLOADED`
- /csvfiles - This is where the list of PDF IDs output file in csv format

## .au3 Changes
You will need to change some lines in the .au3 files before compiling them. Look for `PATH-TO-YOUR-PROJECT-ROOT` and change them to your appropriate project root folder. Once change, you will need to compile them.
##### move_file.au3
- Line `4` and `24`  
##### upload_pdf.au3  
- Line `4`, `26`, and `30`

*Note: Check out the Selenium with AutoIt Tutorial to know how to compile these files.*

## User-agent
The user Agent header has a particular string that provides the network protocol along with the details of operating system, software version, application, and so on.  
- Create a `user_agents.csv` file. Just copy the user-agents list here and save in column A: [User-Agents For Web](https://brightdata.com/blog/how-tos/user-agents-for-web-scraping-101)

## Run the Script
`$ python ask.py`  

*Note: Make sure you have PDF files in you `/pdf` folder, or your script run will fail.*