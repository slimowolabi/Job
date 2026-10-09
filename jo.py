#!/usr/bin/env python3

import time

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

def open_browser():
    driver = None

    try:
        driver = webdriver.Firefox()
        driver.get("https://www.facebook.com/")

        print(OKGREEN + "Firefox opened successfully." + ENDC)
        print(WARNING + "Log in manually in Firefox." + ENDC)

        input("After logging in, press Enter in Termux...")

        return driver

    except WebDriverException as error:
        print(FAIL + "Browser error: " + str(error) + ENDC)

        if driver is not None:
            driver.quit()

        return None




def help():
    print(OKBLUE + "start : Start the script." + ENDC)
    print(OKBLUE + "version : Version." + ENDC)
    print(OKBLUE + "exit : Exit." + ENDC)
    print(OKBLUE + "info : Info." + ENDC)
    print(OKBLUE + "clear : Clear console." + ENDC)
    print(OKBLUE + "help : This help message." + ENDC)


tool = "friends@py:~# "
n = "\n"


def start():
    driver = open_browser()

    if driver is None:
        return

    try:
        links = []

        print(OKGREEN + "\nEnter the Facebook profile links." + ENDC)
        print("Type DONE when you have entered all the links.\n")

        while True:
            link = input("Enter profile link: ").strip()

            if link.lower() == "done":
                break

            if link.startswith("https://"):
                links.append(link)
                print(OKGREEN + "Link saved." + ENDC)
            else:
                print(FAIL + "Enter a full HTTPS profile link." + ENDC)

        for i, link in enumerate(links, start=1):
            print(OKBLUE + f"Opening profile {i} of {len(links)}..." + ENDC)
            driver.get(link)

            input(
                "Review the profile and send a friend request manually "
                "if appropriate. Press Enter for the next profile..."
            )

        print(OKGREEN + "Finished reviewing all profiles." + ENDC)

    finally:
        driver.quit()


while True:
    command = input(OKGREEN + tool + ENDC).strip().lower()

    if command == "start":
        start()

    elif command == "version":
        print("Version 2.0")

    elif command == "exit":
        print("Exiting...")
        break

    elif command == "info":
        print("Opens Facebook profile links for manual review.")

    elif command == "clear":
        print("\033[2J\033[H", end="")

    elif command in ("help", "h"):
        help()

    else:
        print(FAIL + "Command not recognized. Type help." + ENDC)
