# V2.2 added captcha solving and some Amazon EU-Stores - autobuy Germany
# BuyBot PS5 - Auto Buy on Amazon
# https://github.com/bulior/PS5BUYBOT
# -------------------------------------
# If you change something, let me know ;)
# -------------------------------------
import random
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
from termcolor import colored

import telegram as tg
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, CallbackContext)

import configparser

from amazoncaptcha import AmazonCaptcha

# Load Configs
config = configparser.ConfigParser()
config.read("C:/Users/Public/Documents/buybotconfig.ini")
tgtoken = config['telegram']['tgtoken']
tgcid = config['telegram']['tgcid']
amazonuser = config['accountsettings']['amazonuser']
amazonpw = config['accountsettings']['amazonpw']
chrompath = config['pathes']['chrompath']
imgpath = config['pathes']['imgpath']


#### DEGUGGGING #####
debugging = True


# ----- Links to check - old not used-----
query_links = ["https://www.amazon.de/Sony-PlayStation-5-Digital-Edition/dp/B08H98GVK8?tag=mmo-deals-21",
               "https://www.mediamarkt.de/de/product/_sony-playstation%C2%AE5-digital-edition-2661939.html",
               # "https://www.amazon.de/-/en/gp/product/B08H99BPJN/ref=ox_sc_saved_title_1?smid=A3JWKAKR8XB7XF&psc=1"
               ]

# ----- How many loops - old not used -----
loop_n_max = 120
global_loop_n = 0
processbar_text = "none - try later"
updater = Updater(tgtoken)
# ----- Wait until request from telegram user -----
global wait_basket
wait_basket = True


# ---- Progressbar - old not used ---
def progressBar(x, iterable, prefix='', suffix='', decimals=1, length=loop_n_max, fill='█', printEnd="\n"):
    total = iterable
    # Progress Bar Printing Function
    iteration = x
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    global processbar_text
    processbar_text = (f'\r{prefix} |{bar}| {percent}% {suffix}')
    return processbar_text

# --- START CHROME ---
def initialize_webdriver():
    global action
    global browser
    print(colored("Initializing Browser...", 'blue'))
    chrome_options  = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    #option.add_argument('headless')
    browser = webdriver.Chrome(chrompath, options=chrome_options )  # initialize browser app

    browser.get('https://www.amazon.de')
    textcaptcha = "Geben Sie die angezeigten Zeichen"
    if (textcaptcha in browser.page_source):
        captcha = AmazonCaptcha.fromdriver(browser)
        solution = captcha.solve()
        while solution == "Not solved":
            browser.get("https://www.amazon.de")
            captcha = AmazonCaptcha.fromdriver(browser)
            solution = captcha.solve()
            print(colored("[Amazon DE] captcha: ", "red") + colored(solution, "red"))
            time.sleep(1)
        print(colored("[Amazon DE] captcha: ", "red") + colored(solution, "green"))
        captchalist = list(solution)
        for i in range(len(captchalist)):
            captchasolving = browser.find_element_by_xpath('//*[@id="captchacharacters"]')
            captchasolving.send_keys(str(captchalist[i]))
            time.sleep(random.uniform(0, 1))
        print(colored("[Amazon DE] captcha: ", "red") + colored("solved", "green"))
        time.sleep(1)
        captchasubmit = browser.find_element_by_xpath('//button[normalize-space()="Weiter shoppen"]')
        captchasubmit.click()
        browser.get('https://www.amazon.de')
        cookies = browser.find_element_by_xpath('//*[@id="sp-cc-accept"]')
        cookies.click()
        time.sleep(0.5)
    else:
        cookies = browser.find_element_by_xpath('//*[@id="sp-cc-accept"]')
        cookies.click()
        time.sleep(0.5)

    browser.get('https://www.amazon.fr')
    textcaptcha = "Saisissez les caractères"
    if (textcaptcha in browser.page_source):
        captcha = AmazonCaptcha.fromdriver(browser)
        solution = captcha.solve()
        while solution == "Not solved":
            browser.get("https://www.amazon.fr")
            captcha = AmazonCaptcha.fromdriver(browser)
            solution = captcha.solve()
            print(colored("[Amazon FR] captcha: ", "red") + colored(solution, "red"))
            time.sleep(1)
        print(colored("[Amazon FR] captcha: ", "red") + colored(solution, "green"))
        captchalist = list(solution)
        for i in range(len(captchalist)):
            captchasolving = browser.find_element_by_xpath('//*[@id="captchacharacters"]')
            captchasolving.send_keys(str(captchalist[i]))
            time.sleep(random.uniform(0, 1))
        print(colored("[Amazon FR] captcha: ", "red") + colored("solved", "green"))
        time.sleep(1)
        captchasubmit = browser.find_element_by_xpath('//button[normalize-space()="Continuer les achats"]')
        captchasubmit.click()
        browser.get('http://www.amazon.fr')  # open url
        cookies = browser.find_element_by_xpath('//*[@id="sp-cc-accept"]')
        cookies.click()
        time.sleep(0.5)
    else:
        cookies = browser.find_element_by_xpath('//*[@id="sp-cc-accept"]')
        cookies.click()
        time.sleep(0.5)

    browser.get('https://www.amazon.es')
    textcaptcha = "Teclea los caracteres"
    if (textcaptcha in browser.page_source):
        captcha = AmazonCaptcha.fromdriver(browser)
        solution = captcha.solve()
        while solution == "Not solved":
            browser.get("https: // www.amazon.es")
            captcha = AmazonCaptcha.fromdriver(browser)
            solution = captcha.solve()
            print(colored("[Amazon ES] captcha: ", "red") + colored(solution, "red"))
            time.sleep(1)
        print(colored("[Amazon ES] captcha: ", "red") + colored(solution, "green"))
        captchalist = list(solution)
        for i in range(len(captchalist)):
            captchasolving = browser.find_element_by_xpath('//*[@id="captchacharacters"]')
            captchasolving.send_keys(str(captchalist[i]))
            time.sleep(random.uniform(0, 1))
        print(colored("[Amazon ES] captcha: ", "red") + colored("solved", "green"))
        time.sleep(1)
        captchasubmit = browser.find_element_by_xpath('//button[normalize-space()="Seguir comprando"]')
        captchasubmit.click()
        browser.get('http://www.amazon.es')  # open url
        cookies = browser.find_element_by_xpath('//*[@id="sp-cc-accept"]')
        cookies.click()
        time.sleep(0.5)
    else:
        cookies = browser.find_element_by_xpath('//*[@id="sp-cc-accept"]')
        cookies.click()
        time.sleep(0.5)


    browser.get('https://www.amazon.it')
    textcaptcha = "Digita i caratteri"
    if (textcaptcha in browser.page_source):
        captcha = AmazonCaptcha.fromdriver(browser)
        solution = captcha.solve()
        while solution == "Not solved":
            browser.get("https: // www.amazon.it")
            captcha = AmazonCaptcha.fromdriver(browser)
            solution = captcha.solve()
            print(colored("[Amazon IT] captcha: ", "red") + colored(solution, "red"))
            time.sleep(1)
        print(colored("[Amazon IT] captcha: ", "red") + colored(solution, "green"))
        captchalist = list(solution)
        for i in range(len(captchalist)):
            captchasolving = browser.find_element_by_xpath('//*[@id="captchacharacters"]')
            captchasolving.send_keys(str(captchalist[i]))
            time.sleep(random.uniform(0, 1))
        print(colored("[Amazon IT] captcha: ", "red") + colored("solved", "green"))
        time.sleep(1)
        captchasubmit = browser.find_element_by_xpath('//button[normalize-space()="Continua con gli acquisti"]')
        captchasubmit.click()
        browser.get('http://www.amazon.it')  # open url
        cookies = browser.find_element_by_xpath('//*[@id="sp-cc-accept"]')
        cookies.click()
        time.sleep(0.5)
    else:
        cookies = browser.find_element_by_xpath('//*[@id="sp-cc-accept"]')
        cookies.click()
        time.sleep(0.5)


    action = ActionChains(browser)
    assert "Amazon" in browser.title  # check if name is in title and page is loaded
    time.sleep(3)
    # xOffset = random.randrange( 250 )
    # yOffset = random.randrange( 250 )
    # actions = ActionChains( browser )  # initialize actions
    print(colored("Browser is running!", "green"))
    return browser

