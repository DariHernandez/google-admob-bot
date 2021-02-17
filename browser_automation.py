#! python3

import logging, zipfile, os, time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from proxy_manager import Proxy

class Browser (): 
    """
    Class to make web automation
    """

    def __init__ (self, start_page="http://ipinfo.io/json", headless=False, proxy=False): 
        """
        Constructor of class
        """

        # Instance of proxy class
        my_proxy = Proxy (proxy_file="proxy_list.txt", removed_proxy_file="removed_proxy_list.txt")

        # Disable testing mode
        logging.disable()

        # Run a loop to find a functional proxy
        while True:

            try: 
                # Variables for class
                self.__web_page = start_page
                self.__headless = headless

                if proxy: 
                    # Get proxy for the current chrome instance
                    self.current_dir = os.path.dirname (__file__)
                    self.proxy = my_proxy.get_random_proxy()

                    # Print iformation
                    proxy_to_print = "{}:{}:{}:{}".format (self.proxy["ip"], \
                        self.proxy["port"], self.proxy["user"], self.proxy["password"])
                    print ("\nLoading ipinfo page: {}...\nProxy: {}".format(self.__web_page[:40], proxy_to_print))
                else: 
                    # Set proxy to None
                    self.proxy = None

                    # Print information
                    print ("\nLoading ipinfo page: {}...".format(self.__web_page[:40]))

                self.__browser = self.__get_chrome_instance()
                self.__browser.set_page_load_timeout (15)

                # Load page
                self.__browser.get (self.__web_page)

                # Verify the correct load of the page
                try: 
                    self.__browser.find_element_by_css_selector("#reload-button")
                except: 
                    break
                else:
                    print ("Page take a lot of time to load. Trying again.")
                    raise TimeoutError ("Page take a lot of time to load. Trying again.")

            except Exception as err:
                # Raise an error: fail proxy detected
                logging.error (err)
                my_proxy.remove_proxy (self.proxy)
                continue
            else: 
                break


    def __get_chrome_instance (self):
        """
        Return an instance of google chrome browser
        """

        # PROXY CONFIGURATION
        manifest_json = """
        {
            "version": "1.0.0",
            "manifest_version": 2,
            "name": "Chrome Proxy",
            "permissions": [
                "proxy",
                "tabs",
                "unlimitedStorage",
                "storage",
                "<all_urls>",
                "webRequest",
                "webRequestBlocking"
            ],
            "background": {
                "scripts": ["background.js"]
            },
            "minimum_chrome_version":"22.0.0"
        }
        """

        background_js = """
        var config = {
                mode: "fixed_servers",
                rules: {
                singleProxy: {
                    scheme: "http",
                    host: "%s",
                    port: parseInt(%s)
                },
                bypassList: ["localhost"]
                }
            };

        chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

        function callbackFn(details) {
            return {
                authCredentials: {
                    username: "%s",
                    password: "%s"
                }
            };
        }

        chrome.webRequest.onAuthRequired.addListener(
                    callbackFn,
                    {urls: ["<all_urls>"]},
                    ['blocking']
        );
        """ % (self.proxy["ip"], self.proxy["port"], self.proxy["user"], self.proxy["password"], )


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

        if self.proxy: 
            pluginfile = os.path.join(self.current_dir, "proxy", 'proxyproxy_auth_plugin.zip')

            with zipfile.ZipFile(pluginfile, 'w') as zp:
                zp.writestr("manifest.json", manifest_json)
                zp.writestr("background.js", background_js)

            options.add_extension(pluginfile)

        browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        
        # Clear extra white lines
        print ("\033[A                             \033[A")
        print ("\033[A                             \033[A")

        return browser

    def new_tob (self): 
        """
        Create new empty tab in browser
        """

        self.__browser.execute_script("window.open('');")
        print ("\t - New empty tab created.")

    def switch_to_tab (self, number): 
        """
        Switch to specific number of tab
        """

        windows = self.__browser.window_handles
        self.__browser.switch_to.window(windows[number])
        print ("\t - Switched to tab: {}.".format (number))

    def send_data (self, selector, data): 
        """
        Send data to specific input fill
        """
        print ("\t - sending information to input fill ({}..., {})".format (selector[0:20], data))
        elem = self.__browser.find_element_by_css_selector (selector)

        # Write data 
        elem.send_keys (data)

    def click (self, selector): 
        """
        Send data to specific input fill
        """
        print ("\t - clicking an element ({}...)".format (selector[0:20]))
        elem = self.__browser.find_element_by_css_selector (selector)
        elem.click()

    def wait_to_load_click (self, selector): 
        """
        Wait to load specific instartable element in the page
        """
                
        print ("\n\t - wating for an clickable element ({}...)".format (selector[0:20]))

        while True: 

            try: 
                elem = self.__browser.find_element_by_css_selector (selector)
                elem.click()
            except:
                time.sleep (0.5) 
                continue
            else: 
                break

    def end_browser (self):
        """
        Close the current instance of chrome
        """

        self.__browser.close()

    def reload_browser (self): 
        """
        Close the current instance of the web browser and reload in the same page
        """

        self.end_browser()
        self.__browser = self.__get_chrome_instance()
        print ("Reloading page")
        self.__browser.get (self.__web_page)

    def load_page (self, page): 
        """
        Load specific page in current browser
        """
        print ("Loading page: {}...".format (page[0:40]))
        self.__web_page = page
        self.__browser.get (self.__web_page)

    




