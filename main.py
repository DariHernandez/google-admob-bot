#! python3

import pprint
from google_ss import Google_shets
from web_scraping import Browser


# Public shred google sheet link with edit permissions
sheet_link = "https://docs.google.com/spreadsheets/d/13FWzWDD75akWq-NajYRYwXij-ptWNF3w0sBgaUv7r7Q/edit?usp=sharing"


# Web browser configuration variable
headless = False

# Instance of web browser
my_browser = Browser (headless=headless)

# Instance of google sheet
my_google_sheets = Google_shets (sheet_link)
data_sheet = my_google_sheets.get_data()


# Loop for each row in sheet
for row in data_sheet: 
    
    # Get credentials
    email = row["Email"]
    password = row ["Password"]

    # Wait time to use proxy
    input ("\nManual configure your proxy or vpn. Press any key to continue...\n")


    # LOGIN
    
    # Load login page
    login_page = "https://accounts.google.com/signin/v2/identifier?service=admob&passive=1209600&continue=https%3A%2F%2Fapps.admob.com%2F%3F_ga%3D2.15979646.959976446.1613507101-1331192604.1613507101&followup=https%3A%2F%2Fapps.admob.com%2F%3F_ga%3D2.15979646.959976446.1613507101-1331192604.1613507101&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
    my_browser.load_page (login_page)


    # Write user name and continue
    selector_email = "#identifierId"
    selector_next_button = "#identifierNext > div > button > div.VfPpkd-RLmnJb"
    my_browser.wait_to_load_click (selector_email)
    my_browser.send_data (selector_email, email)
    my_browser.click (selector_next_button)

    # Write password and continue
    selector_password = "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input"    
    selector_next_button = "#passwordNext > div > button > div.VfPpkd-RLmnJb"
    my_browser.wait_to_load_click (selector_password)
    my_browser.send_data (selector_password, password)
    my_browser.click (selector_next_button)

    # Click in accept button | Try to click ot skip
    selector_accept_button = "#accept"
    my_browser.wait_to_load_click (selector_accept_button, optional=True)

    # Click in "here" link
    selector_update_details_link = "body > div > root > div:nth-child(2) > error > article > section > p > simple-html > span > a"
    my_browser.wait_to_load_click (selector_update_details_link)

    # BIRTHDAY FORM FILL

    