# ----TELEGRAM BOT startup ---
def initialize_telegram(tgtoken, tgcid):
    print(colored("Initializing Telegram...", 'blue'))
    tg_bot = tg.Bot(token=tgtoken)
    # updater = Updater(tgtoken)
    time.sleep(1)
    print(colored("Deleting all previous updates...", 'blue'))
    offset = tg_bot.get_updates()[-1].update_id
    return tg_bot, tgcid, offset

def bot_startupmessage(update: Update, context: CallbackContext) -> int:
    # Welcome message
    msg = "--- Amazon BuyBot startup ---\n"
    msg += " 👨🏼‍💻 🦾🦾🦾 👨🏼‍💻  \n"
    msg += "Menü:\n"
    msg += "/start - start the bot query\n"
    msg += "/stop - stop everything\n"
    msg += "/status - get status\n"
    msg += "/end - end status messaging\n"
    msg += "/getquery - get/set query links\n"
    # msg += "/status - status of loop function\n"
    # msg += "/cancel - mimimi \n\n"
    # Commands menu
    main_menu_keyboard = [[tg.KeyboardButton('/start', callback_data=str(start))]]
    reply_kb_markup = tg.ReplyKeyboardMarkup(main_menu_keyboard, resize_keyboard=True, one_time_keyboard=True)
    # Send the message with menu
    tg_bot.send_message(chat_id=tgcid, text=msg, reply_markup=reply_kb_markup)
    tg_bot.send_chat_action(chat_id=tgcid, action=tg.ChatAction.TYPING)

# ---- some defs ---

def getquery(update: Update, context: CallbackContext):
    for x in range(len(query_links)):
        tg_bot.send_message(chat_id=tgcid, text=query_links[x])

def log_in(browser, action, amazonuser, amazonpw): # AMAZON
    browser.get('http://www.amazon.de')
    time.sleep(1.5)
    firstLevelMenu = browser.find_element_by_xpath('//*[@id="nav-link-accountList"]/span[2]')
    action.move_to_element(firstLevelMenu).perform()
    time.sleep(2)
    secondLevelMenu = browser.find_element_by_xpath('//*[@id="nav-flyout-ya-signin"]/a/span')
    secondLevelMenu.click()
    time.sleep(1.5)
    signinelement = browser.find_element_by_xpath('//*[@id="ap_email"]')
    signinelement.send_keys(amazonuser)
    time.sleep(1.5)
    cont = browser.find_element_by_xpath('//*[@id="continue"]')
    cont.click()
    time.sleep(1)
    passwordelement = browser.find_element_by_xpath('//*[@id="ap_password"]')
    passwordelement.send_keys(amazonpw)
    time.sleep(2)
    login = browser.find_element_by_xpath('//*[@id="signInSubmit"]')
    login.click()
    time.sleep(1)
    print(colored("Status: Amazon - Successfully logged in", "green"))

def start(update: Update, context: CallbackContext) -> int:
    msg = "Status: Initilizing Web-Broser"
    tg_bot.send_chat_action(chat_id=tgcid, action=tg.ChatAction.TYPING)
    global message
    message = tg_bot.send_message(chat_id=tgcid, text=msg)
    try:
        initialize_webdriver()
        global browser_runnging
        browser_runnging = True
        msg = "Status: Web-Broser is running"
        message.edit_text(msg)
        time.sleep(1)
    except Exception as e:
        print(e)
        browser.close()
        time.sleep(1)
        browser.quit()
        time.sleep(5)

def buy(update: Update, context: CallbackContext):
    global wait_basket
    wait_basket = False
    return wait_basket
    print(wait_basket)

def stopping(update: Update, context: CallbackContext, browser_runnging) -> int:
    if debugging:
        print(browser_runnging)
    if browser_runnging == True:
        print("STOPPE BROWSER")
        browser.quit()  # close browser
        browser_runnging = False
        msg = "Closed! Re /start ?"
        message.edit_text(msg)

