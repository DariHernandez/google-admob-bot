#! python3

import pprint
from google_ss import Google_shets
from web_scraping import Browser
import pyautogui, random, time


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
    input ("\nManual configure your proxy or vpn. Press Enter to continue...\n")


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

    # # Click in accept button | Try to click ot skip
    # selector_accept_button = "#accept"
    # my_browser.wait_to_load_click (selector_accept_button, optional=True)

    # # Click in "here" link
    # selector_update_details_link = "body > div > root > div:nth-child(2) > error > article > section > p > simple-html > span > a"
    # my_browser.wait_to_load_click (selector_update_details_link)


    # # # BIRTHDAY FORM FILL


    # # Get date
    # date_birth = data_sheet[0]["Date of Birth"]
    # date_month = date_birth[:date_birth.find("/")] 
    # date_day = date_birth[date_birth.find("/")+1:date_birth.rfind("/")]
    # date_year = date_birth[date_birth.rfind("/")+1:]    
    
    # # Update switch of tabs | 
    # my_browser.switch_to_tab (0)
    # my_browser.switch_to_tab (1)

    # # Write month
    # selector_month = "#yDmH0d > c-wiz > div > div:nth-child(3) > c-wiz > div > div.VfPpkd-WsjYwc.VfPpkd-WsjYwc-OWXEXe-INsAgc.KC1dQ.Usd1Ac.AaN0Dd.hTY94b.HYI7Re.S69s8b > form > div.wuxXce.ECutae > div:nth-child(1) > div > div > div.M0zhbf.xYWZbf > div.ohXgge.Czzg8c > div > div > div > div.VfPpkd-TkwUic"
    # my_browser.wait_to_load_click (selector_month)
    # for _ in range (0, int(date_month) + 1): 
    #     pyautogui.press ("down")
    # pyautogui.press ("enter")
 
    # # Write day 
    # selector_day = "#i7"
    # my_browser.send_data (selector_day, date_day)

    # # Write year
    # selector_year = "#i9"
    # my_browser.send_data (selector_year, date_year)

    # # Save button
    # selector_save_button = "#yDmH0d > c-wiz > div > div:nth-child(3) > c-wiz > div > div.VfPpkd-WsjYwc.VfPpkd-WsjYwc-OWXEXe-INsAgc.KC1dQ.Usd1Ac.AaN0Dd.hTY94b.HYI7Re.S69s8b > form > div.wuxXce.ECutae > div.SjcvKf > div.Atqwuf > div > div > button > div.VfPpkd-RLmnJb"
    # my_browser.click (selector_save_button)

    # # Confirm button
    # selector_confirm_button = "#yDmH0d > div.VfPpkd-Sx9Kwc.cC1eCc.UDxLd.PzCPDd.VfPpkd-Sx9Kwc-OWXEXe-FNFY6c > div.VfPpkd-wzTsW > div > div.VfPpkd-T0kwCb > button:nth-child(2) > div.VfPpkd-RLmnJb"
    # my_browser.wait_to_load_click (selector_confirm_button)


    # RELOAD LAST PAGE | UPDATE COUNTRY, TIME ZONE AND CURRENCY


    # # Go to the last tap an reload it
    # time.sleep (2)
    # my_browser.switch_to_tab(0)
    # my_browser.reload_page()

    # # Country 
    # selector_country = "body > div:nth-child(8) > root > div:nth-child(2) > admob-signup > section:nth-child(2) > create-adsense-adwords > article > section > div:nth-child(1) > material-dropdown-select > dropdown-button > div"
    # my_browser.wait_to_load_click (selector_country)
    # pyautogui.typewrite ("United")
    # pyautogui.press ("down")
    # pyautogui.press ("down")
    # pyautogui.press ("enter")

    # # Time zone
    # selector_time = "body > div:nth-child(8) > root > div:nth-child(2) > admob-signup > section:nth-child(2) > create-adsense-adwords > article > section > div:nth-child(2) > material-dropdown-select > dropdown-button > div"
    # my_browser.click (selector_time)
    # time_zone_random = random.randint (1,21)
    # for _ in range (0, time_zone_random): 
    #     pyautogui.press ("down")
    # pyautogui.press ("enter")

    # # Currency
    # selector_currency = "body > div:nth-child(8) > root > div:nth-child(2) > admob-signup > section:nth-child(2) > create-adsense-adwords > article > section > div:nth-child(3) > material-dropdown-select > dropdown-button > div"
    # my_browser.click (selector_currency)
    # pyautogui.press ("down")
    # pyautogui.press ("enter")

    # # Accept
    # selector_accept = "body > div:nth-child(8) > root > div:nth-child(2) > admob-signup > section:nth-child(3) > terms > article > div > material-checkbox"
    # my_browser.wait_to_load_click (selector_accept)

    # # Create account
    # selector_create_account = "body > div:nth-child(8) > root > div:nth-child(2) > admob-signup > section > div > material-button > material-ripple"
    # my_browser.wait_to_load_click (selector_create_account)
    # # my_browser.wait_to_load_click (selector_create_account)
    # print (selector_create_account)

