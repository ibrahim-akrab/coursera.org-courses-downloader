# import useful modules
import re
from robobrowser import RoboBrowser
import sys


def main():
        # initialize a browser to be used in exploring the weebsite
        browser = RoboBrowser()

        # the url address of the login webpage
        login_url = 'https://www.coursera.org/?authMode=login'
        # the url address that the POST request will be submitted to
        # you can get it using developer tools in your favourite web browser
        submission_url = 'https://www.coursera.org/api/login/v3Ssr'
        # the url of the dashboard that contains all courses you are enrolled in
        recommendation_url = 'https://www.coursera.org/recommendations'

        # the header that will be used to when interacting with edx.org
        # to make it feel like the program is real browser
        # you can get it from browser developer tools as weel
        headers = {'Host': 'www.coursera.org',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'Accept-Language': 'en-US,en;q=0.5',
                   'Accept-Encoding': 'gzip, deflate, br',
                   'Content-Type': 'application/x-www-form-urlencoded',
                   'Content-Length': '47',
                   'Referer': 'https://www.coursera.org/?authMode=login',
                   'Cookie': 'CSRF3-Token=1503349304.16YZd5LEMfmabex8; __204u=8517206208-1502485304770; __204r=; __400v=105a77a0-865f-40de-9595-c15e21c3c209; __400vt=1502481783731; ip_origin=US; ip_currency=USD; stc113717=tsa:1502481710737.1521665636.6082046.2235132885858815.:20170811203301|env:1%7C20170911200150%7C20170811203301%7C2%7C1030880:20180811200301|uid:1502481710736.260078514.54091024.113717.431429710.:20180811200301|srchist:1030880%3A1%3A20170911200150:20180811200301; _uetsid=_uetc8e3959d',
                   'DNT': '1',
                   'Connection': 'keep-alive',
                   'Upgrade-Insecure-Requests': '1'
                   }

        # the dict data that will be submitted for the website to log in the account
        # will add ways to enter these data dynamically
        payload = {'email': 'ibrahim.mahmoud97@eng-st.cu.edu.eg',
                   'password': "AhmEd2002"
                   }
        params = {'csrf3-token': '1503349304.16YZd5LEMfmabex8',
                   'src': 'undefined'
                   }

        # send POST request to the submission url with the data and the header
        response = browser.session.post(submission_url, params=params, data = payload, headers = headers)
        browser._update_state(response)

        #if not browser.response.ok: sys.exit(1)     
        print(response)
        # update the state of the browser with the response
        # now that we are logged in
        browser.open(recommendation_url)
        #if not browser.response.ok: sys.exit(1)
        print(browser.response)
        print(browser.response.text)
	








if __name__ == "__main__": main()