def anticaptcha(update: Update, context: CallbackContext):
    browser.get('https://www.amazon.com/errors/validateCaptcha')
    captcha = AmazonCaptcha.fromdriver(browser)
    solution = captcha.solve()


# ---- QUERYS AND BUY PROCESS ---

def amazon_disc_DE(update: Update, context: CallbackContext, status_avail):
    # ------  PS5  -------
    text = "Derzeit nicht verfügbar"
    text2 = "Currently Unavailable"
    text3 = "Choose a delivery address"
    text4 = "Wählen Sie eine Lieferadresse"
    querylink="https://amzn.to/33yATep"
    browser.get(querylink)
    textcaptcha = "Geben Sie die angezeigten Zeichen"
    if (textcaptcha in browser.page_source):
        captcha = AmazonCaptcha.fromdriver(browser)
        solution = captcha.solve()
        print(colored("[Amazon DE] captcha: ", "red") + solution)
        captchalist = list(solution)
        time.sleep(1)
        while solution == "Not solved":
            browser.get(querylink)
            captcha = AmazonCaptcha.fromdriver(browser)
            solution = captcha.solve()
            print(colored("[Amazon DE] captcha: ", "red") + colored(solution, "red"))
            time.sleep(1)
        print(colored("[Amazon DE] captcha: ", "red") + colored(solution, "green"))
        captchalist = list(solution)
        time.sleep(1)
        for i in range(len(captchalist)):
            captchasolving = browser.find_element_by_xpath('//*[@id="captchacharacters"]')
            captchasolving.send_keys(str(captchalist[i]))
            time.sleep(random.uniform(0, 1))
        print(colored("[Amazon DE] captcha: ", "red") + colored("solved", "green"))
        time.sleep(1)
        captchasubmit = browser.find_element_by_xpath('//button[normalize-space()="Weiter shoppen"]')
        captchasubmit.click()
        browser.get('https://www.amazon.de')
        #cookies = browser.find_element_by_xpath('//*[@id="sp-cc-accept"]')
        #cookies.click()
        browser.get(querylink)
    else:
        time.sleep(0.5)
        ps5digi = browser.find_element_by_xpath('//button[normalize-space()="PS5"]')
        ps5digi.click()
        time.sleep(1.8)
    if (text in browser.page_source) or (text2 in browser.page_source):
        now = datetime.now()
        timenow = now.strftime("%H-%M-%S: ")
        print(colored(timenow, "blue") + colored("PS5 Disc [Amazon DE] Unavailable", "red"))
        if status_avail == True:
            tg_bot.send_message(chat_id=tgcid, text=timenow + " PS5 Disc [Amazon DE] - Unavailable")
    else:
        now = datetime.now()
        timenow = now.strftime("%H-%M-%S: ")
        print(colored(timenow, "blue") + colored("PS5 Disc [Amazon DE] Available!!!!", "green"))
        preis = browser.find_element_by_xpath('//*[@id="priceblock_ourprice"]').text
        # Add to Card
        addtocard = browser.find_element_by_xpath('//*[@id="add-to-cart-button"]')
        addtocard.click()
        print("Added to Card!")
        # Info
        tg_bot.send_message(chat_id=tgcid, text="************* PS5 Disc ***************")
        tg_bot.send_message(chat_id=tgcid, text="PS5 Disc [Amazon DE] - Available!!!!")
        now = datetime.now()
        timenow = now.strftime("%H-%M-%S")
        imagename1 = timenow + "img.png"
        browser.save_screenshot(imagename1)
        tg_bot.send_chat_action(chat_id=tgcid, action=tg.ChatAction.TYPING)
        tg_bot.send_document(chat_id=tgcid, document=open(imagename1, "rb"))
        # preis = browser.find_element_by_xpath('//*[@id="priceblock_ourprice"]').text
        amazon_instock_info(tg_bot, updater, preis)  # telegram buy request
        time.sleep(1)
        # Login to Amazon
        msg = "Status: Login to Amazon"
        tg_bot.send_message(chat_id=tgcid, text=msg)
        log_in(browser, action, amazonuser, amazonpw)
        msg = "Status: Successful loged in on Amazon"
        tg_bot.send_message(chat_id=tgcid, text=msg)

        wait_basket = True
        while True: # Einkaufs
            buynow = wait_basket
            time.sleep(1)
            tg_command = tg_bot.get_updates(offset=offset)[-1].message.text
            print(f"waiting, telegram_request: {tg_command}, {buynow}")
            if tg_command == "/buy":
                tg_bot.send_message(chat_id=tgcid, text='Okay ich werde den Kauf veranlassen')
                tg_bot.send_message(chat_id=tgcid, text='Artikel im Warenkorb:')
                browser.get("https://www.amazon.de/gp/cart/view.html?ref_=nav_cart")
                now = datetime.now()  # current date and time
                timenow = now.strftime("%H-%M-%S")
                image_basked = timenow + "img_basked.png"
                browser.save_screenshot(image_basked)
                tg_bot.send_document(chat_id=tgcid, document=open(image_basked, "rb"))
                tg_bot.send_message(chat_id=tgcid, text='Checkout:')
                time.sleep(1)
                print("checkout")
                time.sleep(2)
                gotocheckout = browser.find_element_by_xpath('//*[@id="sc-buy-box-ptc-button"]')
                gotocheckout.click()
                now = datetime.now()  # current date and time
                timenow = now.strftime("%H-%M-%S")
                image_checkout = timenow + "img_checkout.png"
                browser.save_screenshot(image_checkout)
                tg_bot.send_document(chat_id=tgcid, document=open(image_checkout, "rb"))
                if (text3 in browser.page_source) or (text4 in browser.page_source):
                    print("Adressenauswahl")
                    adresscheckout = browser.find_element_by_xpath(
                        '//*[@id="orderSummaryPrimaryActionBtn"]')
                    adresscheckout.click()
                    time.sleep(2)
                else:
                    gobuy = browser.find_element_by_xpath('//*[@id="submitOrderButtonId"]')
                    gobuy.click()
                    time.sleep(2)
                    now = datetime.now()  # current date and time
                    timenow = now.strftime("%H-%M-%S")
                    tg_bot.send_message(chat_id=tgcid, text='buyed on:' + timenow)
                    image_buy = timenow + "img_buy.png"
                    browser.save_screenshot(image_buy)
                    tg_bot.send_document(chat_id=tgcid, document=open(image_buy, "rb"))
                    tg_bot.send_animation(chat_id=tgcid,
                                          animation='https://media.giphy.com/media/dWCaFhKKq3K8TryllR/source.gif',
                                          duration=None, width=None, height=None, thumb=None,
                                          caption=None, parse_mode=None, disable_notification=False,
                                          reply_to_message_id=None, reply_markup=None, timeout=20)
                    print("Artikel gekauft!")
                    time.sleep(26000)
                    break
            if tg_command == "/cancel":
                browser.close()
                time.sleep(1)
                browser.quit()
                time.sleep(5)
                initialize_webdriver()
                break
    time.sleep(random.uniform(0, 1.5))
