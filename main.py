#! python3

import pyautogui, random, time, pprint
from google_ss import Google_shets
from web_scraping import Browser
from random_address import get_ramdom_address


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

    # Click in accept button | Try to click ot skip
    selector_accept_button = "#accept"
    my_browser.wait_to_load_click (selector_accept_button, optional=True)

    # Click in "here" link
    selector_update_details_link = "body > div > root > div:nth-child(2) > error > article > section > p > simple-html > span > a"
    my_browser.wait_to_load_click (selector_update_details_link)


    # # BIRTHDAY FORM FILL


    # Get date
    date_birth = data_sheet[0]["Date of Birth"]
    date_month = date_birth[:date_birth.find("/")] 
    date_day = date_birth[date_birth.find("/")+1:date_birth.rfind("/")]
    date_year = date_birth[date_birth.rfind("/")+1:]    
    
    # Update switch of tabs | 
    my_browser.switch_to_tab (0)
    my_browser.switch_to_tab (1)

    # Write month
    selector_month = "#yDmH0d > c-wiz > div > div:nth-child(3) > c-wiz > div > div.VfPpkd-WsjYwc.VfPpkd-WsjYwc-OWXEXe-INsAgc.KC1dQ.Usd1Ac.AaN0Dd.hTY94b.HYI7Re.S69s8b > form > div.wuxXce.ECutae > div:nth-child(1) > div > div > div.M0zhbf.xYWZbf > div.ohXgge.Czzg8c > div > div > div > div.VfPpkd-TkwUic"
    my_browser.wait_to_load_click (selector_month)
    for _ in range (0, int(date_month) + 1): 
        pyautogui.press ("down")
    pyautogui.press ("enter")
 
    # Write day 
    selector_day = "#i7"
    my_browser.send_data (selector_day, date_day)

    # Write year
    selector_year = "#i9"
    my_browser.send_data (selector_year, date_year)

    # Save button
    selector_save_button = "#yDmH0d > c-wiz > div > div:nth-child(3) > c-wiz > div > div.VfPpkd-WsjYwc.VfPpkd-WsjYwc-OWXEXe-INsAgc.KC1dQ.Usd1Ac.AaN0Dd.hTY94b.HYI7Re.S69s8b > form > div.wuxXce.ECutae > div.SjcvKf > div.Atqwuf > div > div > button > div.VfPpkd-RLmnJb"
    my_browser.click (selector_save_button)

    # Confirm button
    selector_confirm_button = "#yDmH0d > div.VfPpkd-Sx9Kwc.cC1eCc.UDxLd.PzCPDd.VfPpkd-Sx9Kwc-OWXEXe-FNFY6c > div.VfPpkd-wzTsW > div > div.VfPpkd-T0kwCb > button:nth-child(2) > div.VfPpkd-RLmnJb"
    my_browser.wait_to_load_click (selector_confirm_button)


    # RELOAD LAST PAGE | UPDATE COUNTRY, TIME ZONE AND CURRENCY


    # Go to the last tap an reload it
    time.sleep (2)
    my_browser.switch_to_tab(0)
    my_browser.reload_page()

    # Country 
    selector_country = "body > div:nth-child(8) > root > div:nth-child(2) > admob-signup > section:nth-child(2) > create-adsense-adwords > article > section > div:nth-child(1) > material-dropdown-select > dropdown-button > div"
    my_browser.wait_to_load_click (selector_country)
    pyautogui.typewrite ("United")
    pyautogui.press ("down")
    pyautogui.press ("down")
    pyautogui.press ("enter")

    # Time zone
    selector_time = "body > div:nth-child(8) > root > div:nth-child(2) > admob-signup > section:nth-child(2) > create-adsense-adwords > article > section > div:nth-child(2) > material-dropdown-select > dropdown-button > div"
    my_browser.click (selector_time)
    time_zone_random = random.randint (1,21)
    for _ in range (0, time_zone_random): 
        pyautogui.press ("down")
    pyautogui.press ("enter")

    # Currency
    selector_currency = "body > div:nth-child(8) > root > div:nth-child(2) > admob-signup > section:nth-child(2) > create-adsense-adwords > article > section > div:nth-child(3) > material-dropdown-select > dropdown-button > div"
    my_browser.click (selector_currency)
    pyautogui.press ("down")
    pyautogui.press ("enter")

    # Accept
    selector_accept = "body > div:nth-child(8) > root > div:nth-child(2) > admob-signup > section:nth-child(3) > terms > article > div > material-checkbox"
    my_browser.wait_to_load_click (selector_accept)

    # Create account
    selector_create_account = "body > div:nth-child(8) > root > div:nth-child(2) > admob-signup > section > div > material-button > material-ripple"
    my_browser.wait_to_load_click (selector_create_account)
    # my_browser.wait_to_load_click (selector_create_account)
    print (selector_create_account)

    
    # FILL YES / NO FORM


    # Form multiple choices buttons
    selector_yes_1 = "body > div > root > div:nth-child(2) > email-preferences > section:nth-child(2) > div > div:nth-child(2) > material-radio-group > material-radio:nth-child(1) > div > material-ripple"
    selector_yes_2 = "body > div > root > div:nth-child(2) > email-preferences > section:nth-child(2) > div > div:nth-child(3) > material-radio-group > material-radio:nth-child(1) > div > material-ripple"
    selector_yes_3 = "body > div > root > div:nth-child(2) > email-preferences > section:nth-child(2) > div > div:nth-child(4) > material-radio-group > material-radio:nth-child(1) > div > material-ripple"
    selector_yes_4 = "body > div > root > div:nth-child(2) > email-preferences > section:nth-child(2) > div > div:nth-child(5) > material-radio-group > material-radio:nth-child(1) > div > material-ripple"
    selector_yes_5 = "body > div > root > div:nth-child(2) > email-preferences > section:nth-child(2) > div > div:nth-child(6) > material-radio-group > material-radio:nth-child(1) > div > material-ripple"

    my_browser.wait_to_load_click (selector_yes_1)
    my_browser.click (selector_yes_2)
    my_browser.click (selector_yes_3)
    my_browser.click (selector_yes_4)
    my_browser.click (selector_yes_5)

    selector_next_button = "body > div > root > div:nth-child(2) > email-preferences > section:nth-child(2) > div > material-button > material-ripple"
    my_browser.wait_to_load_click (selector_next_button)


    # SETUP PAYMENTS


    selector_payments = "body > div:nth-child(7) > root > div > div > sidebar > div > sidebar-menu > material-list > div:nth-child(4) > sidebar-panel:nth-child(4) > div > sidebar-menu-item > material-list-item > material-ripple"
    my_browser.wait_to_load_click (selector_payments)

    selector_setup_payments = "payments > publisher-payments > div > div > payments-card > template-card > div > div > material-button > material-ripple"
    my_browser.wait_to_load_click (selector_setup_payments)

    # Get address from file
    address = get_ramdom_address()
    

    # Switch inside the frame
    frame_id = "signup-containerIframe"
    frame_selector = "#signup-containerIframe"
    my_browser.wait_to_load_click (frame_selector)
    my_browser.swith_to_frame (frame_id)

    # Write address
    selector_street = "input[name='ADDRESS_LINE_1']"
    selector_city = "input[name='LOCALITY']"
    selector_state = "div[data-name='ADMIN_AREA']"
    selector_zip_code = "input[name='POSTAL_CODE']"

    my_browser.wait_to_load_click (selector_street)
    my_browser.send_data (selector_street, address["street"])
    my_browser.send_data (selector_city, address["city"])
    my_browser.click (selector_state)
    pyautogui.typewrite ("n")
    for _ in range (0, 23): 
        pyautogui.press ("down")
    pyautogui.press ("enter")
    my_browser.send_data (selector_zip_code, address["zip_code"])

    # Switch to mian data frame
    my_browser.swith_to_main_frame()

    # Send form
    selector_next_button = "inventory-app > payments > publisher-payments > div > div > payments-signup > div > material-button"
    my_browser.wait_to_load_click (selector_next_button)

    