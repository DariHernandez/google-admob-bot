#! python3

import logging, zipfile, os, time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

class Browser (): 
    """
    Class to make web automation
    """

    def __init__ (self, start_page="http://ipinfo.io/json", headless=False): 
        """
        Constructor of class
        """

        # Disable testing mode
        logging.basicConfig( level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s' )
        logging.disable()

        # Run a loop to find a functional proxy
        while True:

            try: 
                # Variables for class
                self.__web_page = start_page
                self.__headless = headless

                # Set proxy to None
                self.proxy = None

                # Print information
                print ("\nLoading ipinfo page: {}...".format(self.__web_page[:40]))

                self.browser = self.__get_chrome_instance()
                self.browser.set_page_load_timeout (15)

                # Load page
                self.browser.get (self.__web_page)

                # Verify the correct load of the page
                try: 
                    self.browser.find_element_by_css_selector("#reload-button")
                except: 
                    break
                else:
                    print ("Page take a lot of time to load. Trying again.")
                    raise TimeoutError ("Page take a lot of time to load. Trying again.")

            except Exception as err:
                # Raise an error: fail proxy detected
                logging.error (err)
                print (err)
                continue
            else: 
                break


    def __get_chrome_instance (self):
        """
        Return an instance of google chrome browser
        """

        # CONFIURE GOOGLE CHROME
        options = webdriver.ChromeOptions()

        if self.__headless == True: 
            options.add_argument("--headless")

        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')  
        options.add_argument('--start-maximized')
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')

        browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        
        # Clear extra white lines
        print ("\033[A                             \033[A")
        print ("\033[A                             \033[A")

        return browser

    def new_tab (self): 
        """
        Create new empty tab in browser
        """

        self.browser.execute_script("window.open('');")
        print ("\t - New empty tab created.")

    def switch_to_tab (self, number): 
        """
        Switch to specific number of tab
        """

        windows = self.browser.window_handles
        self.browser.switch_to.window(windows[number])
        print ("\t - Switched to tab: {}.".format (number))

    def send_data (self, selector, data): 
        """
        Send data to specific input fill
        """
        print ("\t - sending information to input fill ({}..., {})".format (selector[0:20], data))
        elem = self.browser.find_element_by_css_selector (selector)

        # Write data 
        elem.send_keys (data)

    def click (self, selector): 
        """
        Send data to specific input fill
        """
        print ("\t - clicking an element ({}...)".format (selector[0:20]))
        elem = self.browser.find_element_by_css_selector (selector)
        elem.click()

    def wait_to_load_click (self, selector, timeout=None): 
        """
        Wait to load specific instartable element in the page
        """
                
        print ("\n\t - wating for an clickable element ({}...)".format (selector[0:20]))

        loops_ounter = 0

        # Seach the element each 0.5 seconds
        while True: 

            loops_ounter += 1
            
            # if elemt is optional and the pages takes to many time to load, skip it
            if timeout*2 == loops_ounter: 
                return False

            try: 
                elem = self.browser.find_element_by_css_selector (selector)
                elem.click()
            except Exception as err:
                time.sleep (0.5) 
                logging.debug (err)
                continue
            else: 
                return True

    def reload_page (self): 
        """
        Reload the current page
        """

        self.browser.refresh()

    def end_browser (self):
        """
        Close the current instance of chrome
        """

        self.browser.close()

    def load_page (self, page): 
        """
        Load specific page in current browser
        """
        print ("Loading page: {}...".format (page[0:40]))
        self.__web_page = page
        self.browser.get (self.__web_page)

    def swith_to_frame (self, frame_id): 
        """
        Switch to iframe inside the main content
        """

        self.swith_to_main_frame()
        frame_id = frame_id.replace ("#","")
        self.browser.switch_to_frame (frame_id)

    def swith_to_main_frame (self): 
        """
        Switch to the main contecnt of the page
        """
        
        self.browser.switch_to_default_content()

    