def amazon_digital_DE(update: Update, context: CallbackContext, status_avail):
    # ------  PS5  -------
    text = "Derzeit nicht verfügbar"
    text2 = "Currently Unavailable"
    text3 = "Choose a delivery address"
    text4 = "Wählen Sie eine Lieferadresse"
    querylink = "https://amzn.to/33yATep"
    browser.get(querylink)
    textcaptcha = "Geben Sie die angezeigten Zeichen"
    if (textcaptcha in browser.page_source):
        captcha = AmazonCaptcha.fromdriver(browser)
        solution = captcha.solve()
        print(colored("[Amazon DE] captcha: ", "red") + solution)
        captchalist = list(solution)
        time.sleep(1)
        while solution == "Not solved":
            browser.get(querylink)
            captcha = AmazonCaptcha.fromdriver(browser)
            solution = captcha.solve()
            print(colored("[Amazon DE] captcha: ", "red") + colored(solution, "red"))
            time.sleep(1)
        print(colored("[Amazon DE] captcha: ", "red") + colored(solution, "green"))
        captchalist = list(solution)
        time.sleep(1)
        for i in range(len(captchalist)):
            captchasolving = browser.find_element_by_xpath('//*[@id="captchacharacters"]')
            captchasolving.send_keys(str(captchalist[i]))
            time.sleep(random.uniform(0, 1))
        print(colored("[Amazon DE] captcha: ", "red") + colored("solved", "green"))
        time.sleep(1)
        captchasubmit = browser.find_element_by_xpath('//button[normalize-space()="Weiter shoppen"]')
        captchasubmit.click()
        browser.get('https://www.amazon.de')
        #cookies = browser.find_element_by_xpath('//*[@id="sp-cc-accept"]')
        #cookies.click()
        browser.get(querylink)
    else:
        time.sleep(0.5)
        ps5digi = browser.find_element_by_xpath('//button[normalize-space()="PS5 - Digital Edition"]')
        ps5digi.click()
        time.sleep(1.8)
    if (text in browser.page_source) or (text2 in browser.page_source):
        now = datetime.now()
        timenow = now.strftime("%H-%M-%S: ")
        print(colored(timenow, "blue") + colored("PS5 Digi [Amazon DE] Unavailable", "red"))
        if status_avail == True:
            tg_bot.send_message(chat_id=tgcid, text=timenow + " PS5 Digi [Amazon DE] - Unavailable")
    else:
        now = datetime.now()
        timenow = now.strftime("%H-%M-%S: ")
        print(colored(timenow, "blue") + colored("PS5 Digi [Amazon DE] Available!!!!", "green"))
        preis = browser.find_element_by_xpath('//*[@id="priceblock_ourprice"]').text
        # Add to Card
        addtocard = browser.find_element_by_xpath('//*[@id="add-to-cart-button"]')
        addtocard.click()
        print("Added to Card!")
        # Info
        tg_bot.send_message(chat_id=tgcid, text="************* PS5 Digi ***************")
        tg_bot.send_message(chat_id=tgcid, text="PS5 Digi [Amazon DE] - Available!!!!")
        now = datetime.now()
        timenow = now.strftime("%H-%M-%S")
        imagename1 = timenow + "img.png"
        browser.save_screenshot(imagename1)
        tg_bot.send_chat_action(chat_id=tgcid, action=tg.ChatAction.TYPING)
        tg_bot.send_document(chat_id=tgcid, document=open(imagename1, "rb"))
        # preis = browser.find_element_by_xpath('//*[@id="priceblock_ourprice"]').text
        amazon_instock_info(tg_bot, updater, preis)  # telegram buy request
        time.sleep(1)
        # Login to Amazon
        msg = "Status: Login to Amazon"
        tg_bot.send_message(chat_id=tgcid, text=msg)
        log_in(browser, action, amazonuser, amazonpw)
        msg = "Status: Successful loged in on Amazon"
        tg_bot.send_message(chat_id=tgcid, text=msg)

        wait_basket = True
        while True:  # Einkaufs
            buynow = wait_basket
            time.sleep(1)
            tg_command = tg_bot.get_updates(offset=offset)[-1].message.text
            print(f"waiting, telegram_request: {tg_command}, {buynow}")
            if tg_command == "/buy":
                tg_bot.send_message(chat_id=tgcid, text='Okay ich werde den Kauf veranlassen')
                tg_bot.send_message(chat_id=tgcid, text='Artikel im Warenkorb:')
                browser.get("https://www.amazon.de/gp/cart/view.html?ref_=nav_cart")
                now = datetime.now()  # current date and time
                timenow = now.strftime("%H-%M-%S")
                image_basked = timenow + "img_basked.png"
                browser.save_screenshot(image_basked)
                tg_bot.send_document(chat_id=tgcid, document=open(image_basked, "rb"))
                tg_bot.send_message(chat_id=tgcid, text='Checkout:')
                time.sleep(1)
                print("checkout")
                time.sleep(2)
                gotocheckout = browser.find_element_by_xpath('//*[@id="sc-buy-box-ptc-button"]')
                gotocheckout.click()
                now = datetime.now()  # current date and time
                timenow = now.strftime("%H-%M-%S")
                image_checkout = timenow + "img_checkout.png"
                browser.save_screenshot(image_checkout)
                tg_bot.send_document(chat_id=tgcid, document=open(image_checkout, "rb"))
                if (text3 in browser.page_source) or (text4 in browser.page_source):
                    print("Adressenauswahl")
                    adresscheckout = browser.find_element_by_xpath(
                        '//*[@id="orderSummaryPrimaryActionBtn"]')
                    adresscheckout.click()
                    time.sleep(2)
                else:
                    gobuy = browser.find_element_by_xpath('//*[@id="submitOrderButtonId"]')
                    gobuy.click()
                    time.sleep(2)
                    now = datetime.now()  # current date and time
                    timenow = now.strftime("%H-%M-%S")
                    tg_bot.send_message(chat_id=tgcid, text='buyed on:' + timenow)
                    image_buy = timenow + "img_buy.png"
                    browser.save_screenshot(image_buy)
                    tg_bot.send_document(chat_id=tgcid, document=open(image_buy, "rb"))
                    tg_bot.send_animation(chat_id=tgcid,
                                          animation='https://media.giphy.com/media/dWCaFhKKq3K8TryllR/source.gif',
                                          duration=None, width=None, height=None, thumb=None,
                                          caption=None, parse_mode=None, disable_notification=False,
                                          reply_to_message_id=None, reply_markup=None, timeout=20)
                    print("Artikel gekauft!")
                    time.sleep(26000)
                    break
            if tg_command == "/cancel":
                browser.close()
                time.sleep(1)
                browser.quit()
                time.sleep(5)
                initialize_webdriver()
                break
    time.sleep(random.uniform(0, 1.5))

