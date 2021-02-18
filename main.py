#! python3

import pyautogui, random, time, pprint, os
from google_ss import Google_shets
from web_scraping import Browser
from random_address import get_ramdom_address


class Web_automation (): 
    """
    Class with functions to make the web automation of the project,
    using the other modules: web_scraping, random_address and google_ss
    """

    def __init__ (self, sheet_link, data_row): 
        """
        Constructor of the class
        """

        current_folder = os.path.dirname (__file__)
        index_file = os.path.join ("file://", current_folder, "index.html")

        # Variables of class
        self.headless = headless
        self.row = row 
    
        # instance of classes
        self.my_browser = Browser (headless=headless, start_page=index_file)
        
        # Wait time to use proxy
        input ("\nManual configure your proxy or vpn.\n")
    
    
    def login (self): 
        """
        Make a login to google in the current browser window
        """

        # Get credentials
        email = self.row["Email"]
        password = self.row["Password"]

        # Load login page
        login_page = "https://accounts.google.com/signin/v2/identifier?service=admob&passive=1209600&continue=https%3A%2F%2Fapps.admob.com%2F%3F_ga%3D2.15979646.959976446.1613507101-1331192604.1613507101&followup=https%3A%2F%2Fapps.admob.com%2F%3F_ga%3D2.15979646.959976446.1613507101-1331192604.1613507101&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
        self.my_browser.load_page (login_page)

        # Write user name and continue
        selector_email = "#identifierId"
        selector_next_button = "#identifierNext > div > button > div.VfPpkd-RLmnJb"
        self.my_browser.wait_to_load_click (selector_email)
        self.my_browser.send_data (selector_email, email)
        self.my_browser.click (selector_next_button)

        # Write password and continue
        selector_password = "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input"    
        selector_next_button = "#passwordNext > div > button > div.VfPpkd-RLmnJb"
        self.my_browser.wait_to_load_click (selector_password)
        self.my_browser.send_data (selector_password, password)
        self.my_browser.click (selector_next_button)

    def accept_warning (self): 
        """
        Accept the warning that is sometimes displayed after login
        """

        # Click in accept button | Try to click ot skip
        selector_accept_button = "#accept"
        self.my_browser.wait_to_load_click (selector_accept_button, optional=True)

    def update_details_link (self): 
        """
        Open "update details" link
        """

        # Click in "here" link
        selector_update_details_link = "body > div > root > div:nth-child(2) > error > article > section > p > simple-html > span > a"
        self.my_browser.wait_to_load_click (selector_update_details_link)

    def birthday_form (self): 
        """
        Fill form of birthday information
        """

        # Get date
        date_birth = self.data_sheet[0]["Date of Birth"]
        date_month = date_birth[:date_birth.find("/")] 
        date_day = date_birth[date_birth.find("/")+1:date_birth.rfind("/")]
        date_year = date_birth[date_birth.rfind("/")+1:]    
        
        # Update switch of tabs | 
        self.my_browser.switch_to_tab (0)
        self.my_browser.switch_to_tab (1)

        # Write month
        selector_month = "#yDmH0d > c-wiz > div > div:nth-child(3) > c-wiz > div > div.VfPpkd-WsjYwc.VfPpkd-WsjYwc-OWXEXe-INsAgc.KC1dQ.Usd1Ac.AaN0Dd.hTY94b.HYI7Re.S69s8b > form > div.wuxXce.ECutae > div:nth-child(1) > div > div > div.M0zhbf.xYWZbf > div.ohXgge.Czzg8c > div > div > div > div.VfPpkd-TkwUic"
        self.my_browser.wait_to_load_click (selector_month)
        for _ in range (0, int(date_month) + 1): 
            pyautogui.press ("down")
        pyautogui.press ("enter")
    
        # Write day 
        selector_day = "#i7"
        self.my_browser.send_data (selector_day, date_day)

        # Write year
        selector_year = "#i9"
        self.my_browser.send_data (selector_year, date_year)

        # Save button
        selector_save_button = "#yDmH0d > c-wiz > div > div:nth-child(3) > c-wiz > div > div.VfPpkd-WsjYwc.VfPpkd-WsjYwc-OWXEXe-INsAgc.KC1dQ.Usd1Ac.AaN0Dd.hTY94b.HYI7Re.S69s8b > form > div.wuxXce.ECutae > div.SjcvKf > div.Atqwuf > div > div > button > div.VfPpkd-RLmnJb"
        self.my_browser.click (selector_save_button)

        # Confirm button
        selector_confirm_button = "#yDmH0d > div.VfPpkd-Sx9Kwc.cC1eCc.UDxLd.PzCPDd.VfPpkd-Sx9Kwc-OWXEXe-FNFY6c > div.VfPpkd-wzTsW > div > div.VfPpkd-T0kwCb > button:nth-child(2) > div.VfPpkd-RLmnJb"
        self.my_browser.wait_to_load_click (selector_confirm_button)

    def move_to_tap (self, tab): 
        """
        Move to specific number of tab (start in 0)
        """
        # Go to the last tap an reload it
        time.sleep (2)
        self.my_browser.switch_to_tab(tab)
        self.my_browser.reload_page()

    def location_from (self): 
        """
        Fill form of country, time zone and currency
        """

        # Country 
        selector_country = "body > div:nth-child(8) > root > div:nth-child(2) > admob-signup > section:nth-child(2) > create-adsense-adwords > article > section > div:nth-child(1) > material-dropdown-select > dropdown-button > div"
        self.my_browser.wait_to_load_click (selector_country)
        pyautogui.typewrite ("United")
        pyautogui.press ("down")
        pyautogui.press ("down")
        pyautogui.press ("enter")

        # Time zone
        selector_time = "body > div:nth-child(8) > root > div:nth-child(2) > admob-signup > section:nth-child(2) > create-adsense-adwords > article > section > div:nth-child(2) > material-dropdown-select > dropdown-button > div"
        self.my_browser.click (selector_time)
        time_zone_random = random.randint (1,21)
        for _ in range (0, time_zone_random): 
            pyautogui.press ("down")
        pyautogui.press ("enter")

        # Currency
        selector_currency = "body > div:nth-child(8) > root > div:nth-child(2) > admob-signup > section:nth-child(2) > create-adsense-adwords > article > section > div:nth-child(3) > material-dropdown-select > dropdown-button > div"
        self.my_browser.click (selector_currency)
        pyautogui.press ("down")
        pyautogui.press ("enter")

        # Accept
        selector_accept = "body > div:nth-child(8) > root > div:nth-child(2) > admob-signup > section:nth-child(3) > terms > article > div > material-checkbox"
        self.my_browser.wait_to_load_click (selector_accept)

        # Create account
        selector_create_account = "body > div:nth-child(8) > root > div:nth-child(2) > admob-signup > section > div > material-button > material-ripple"
        self.my_browser.wait_to_load_click (selector_create_account)

    def fill_yes_no_form (self): 
        """
        Fill form with all response in "yes"
        """

        # Form multiple choices buttons
        selector_yes_1 = "body > div > root > div:nth-child(2) > email-preferences > section:nth-child(2) > div > div:nth-child(2) > material-radio-group > material-radio:nth-child(1) > div > material-ripple"
        selector_yes_2 = "body > div > root > div:nth-child(2) > email-preferences > section:nth-child(2) > div > div:nth-child(3) > material-radio-group > material-radio:nth-child(1) > div > material-ripple"
        selector_yes_3 = "body > div > root > div:nth-child(2) > email-preferences > section:nth-child(2) > div > div:nth-child(4) > material-radio-group > material-radio:nth-child(1) > div > material-ripple"
        selector_yes_4 = "body > div > root > div:nth-child(2) > email-preferences > section:nth-child(2) > div > div:nth-child(5) > material-radio-group > material-radio:nth-child(1) > div > material-ripple"
        selector_yes_5 = "body > div > root > div:nth-child(2) > email-preferences > section:nth-child(2) > div > div:nth-child(6) > material-radio-group > material-radio:nth-child(1) > div > material-ripple"

        self.my_browser.wait_to_load_click (selector_yes_1)
        self.my_browser.click (selector_yes_2)
        self.my_browser.click (selector_yes_3)
        self.my_browser.click (selector_yes_4)
        self.my_browser.click (selector_yes_5)

        selector_next_button = "body > div > root > div:nth-child(2) > email-preferences > section:nth-child(2) > div > material-button > material-ripple"
        self.my_browser.wait_to_load_click (selector_next_button)

    def set_payments_info (self): 
        """
        Set payments information
        """

        # Loop for each row in sheet
        for row in self.data_sheet: 

            # SETUP PAYMENTS
            selector_payments = "body > div:nth-child(7) > root > div > div > sidebar > div > sidebar-menu > material-list > div:nth-child(4) > sidebar-panel:nth-child(4) > div > sidebar-menu-item > material-list-item > material-ripple"
            self.my_browser.wait_to_load_click (selector_payments)

            selector_setup_payments = "payments > publisher-payments > div > div > payments-card > template-card > div > div > material-button > material-ripple"
            self.my_browser.wait_to_load_click (selector_setup_payments)

            # Get address from file
            address = get_ramdom_address()

            # Switch inside the frame
            frame_id = "signup-containerIframe"
            frame_selector = "#signup-containerIframe"
            self.my_browser.wait_to_load_click (frame_selector)
            self.my_browser.swith_to_frame (frame_id)

            # Write address
            selector_street = "input[name='ADDRESS_LINE_1']"
            selector_city = "input[name='LOCALITY']"
            selector_state = "div[data-name='ADMIN_AREA']"
            selector_zip_code = "input[name='POSTAL_CODE']"

            self.my_browser.wait_to_load_click (selector_street)
            self.my_browser.send_data (selector_street, address["street"])
            self.my_browser.send_data (selector_city, address["city"])
            self.my_browser.click (selector_state)
            pyautogui.typewrite ("n")
            for _ in range (0, 23): 
                pyautogui.press ("down")
            pyautogui.press ("enter")
            self.my_browser.send_data (selector_zip_code, address["zip_code"])

            # Switch to mian data frame
            self.my_browser.swith_to_main_frame()

            # Send form
            selector_next_button = "inventory-app > payments > publisher-payments > div > div > payments-signup > div > material-button"
            self.my_browser.wait_to_load_click (selector_next_button)


            # LOOP FOR ADD EACH TYPE OF ACCOUNT
            for type_index in range (1, 4): 
                    
                # GOOGLE PAY | Add new payment

                google_pay_page = "https://pay.google.com/gp/w/u/0/home/paymentmethods"
                time.sleep(2)
                self.my_browser.load_page (google_pay_page)

                # Swith to intermal frame
                frame_id = "mainWidget_:0Iframe"
                frame_selector = "iframe"
                self.my_browser.wait_to_load_click (frame_selector)
                self.my_browser.swith_to_frame (frame_id)
                
                if type_index == 1: 
                    selector_add_pay_button = "#iframeBody > div.b3id-payment-methods.b3-payment-methods > div.b3-page-content.b3-payment-methods-content > div a > div > div > span"
                else: 
                    selector_add_pay_button = "#iframeBody div.b3-payment-methods-instrument-details-container > a:last-child span"
                self.my_browser.click(selector_add_pay_button)

                # SET PAYMENTS INFO

                # Swith to intermal frame
                frame_id = "mainWidget_:0Iframe"
                frame_selector = "iframe"
                time.sleep (2)
                self.my_browser.swith_to_frame (frame_id)

                # Select bank
                selector_add_bank_button = "div[id$='_option3']"
                self.my_browser.wait_to_load_click (selector_add_bank_button)

                # Swith to intermal frame
                frame_id = "mainWidget_:0Iframe"
                frame_selector = "#mainWidget_:0Iframe"
                time.sleep (5)
                self.my_browser.swith_to_frame (frame_id)

                # Write info
                selector_bank = "input[name='FIELD_ACCOUNT_HOLDER_NAME']"
                selector_type = "#\:x8 > div"
                selector_routing = "input[name='FIELD_BANK_CODE']"
                selector_account = "input[name='FIELD_ACCOUNT_NUMBER']"

                # loop for save each account in diferent types
                # for index_count_type in range (1, 4): 

                self.my_browser.send_data (selector_bank, row["Name on Bank"])
                for _ in range (0, type_index-1):
                    pyautogui.press ("down")
                pyautogui.press ("enter")
                self.my_browser.send_data (selector_routing, row["Routing"])
                self.my_browser.send_data (selector_account, row["Account No."])

                selector_next_button = "#saveAddInstrument"
                self.my_browser.click (selector_next_button)

                # VERIFY BANK ACCOUNT

                frame_id = "bankAccountVerification"
                frame_selector = "#bankAccountVerification"
                time.sleep (5)
                self.my_browser.swith_to_frame (frame_id)

                selector_verify_test_deposit = "#iframeBody > div > div > div > div > div > div > div:nth-child(3) > div"
                self.my_browser.click (selector_verify_test_deposit)

                selector_next_button = "#saveAddInstrument"
                self.my_browser.click (selector_next_button)

                selector_next_button = "#cancelAddInstrument"
                self.my_browser.click (selector_next_button)

# Run or nor the browser in background
headless = False

# Link of the google sheet with the information
sheet_link = "https://docs.google.com/spreadsheets/d/13FWzWDD75akWq-NajYRYwXij-ptWNF3w0sBgaUv7r7Q/edit?usp=sharing"

# Get data from google sheet
my_google_sheets = Google_shets (sheet_link)
data_sheet = my_google_sheets.get_data()

# Loop for each user in google sheet
for row in data_sheet:   
    # my_web_automation = Web_automation(headless, row)
    # my_web_automation.login()

    var_input = input ("End row")