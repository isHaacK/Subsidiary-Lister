import sys
import requests
from bs4 import BeautifulSoup

# the script might break in some languages (depends on the ip)

# ./filiales.py "company name"
try:
	company = sys.argv[1]
except:
	print("Please provide company name")
	exit(0)

response = requests.get(f"https://www.google.com/search?q={company}+subsidiaries", \
						cookies={"CONSENT":"YES+a.a"}, \
						headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"})

html_text = response.text
soup = BeautifulSoup(html_text, 'html.parser')

tabs = soup.find_all('a', {"role":"tab"})
if tabs:
	for t in tabs:
		try:
			print(t["aria-label"])

		except:
      # debug purposes since google is always changing stuff
			print("something went wrong, saving error.html\n")
			print("maybe VPN language?")
			file = open("error.html","w")
			file.write(html_text)
			file.close()
			exit(0)
else:
	if "CAPTCHA" in html_text:
		print("IP blacklisted from google")
	else:
		print(f"Nothing found for {company}, try full company name or change VPN location")
		#print(f"Debug: maybe VPN language? showing some response text. \n{soup.text[len(company)+16:130]}")