def amazon_disc_FR(update: Update, context: CallbackContext, status_avail):
    # ------  PS5  -------
    querylink="https://www.amazon.fr/PlayStation-%C3%89dition-Standard-DualSense-Couleur/dp/B08H93ZRK9/ref=sr_1_1?dchild=1&keywords=Ps5+Console&qid=1612890317&sr=8-1"
    browser.get(querylink)
    textcaptcha = "Saisissez les caractères"
    if (textcaptcha in browser.page_source):
        captcha = AmazonCaptcha.fromdriver(browser)
        solution = captcha.solve()
        while solution == "Not solved":
            browser.get(querylink)
            captcha = AmazonCaptcha.fromdriver(browser)
            solution = captcha.solve()
            print(colored("[Amazon FR] captcha: ", "red") + colored(solution, "red"))
            time.sleep(1)
        print(colored("[Amazon FR] captcha: ", "red") + colored(solution, "green"))
        captchalist = list(solution)
        time.sleep(1)
        for i in range(len(captchalist)):
            captchasolving = browser.find_element_by_xpath('//*[@id="captchacharacters"]')
            captchasolving.send_keys(str(captchalist[i]))
            time.sleep(random.uniform(0, 1))
        print(colored("[Amazon FR] captcha: ", "red") + colored("solved", "green"))
        time.sleep(1)
        captchasubmit = browser.find_element_by_xpath('//button[normalize-space()="Continuer les achats"]')
        captchasubmit.click()
        browser.get(querylink)
        time.sleep(0.5)
    else:
        ps5normal = browser.find_element_by_xpath('//button[normalize-space()="PS5"]')
        ps5normal.click()
        time.sleep(1.6)
        text = "Actuellement indisponible"
        text2 = "Currently Unavailable"
        if (text in browser.page_source) or (text2 in browser.page_source):
            now = datetime.now()
            timenow = now.strftime("%H-%M-%S: ")
            print(colored(timenow, "blue") + colored("PS5 Disc [Amazon FR] Unavailable", "red"))
            if status_avail == True:
                tg_bot.send_message(chat_id=tgcid, text=timenow + " PS5 Disc [Amazon FR] - Unavailable")
        else:
            now = datetime.now()
            timenow = now.strftime("%H-%M-%S: ")
            print(colored(timenow, "blue") + colored("PS5 Disc [Amazon FR] Available!!!!", "green"))
            tg_bot.send_message(chat_id=tgcid, text="PS5 Disc [Amazon FR] Available!!!!")
            tg_bot.send_message(chat_id=tgcid, text=querylink)
            tg_bot.send_message(chat_id=tgcid, text="*********************************")
            time.sleep(1)
        time.sleep(random.uniform(0, 1.5))
def amazon_digital_FR(update: Update, context: CallbackContext, status_avail):
    # ------  PS5  -------
    querylink="https://www.amazon.fr/PlayStation-%C3%89dition-Standard-DualSense-Couleur/dp/B08H93ZRK9/ref=sr_1_1?dchild=1&keywords=Ps5+Console&qid=1612890317&sr=8-1"
    browser.get(querylink)
    textcaptcha = "Saisissez les caractères"
    if (textcaptcha in browser.page_source):
        captcha = AmazonCaptcha.fromdriver(browser)
        solution = captcha.solve()
        while solution == "Not solved":
            browser.get(querylink)
            captcha = AmazonCaptcha.fromdriver(browser)
            solution = captcha.solve()
            print(colored("[Amazon FR] captcha: ", "red") + colored(solution, "red"))
            time.sleep(1)
        print(colored("[Amazon FR] captcha: ", "red") + colored(solution, "green"))
        captchalist = list(solution)
        time.sleep(1)
        for i in range(len(captchalist)):
            captchasolving = browser.find_element_by_xpath('//*[@id="captchacharacters"]')
            captchasolving.send_keys(str(captchalist[i]))
            time.sleep(random.uniform(0, 1))
        print(colored("[Amazon FR] captcha: ", "red") + colored("solved", "green"))
        time.sleep(1)
        captchasubmit = browser.find_element_by_xpath('//button[normalize-space()="Continuer les achats"]')
        captchasubmit.click()
        browser.get(querylink)
        time.sleep(0.5)
    else:
        ps5normal = browser.find_element_by_xpath('//button[normalize-space()="PS5 - Digital Edition"]')
        ps5normal.click()
        time.sleep(1.6)
        text = "Actuellement indisponible"
        text2 = "Currently Unavailable"
        if (text in browser.page_source) or (text2 in browser.page_source):
            now = datetime.now()
            timenow = now.strftime("%H-%M-%S: ")
            print(colored(timenow, "blue") + colored("PS5 Digi [Amazon FR] Unavailable", "red"))
            if status_avail == True:
                tg_bot.send_message(chat_id=tgcid, text=timenow + " PS5 Digi [Amazon FR] - Unavailable")
        else:
            now = datetime.now()
            timenow = now.strftime("%H-%M-%S: ")
            print(colored(timenow, "blue") + colored("PS5 Digital [Amazon FR] Available!!!!", "green"))
            tg_bot.send_message(chat_id=tgcid, text="PS5 Digital [Amazon FR] Available!!!!")
            tg_bot.send_message(chat_id=tgcid, text=querylink)
            tg_bot.send_message(chat_id=tgcid, text="*********************************")
            time.sleep(1)
        time.sleep(random.uniform(0, 1.5))

