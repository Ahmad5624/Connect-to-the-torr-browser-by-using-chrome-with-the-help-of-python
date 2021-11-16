from selenium import webdriver
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager

# To use Tor's SOCKS proxy server with chrome, include the socks protocol in the scheme with the --proxy-server option
# PROXY = "socks5://127.0.0.1:9150" # IP:PORT or HOST:PORT

torexe = os.popen(r'C:\Tor Browser\Browser\TorBrowser\Tor\tor.exe')                            #please add to your torrr browser location
PROXY = "socks5://localhost:9050"  # IP:PORT or HOST:PORT

# Enable Performance Logging of Chrome.
desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities["goog:loggingPrefs"] = {"performance": "ALL"}
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=%s' % PROXY)
#options.add_argument("--auto-open-devtools-for-tabs")
#driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\chromedriver.exe')
driver = webdriver.Chrome(ChromeDriverManager().install(),
                          chrome_options=options)
driver.get("http://check.torproject.org")
driver.maximize_window()

#if you want to close the driver then uncomment the below line otherwise move forward
#driver.close()
