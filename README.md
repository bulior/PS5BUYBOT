# PS5BUYBOT
Python PS5 Web crawler with auto buy option<br>
Version 1.2 2021-02<br>

This is one easy way to check differnt Retailers and buy automaticly e.g. the PS5 / PS5 digi.<br>
It is not cleanly programmed but works for me very well. I am always open for feedback ;)<br>


# ----- Instruction ------

1. Download <br>
    - main.py and config.ini file<br><br>
    
2. Setup<br>
    2.1 install ChromeDriver for Chromebrowser:<br>
        https://www.youtube.com/watch?v=dz59GsdvUF8<br>
    2.2 install all Libs:<br>
        - SELENIUM<br>
        - PYTHON-TELEGRAM-BOT<br>
        - TERMCOLOR<br>
        
3. PreConfig:<br>
   Edit config.ini
    - Telegram
      - Bot Token
      - Bot Chat ID
    - Account Data for AutoBuy on Amazon
      - username
      - password
    - Pathes
      - chromedriver path
      - path for screenshots
      
      
# ----- in Action ------

Telegram notification on Startup:<br>
<a href="https://i.ibb.co/mN41Kjv/2021-02-07-10-23-45-Window.png"><img src="https://i.ibb.co/mN41Kjv/2021-02-07-10-23-45-Window.png" alt="2021-02-07-10-23-45-Window" border="0"></a><br><br>

get status updates with telegram:<br>
Until now you must send an /end option to stop status messaging<br>
<a href="https://i.ibb.co/qp4yQWK/2021-02-07-10-27-30-Window.png"><img src="https://i.ibb.co/qp4yQWK/2021-02-07-10-27-30-Window.png" alt="2021-02-07-10-27-30-Window" border="0"></a><br><br>

python terminal looks like this:<br>
<a href="https://i.ibb.co/xFnWyGt/2021-02-07-10-29-01-Window.png"><img src="https://i.ibb.co/xFnWyGt/2021-02-07-10-29-01-Window.png" alt="2021-02-07-10-29-01-Window" border="0"></a><br><br>

If the Item is in stock, the bot will inform you and on Amazon the bot will add it to your basket, will automaticly log in, will inform you with price tag and ask to buy:<br>
For every step you will receive screenshots.<br><br>
An example purchase looks like this:<br>
<a href="https://i.ibb.co/JKBw1Vh/2021-02-07-10-37-02-Window.png"><img src="https://i.ibb.co/JKBw1Vh/2021-02-07-10-37-02-Window.png" alt="2021-02-07-10-37-02-Window" border="0"></a><br><br>

If you buy it:<br>
<a href="https://i.ibb.co/BgrygFK/2021-02-07-10-41-49-Window.png"><img src="https://i.ibb.co/BgrygFK/2021-02-07-10-41-49-Window.png" alt="2021-02-07-10-41-49-Window" border="0"></a><br><br>



<a href="https://www.paypal.com/donate?hosted_button_id=3S68EYYDSLM8W">
  <img src="https://raw.githubusercontent.com/stefan-niedermann/paypal-donate-button/master/paypal-donate-button.png" alt="Donate with PayPal" />
</a>