def amazon_disc_IT(update: Update, context: CallbackContext, status_avail):
    # ------  PS5  -------
    querylink="https://www.amazon.it/Sony-PlayStation-5-Digital-Edition/dp/B08KJF2D25"
    #https://www.amazon.it/Playstation-Sony-PlayStation-5/dp/B08KKJ37F7/ref=sr_1_1?brr=1&dchild=1&qid=1613215006&rd=1&s=videogames&sr=1-1
    browser.get(querylink)
    textcaptcha = "Digita i caratteri"
    if (textcaptcha in browser.page_source):
        captcha = AmazonCaptcha.fromdriver(browser)
        solution = captcha.solve()
        while solution == "Not solved":
            browser.get(querylink)
            captcha = AmazonCaptcha.fromdriver(browser)
            solution = captcha.solve()
            print(colored("[Amazon IT] captcha: ", "red") + colored(solution, "red"))
            time.sleep(1)
        print(colored("[Amazon IT] captcha: ", "red") + colored(solution, "green"))
        captchalist = list(solution)
        time.sleep(1)
        for i in range(len(captchalist)):
            captchasolving = browser.find_element_by_xpath('//*[@id="captchacharacters"]')
            captchasolving.send_keys(str(captchalist[i]))
            time.sleep(random.uniform(0, 1))
        print(colored("[Amazon IT] captcha: ", "red") + colored("solved", "green"))
        time.sleep(1)
        captchasubmit = browser.find_element_by_xpath('//button[normalize-space()="Continua con gli acquisti"]')
        captchasubmit.click()
        browser.get(querylink)
        time.sleep(0.5)
    else:
        time.sleep(1.6)
        text = "Non disponibile"
        text2 = "Currently Unavailable"
        if (text in browser.page_source) or (text2 in browser.page_source):
            now = datetime.now()
            timenow = now.strftime("%H-%M-%S: ")
            print(colored(timenow, "blue") + colored("PS5 Disc [Amazon IT] Unavailable", "red"))
            if status_avail == True:
                tg_bot.send_message(chat_id=tgcid, text=timenow + " PS5 Disc [Amazon IT] - Unavailable")
        else:
            now = datetime.now()
            timenow = now.strftime("%H-%M-%S: ")
            print(colored(timenow, "blue") + colored("PS5 Disc [Amazon IT] Available!!!!", "green"))
            tg_bot.send_message(chat_id=tgcid, text="PS5 Disc [Amazon IT] Available!!!!")
            tg_bot.send_message(chat_id=tgcid, text=querylink)
            tg_bot.send_message(chat_id=tgcid, text="*********************************")
            time.sleep(1)
        time.sleep(random.uniform(0, 1.5))
def amazon_digital_IT(update: Update, context: CallbackContext, status_avail):
    # ------  PS5  -------
    querylink="https://www.amazon.it/Playstation-Sony-PlayStation-5/dp/B08KKJ37F7/ref=sr_1_1?brr=1&dchild=1&qid=1613215006&rd=1&s=videogames&sr=1-1"
    browser.get(querylink)
    textcaptcha = "Digita i caratteri"
    if (textcaptcha in browser.page_source):
        captcha = AmazonCaptcha.fromdriver(browser)
        solution = captcha.solve()
        while solution == "Not solved":
            browser.get(querylink)
            captcha = AmazonCaptcha.fromdriver(browser)
            solution = captcha.solve()
            print(colored("[Amazon IT] captcha: ", "red") + colored(solution, "red"))
            time.sleep(1)
        print(colored("[Amazon IT] captcha: ", "red") + colored(solution, "green"))
        captchalist = list(solution)
        time.sleep(1)
        for i in range(len(captchalist)):
            captchasolving = browser.find_element_by_xpath('//*[@id="captchacharacters"]')
            captchasolving.send_keys(str(captchalist[i]))
            time.sleep(random.uniform(0, 1))
        print(colored("[Amazon IT] captcha: ", "red") + colored("solved", "green"))
        time.sleep(1)
        captchasubmit = browser.find_element_by_xpath('//button[normalize-space()="Continua con gli acquisti"]')
        captchasubmit.click()
        browser.get(querylink)
        time.sleep(0.5)
    else:
        time.sleep(1.6)
        text = "Non disponibile"
        text2 = "Currently Unavailable"
        if (text in browser.page_source) or (text2 in browser.page_source):
            now = datetime.now()
            timenow = now.strftime("%H-%M-%S: ")
            print(colored(timenow, "blue") + colored("PS5 Digi [Amazon IT] Unavailable", "red"))
            if status_avail == True:
                tg_bot.send_message(chat_id=tgcid, text=timenow + " PS5 Digi [Amazon IT] - Unavailable")
        else:
            now = datetime.now()
            timenow = now.strftime("%H-%M-%S: ")
            print(colored(timenow, "blue") + colored("PS5 Digi [Amazon IT] Available!!!!", "green"))
            tg_bot.send_message(chat_id=tgcid, text="PS5 Digi [Amazon IT] Available!!!!")
            tg_bot.send_message(chat_id=tgcid, text=querylink)
            tg_bot.send_message(chat_id=tgcid, text="*********************************")
            time.sleep(1)
        time.sleep(random.uniform(0, 1.5))

