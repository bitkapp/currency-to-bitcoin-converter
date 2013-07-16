import json,urllib2
from Tkinter import *
from collections import OrderedDict

# Created By BitKapp.com
# This software is released under GNU License
# (c) 2013
# Donate at 1Bc9Jr8rxcp3be4DUHfVdSh3sZ9My9pqog

currencies = OrderedDict([('US Dollar','USD'),('British Pound','GBP'),('Euro','EUR')])
currency = currencies[currencies.keys()[0]]
curr_links = {'USD':'https://data.mtgox.com/api/2/BTCUSD/money/ticker_fast',
  	'GBP':'https://data.mtgox.com/api/2/BTCGBP/money/ticker_fast',
		'EUR':'https://data.mtgox.com/api/2/BTCEUR/money/ticker_fast' }

#Function that requests the latest bitcoin Mt Gox price
def req_price(url):
	url_read = urllib2.urlopen(url)
	read = url_read.read()
	dec_json = json.loads(read)['data']['last']['value']
	return dec_json
	

class App(object):
	def __init__(self):
		#Setting up GUI
		self.root = Tk()
		self.root.wm_title('BitKapp Currency to Bitcoin Converter')
		#Entry and button widget
		self.entry = Entry(master = self.root)
		self.button = Button(master = self.root, text = "Calculate",command = self.click)
		#Labels
		self.v = StringVar()
		self.v.set(u'\u0E3F '+str(0))
		self.label = Label(master = self.root, textvariable = self.v,font=(13))
		self.entry_v = StringVar()
		self.entry_v.set('Insert Amount '+'('+currency+')'+' :')
		self.entry_label = Label(master=self.root,textvariable= self.entry_v, font=(13))
		#Menu
		self.var = StringVar()
		self.currencies = currencies.keys()
		self.var.set(self.currencies[0])
		args = [self.root,self.var] + self.currencies
		keyw = {'command':self.curr}
		self.menu = OptionMenu(*args,**keyw)
	
	#Currency menu update function
	def curr(self,e):
		global currency
		currency = currencies[self.var.get()]
		self.entry_v.set('Insert Amount '+'('+currency+')'+' : ')
		
	#Button click function
	def click(self):
		price = req_price(curr_links[currency])
		x = float(self.entry.get())/float(price)
		self.v.set(u'\u0E3F '+str(x))
	
	def run(self):
		self.entry.grid(row=1, column=2)
		self.entry_label.grid(row=1, column=1)
		self.button.grid(row = 2,column=2)
		self.label.grid(row=3,column=1,columnspan=2)
		self.menu.grid(row=2,column=1)
		self.root.mainloop()
		
if __name__ == '__main__':
	try:
		App().run()
	except:
		App().quit()
		
		