def mediamarkt_query(update: Update, context: CallbackContext):
    text = "nicht verfügbar"
    text2 = "add to card"
    text3 = "Choose a delivery address"
    text4 = "Wählen Sie eine Lieferadresse"
    browser.get("https://www.mediamarkt.de/de/product/_sony-playstation%C2%AE5-digital-edition-2661939.html")
    if not(text in browser.page_source) or (text2 in browser.page_source):
        now = datetime.now()
        timenow = now.strftime("%H-%M-%S: ")
        print(colored(timenow, "blue") + colored("PS5 Digital [Mediamarkt] Available!!!!", "green"))
        cookies = browser.find_element_by_xpath('// * [ @ id = "privacy-layer-accept-all-button"]')
        cookies.click()
        preis = browser.find_element_by_xpath('//*[@id="root"]/div[2]/div[3]/div[1]/div/div[4]/div/div/div[1]/div/div/div/div/div/div[2]/div[2]/span[2]').text
        addtocard = browser.find_element_by_xpath('//*[@id="pdp-add-to-cart-button"]')
        addtocard.click()
        timenow = now.strftime("%H-%M-%S")
        imagename1 = timenow + "img.png"
        browser.save_screenshot(imagename1)
        tg_bot.send_message(chat_id=tgcid, text="#PS5 Digital [Mediamarkt] Available!!!!")
        tg_bot.send_document(chat_id=tgcid, document=open(imagename1, "rb"))
        tg_bot.send_message(chat_id=tgcid, text="https://www.mediamarkt.de/de/product/_sony-playstation%C2%AE5-digital-edition-2661939.html")

        while True:
            time.sleep(1)
            print("waiting")

    else:
        now = datetime.now()
        timenow = now.strftime("%H-%M-%S: ")
        print(colored(timenow, "blue") + colored("PS5 Digi [Mediamarkt] Unavailable", "red"))
        if status_avail == True:
            tg_bot.send_message(chat_id=tgcid, text=timenow + " PS5 Digi [Mediamarkt] - Unavailable")

def saturn_disc(update: Update, context: CallbackContext):
    text = "Dieser Artikel ist aktuell nicht verfügbar"
    text2 = "add to card"
    text3 = "Choose a delivery address"
    text4 = "Wählen Sie eine Lieferadresse"
    browser.get("http://bit.ly/SaturnPS5")
    if not(text in browser.page_source) or (text2 in browser.page_source):
        now = datetime.now()
        timenow = now.strftime("%H-%M-%S: ")
        print(colored(timenow, "blue") + colored("PS5 Disc [Saturn] Available!!!!", "green"))
        cookies = browser.find_element_by_xpath('// * [ @ id = "privacy-layer-accept-all-button"]')
        cookies.click()
        preis = browser.find_element_by_xpath('//*[@id="root"]/div[2]/div[3]/div[1]/div/div[4]/div/div/div[1]/div/div/div/div/div/div[2]/div[2]/span[2]').text
        addtocard = browser.find_element_by_xpath('//*[@id="pdp-add-to-cart-button"]')
        addtocard.click()
        timenow = now.strftime("%H-%M-%S")
        imagename1 = timenow + "img.png"
        browser.save_screenshot(imagename1)
        tg_bot.send_message(chat_id=tgcid, text="#PS5 Disc [Saturn] Available!!!!")
        tg_bot.send_document(chat_id=tgcid, document=open(imagename1, "rb"))
        tg_bot.send_message(chat_id=tgcid, text="http://bit.ly/SaturnPS5")

        while True:
            time.sleep(1)
            print("waiting")

    else:
        now = datetime.now()
        timenow = now.strftime("%H-%M-%S: ")
        print(colored(timenow, "blue") + colored("PS5 Disc [SATURN] Unavailable", "red"))
        if status_avail == True:
            tg_bot.send_message(chat_id=tgcid, text=timenow + " PS5 Disc [Saturn] - Unavailable")
def saturn_digital(update: Update, context: CallbackContext):
    text = "Dieser Artikel ist aktuell nicht verfügbar"
    text2 = "add to card"
    text3 = "Choose a delivery address"
    text4 = "Wählen Sie eine Lieferadresse"
    browser.get("https://bit.ly/35ZvzDD")
    if not(text in browser.page_source) or (text2 in browser.page_source):
        now = datetime.now()
        timenow = now.strftime("%H-%M-%S: ")
        print(colored(timenow, "blue") + colored("PS5 Digital [Saturn] Available!!!!", "green"))
        cookies = browser.find_element_by_xpath('// * [ @ id = "privacy-layer-accept-all-button"]')
        cookies.click()
        preis = browser.find_element_by_xpath('//*[@id="root"]/div[2]/div[3]/div[1]/div/div[4]/div/div/div[1]/div/div/div/div/div/div[2]/div[2]/span[2]').text
        addtocard = browser.find_element_by_xpath('//*[@id="pdp-add-to-cart-button"]')
        addtocard.click()
        timenow = now.strftime("%H-%M-%S")
        imagename1 = timenow + "img.png"
        browser.save_screenshot(imagename1)
        tg_bot.send_message(chat_id=tgcid, text="#PS5 Digital [Saturn] Available!!!!")
        tg_bot.send_document(chat_id=tgcid, document=open(imagename1, "rb"))
        tg_bot.send_message(chat_id=tgcid, text="http://bit.ly/SaturnPS5")

        while True:
            time.sleep(1)
            print("waiting")

    else:
        now = datetime.now()
        timenow = now.strftime("%H-%M-%S: ")
        print(colored(timenow, "blue") + colored("PS5 Digi [SATURN] Unavailable", "red"))
        if status_avail == True:
            tg_bot.send_message(chat_id=tgcid, text=timenow + " PS5 Digi [Saturn] - Unavailable")

def otto_digital(update: Update, context: CallbackContext):
    text = "leider ausverkauft"
    browser.get("https://www.otto.de/technik/gaming/playstation/ps5/")
    if not (text in browser.page_source) :
        now = datetime.now()
        timenow = now.strftime("%H-%M-%S: ")
        print(colored(timenow, "blue") + colored("PS5 Digital [Otto] - Available!!!!", "green"))
        imagename1 = timenow + "img.png"
        browser.save_screenshot(imagename1)
        tg_bot.send_document(chat_id=tgcid, document=open(imagename1, "rb"))
        tg_bot.send_message(chat_id=tgcid, text="https://www.otto.de/technik/gaming/playstation/ps5/")
    else:
        now = datetime.now()
        timenow = now.strftime("%H-%M-%S: ")
        print(colored(timenow, "blue") + colored("PS5 Digi [Otto] Unavailable", "red"))
        if status_avail == True:
            tg_bot.send_message(chat_id=tgcid, text=timenow + " PS5 Digi [Otto] - Unavailable")

def euronics_query(update: Update, context: CallbackContext):
    text = "nicht verfügbar"
    browser.get("https://www.euronics.de/spiele-und-konsolen-film-und-musik/spiele-und-konsolen/playstation-5/spielekonsole/playstation-5-digital-edition-konsole-4061856837833")
    time.sleep(1.8)
    if not (text in browser.page_source):
        now = datetime.now()
        timenow = now.strftime("%H-%M-%S: ")
        print(colored(timenow, "blue") + colored("PS5 Digital [Euronics] - Available!!!!", "green"))
        imagename1 = timenow + "img.png"
        browser.save_screenshot(imagename1)
        tg_bot.send_document(chat_id=tgcid, document=open(imagename1, "rb"))
        tg_bot.send_message(chat_id=tgcid, text="PS5 Digital [Euronics] - Available!!!!")
        tg_bot.send_message(chat_id=tgcid, text="https://www.euronics.de/spiele-und-konsolen-film-und-musik/spiele-und-konsolen/playstation-5/spielekonsole/playstation-5-digital-edition-konsole-4061856837833")
    else:
        now = datetime.now()
        timenow = now.strftime("%H-%M-%S: ")
        print(colored(timenow, "blue") + colored("PS5 Digital [Euronics] Unavailable", "red"))
def gamestop_query(update: Update, context: CallbackContext):
    text = "Leider sind keine Playstation 5 mehr verfügbar"
    browser.get("https://www.gamestop.de/PS5/Index")
    time.sleep(1.8)
    if not (text in browser.page_source) :
        now = datetime.now()
        timenow = now.strftime("%H-%M-%S: ")
        print(colored(timenow, "blue") + colored("PS5 Digital [Gamestop] - Available!!!!", "green"))
        imagename1 = timenow + "img.png"
        browser.save_screenshot(imagename1)
        tg_bot.send_document(chat_id=tgcid, document=open(imagename1, "rb"))
        tg_bot.send_message(chat_id=tgcid, text="PS5 Digital [Gamestop] - Available!!!!")
        tg_bot.send_message(chat_id=tgcid, text="https://www.gamestop.de/PS5/Index")
    else:
        now = datetime.now()
        timenow = now.strftime("%H-%M-%S: ")
        print(colored(timenow, "blue") + colored("PS5 Digital [Gamestop] Unavailable", "red"))

# ---- Amazon item in stock ---
def amazon_instock_info(update: Update, context: CallbackContext, preis) -> int:
    # Welcome message
    msg = "Playstaion 5 verfügbar !\n"
    msg += "Preis: "
    msg += preis
    msg += " \n"
    msg += "Artikel wurde zum Warenkorb hinzugefügt\n"
    msg += "Soll ich den Kauf abschließen?\n\n"
    msg += "/buy - let's play 🎮\n"
    msg += "/cancel - mimimi 😒\n\n"
    # Commands menu
    main_menu_keyboard = [[tg.KeyboardButton('/buy', callback_data=str(buy))], [tg.KeyboardButton('/cancel')]]
    reply_kb_markup = tg.ReplyKeyboardMarkup(main_menu_keyboard, resize_keyboard=True, one_time_keyboard=True)
    # Send the message with menu
    tg_bot.send_message(chat_id=tgcid, text=msg, reply_markup=reply_kb_markup)


# --- main ---
tg_bot, tgcid, offset = initialize_telegram(tgtoken, tgcid)
tg_last_command = "bv"
v = 1

browser_runnging = False

bot_startupmessage(tg_bot, updater)

while v == 1:

    # browser = initialize_webdriver()
    time.sleep(1)
    # tg_bot.send_message(chat_id=tgcid, text="Send /start to begin!")

    tg_command = tg_bot.get_updates(offset=offset)[-1].message.text
    if debugging:
        print(colored("last: "+ tg_last_command + ", new: " + tg_command, "yellow") )
    if tg_last_command != tg_command:
        if tg_command == "/start":
            tg_last_command = tg_command
            start(tg_bot, updater)
            #querys(tg_bot, updater, loop_n_max, global_loop_n)
            for a in range(100000):
                try:
                    status_avail = False
                    if tg_bot.get_updates(offset=offset)[-1].message.text == "/stop":
                        break
                    if tg_bot.get_updates(offset=offset)[-1].message.text == "/status":
                        status_avail = True
                        tg_bot.send_message(chat_id=tgcid, text=f"Status: n= {a} /end messaging")

                    amazon_disc_DE(tg_bot, updater, status_avail)
                    amazon_digital_DE(tg_bot, updater, status_avail)
                    amazon_disc_FR(tg_bot, updater, status_avail)
                    amazon_digital_FR(tg_bot, updater, status_avail)
                    amazon_disc_IT(tg_bot, updater, status_avail)
                    amazon_digital_IT(tg_bot, updater, status_avail)

                    mediamarkt_query(tg_bot, updater)
                    #saturn_disc(tg_bot, updater)

                    time.sleep(random.uniform(0, 2))
                    #saturn_digital(tg_bot, updater)
                    time.sleep(random.uniform(0, 2))
                    otto_digital(tg_bot, updater)
                    time.sleep(random.uniform(0, 2))
                    euronics_query(tg_bot, updater)
                    time.sleep(random.uniform(1, 2))
                    gamestop_query(tg_bot, updater)
                    now = datetime.now()
                    timenow = now.strftime("%H-%M-%S: ")
                    text = f"----- n: {a} -----"
                    print(colored(timenow, "blue") + colored(text, "yellow"))
                    a=+ 1
                except Exception as e:
                    print(e)
                    browser.close()
                    time.sleep(1)
                    browser.quit()
                    time.sleep(5)
                    initialize_webdriver()
        if tg_command == "/getquery":
            tg_last_command = tg_command
            getquery(tg_bot, updater)
        if tg_command == "/stop":
            tg_last_command = tg_command
            stopping(tg_bot, updater, browser_runnging)

