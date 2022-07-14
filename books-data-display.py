from tkinter import *
from tkinter import messagebox
#import tkinter.scrolledtext as scrolledtext
from tkinter import ttk
from PIL import ImageTk, Image

import time

import requests
import json
import pyperclip

import quickemailverification

import sys
import os

client = quickemailverification.Client('345e555725b06738e93b8c7a74b00bd56c2910670389656930929d71ffe1') # Replace API_KEY with your API Key
quickemailverification = client.quickemailverification()


root = Tk()


w = 1600
h = 900
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

root.geometry('%dx%d+%d+%d' % (w,h,x,y))
root.title('Book query log')
#root.eval('tk::PlaceWindow.center')
#root.bitmap('')
root.configure(bg='green')
root.state('zoomed')
#line 23-36 helps to perfectly fit the root window to the 


def print_name(event=None):
	ask_for_name.place_forget()
	name_entey.place_forget()
	submit_button.place_forget()
	global welcome_label
	welcome_label = Label(root,text='Welcome '+ name_entey.get(),bg='green',fg='white',font=('Helvetica',25,'bold'))
	welcome_label.place(x=600,y=600)
	ask_for_email()


def ask_for_email():
	global email_entries
	global email_ask_label
	global email_submit_button
	email_ask_label = Label(root,text='Please enter a valid email:',bg='green',fg='white',font=('Helvetica',20))
	email_ask_label.place(x=430,y=650) 

	email_entries = Entry(root,width=30,font=('Helvetica',18))
	email_entries.place(x=780,y=656)
	# get a habbit of always paking/gridding/placing in the next line, otherwise always a None-type() object
	# will be returned and you'll apend hours to figure out this simple problem


	email_submit_button = Button(root,text='Submit',width=20,command=email_verifier)
	root.bind('<Return>', lambda event=None: email_submit_button.invoke())
	email_submit_button.place(x=780,y=700)


def print_book_data():

	for i in range(0,len(all_book_titles)):
		if books_menu.get() == all_book_titles[i]:
			global book_number
			book_number = i
			break
	for widgets in root.winfo_children():
		widgets.place_forget()


	title_lable = Label(root,text=response['items'][book_number]['volumeInfo']['title'],font=('Helvetica',50,"bold"),bg='green',fg='white')
	title_lable.place(x=20,y=20)
	#title_lable.pack()
	#title_lable.grid(row=1,column=2)

	try:
		if len(response['items'][i]['volumeInfo']['authors']) != 0:
			authors = Label(root,text="Author(s): ",font=('Helvetica',15,"bold"),bg='green',fg='red')
			authors.place(x=20,y=150)
			#authors.pack()
			#authors.grid(row=5,column=1)
			author_name = Message(root,text=str(response['items'][i]['volumeInfo']['authors']),font=('Helvetica',15,"bold"),bg='green',fg='white',width=500)
			author_name.place(x=200,y=150)
			#author_name.pack()
			#author_name.grid(row=5,column=2)
	except:
		pass
		# no_author_name = Label(root,text='No Author data available')
		# no_author_name.place(x=20,y=150)
	
	try:	
		if len(response['items'][i]['volumeInfo']['description']) != 0:

			description = Label(root,text="Description: ",font=('Helvetica',15,"bold"),bg='green',fg='red')
			description.place(x=20,y=200)
			#description.pack()
			#description.grid(row=11,column=1)

			description_display = Message(root,text=response['items'][i]['volumeInfo']['description'],font=('Helvetica',15,"bold"),bg='green',fg='white',width=1300)
			description_display.place(x=200,y=200)
			#description_display.pack()
			#description_display.grid(row=11,column=2)

	except:
		pass
		# no_description = Label(root,text='No description available in archives')
		# no_description.place(x=200,y=200)
	
	try:
		if len(response['items'][i]['volumeInfo']['categories']) != 0:
			category = Label(root,text='Category:',font=('Helvetica',15,"bold"),bg='green',fg='red')
			category.place(x=20,y=420)
			#category.pack()
			#category.grid(row=17,column=1)
			category_diaplay = Label(root,text=response['items'][i]['volumeInfo']['categories'],font=('Helvetica',15,"bold"),bg='green',fg='white')
			category_diaplay.place(x=210,y=420)
			#category_diaplay.pack()
			#category_diaplay.grid(row=17,column=2)
	except:
		pass
	
	try:
		if response['items'][i]['volumeInfo']['averageRating'] != 0:
			ratings = Label(root,text="Average Rating: ",font=('Helvetica',15,"bold"),bg='green',fg='red')
			ratings.place(x=20,y=470)
			#ratings.pack()
			#ratings.pack(row=23,column=1)
			ratings_display = Label(root,text=str(response['items'][i]['volumeInfo']['averageRating']),font=('Helvetica',15,"bold"),bg='green',fg='white')
			ratings_display.place(x=210,y=470)
			#ratings_display.pack()
			#ratings_display.pack(row=23,column=2)
	except:
		pass

	try:
		if len(response['items'][i]['saleInfo']['buyLink']) != 0:
			buy_book_url = response['items'][i]['saleInfo']['buyLink']
			# pyperclip.copy(buy_book_url)
			# spam = pyperclip.paste()
			buy = Label(root,text='Buy the book:',font=('Helvetica',15,"bold"),bg='green',fg='red')
			buy.place(x=20,y=520)
			#buy.pack()
			#buy_book_url.grid(row=26,column=1)
			buy_link = Label(root,text=str(response['items'][i]['saleInfo']['buyLink']),font=('Helvetica',15,"bold"),bg='green',fg='white')
			buy_link.place(x=210,y=520)
			link_copied = Label(root,text="(This link has been copied to your clipboard)",font=('Helvetica',10,"bold"),bg='green',fg='white')
			link_copied.place(x=210,y=550)
			#buy_link.pack()
			#buy_link.grid(row=26,column=2)
	except:
		pass

	try:
		if len(response['items'][i]['volumeInfo']['imageLinks']['smallThumbnail']) != 0:
			pass
	except:
		pass

	goto_email_verifier = Button(root,text="Go to Search page",font=('Helvetica',15),command=email_verifier)
	goto_email_verifier.place(x=650,y=650)
	quit_program = Button(root,text="quit",font=('Helvetica',15),command=root.quit)
	quit_program.place(x=900,y=650)
	# scrollbar to description
	# add preview images(imageLinks)
	# goto button to search page


def book_data_return():
	api_key = 'AIzaSyAy9cKq459VMHTTWzKmItWEWBtGYotA9ZI'
	address = query_string.get()
	if address:
		params = {
		    'key': api_key,
		    'q': address
		}
		url = 'https://www.googleapis.com/books/v1/volumes?'
		global response
		response = requests.get(url, params=params).json()

	# response_dict = json_loads(response)
	# if 'items' not in response_dict:
	# 	for widgets in root.winfo_children():
	# 		widgets.destroy()
	if response.get('items') == None:
		for widgets in root.winfo_children():
			widgets.destroy()


		label1 = Label(root,text='Search Interrupted!!',font=('Helvetica',50,'bold'),bg='green',fg='red').place(x=480,y=10)
		label2 = Label(root,text='It might be due to the following reasons:',font=('Helvetica',30,'bold'),bg='green',fg='white').place(x=10,y=120)
		label3 = Label(root,text='1. ERROR 204: No Content',font=('Helvetica',15),bg='green',fg='white').place(x=22,y=190)
		label4 = Label(root,text='2. ERROR 408: Request Timeout',font=('Helvetica',15),bg='green',fg='white').place(x=22,y=220)
		label5 = Label(root,text='3. ERROR 413: Payload too large(Request Entity Too Large)',font=('Helvetica',15),bg='green',fg='white').place(x=22,y=250)
		label6 = Label(root,text='4. ERROR 408: Request Timeout',font=('Helvetica',15),bg='green',fg='white').place(x=22,y=280)
		label7 = Label(root,text='5. ERROR 429: Too many requests',font=('Helvetica',15),bg='green',fg='white').place(x=22,y=310)
		label8 = Label(root,text='6. ERROR 500: Internal server error',font=('Helvetica',15),bg='green',fg='white').place(x=22,y=340)
		label9 = Label(root,text='7. ERROR 503: Service Unavailable',font=('Helvetica',15),bg='green',fg='white').place(x=22,y=370)

		exit_button = Button(root,text='Logout & Exit',font=('Helvetica',15),command=root.quit).place(x=650,y=450)
		def restart_program():
		    """Restarts the current program.	
			Note: this function does not return. Any cleanup action (like
			saving data) must be done before calling this function.

			Or if You want no console behind then Simply Change the extension 
			of the file to .pyw
			And Run this Code:-
			Restarts the Whole Window    
			def restart():
				root.destroy()
				os.startfile("main.pyw")
			"""
		    python = sys.executable
		    os.execl(python, python, * sys.argv)
		goto_starting_button = Button(root,text='Restart',font=('Helvetica',15),command=restart_program).place(x=850,y=450)

	# 	my_image = ImageTk.PhotoImage(Image.open("p03gg1lc.jpg"))
	# 	image_lable = Label(frame1,image = my_image)
	# 	image_lable.place(x=0,y=0)

		# add a suitable image


	global all_book_titles
	for i in range(0,len(response['items'])):
		all_book_titles = [response['items'][i]['volumeInfo']['title'] for i in range(0,len(response['items']))]
		# used labda function above
	global books_menu
	books_menu = ttk.Combobox(root,value=all_book_titles,font=('Helvetica',15),width=50,state='readonly')
	# state: One of “normal”, “readonly”, or “disabled”. In the “readonly” state, the value may not be edited 
	# directly, and the user can only selection of the values from the dropdown list. In the “normal” state, 
	# the text field is directly editable. In the “disabled” state, no interaction is possible.
	books_menu.current(1)
	books_menu.place(x=631,y=450)

	# global choosen_book
	# choosen_book = books_menu.get()

	submit_book = Button(root,text='Submit',font=('Helvetica',15),width=20,command=print_book_data)
	root.bind('<Return>', lambda event=None: submit_book.invoke())
	submit_book.place(x=631,y=500)


def email_verifier():
	response = quickemailverification.verify(email_entries.get())

	if response.body['result'] == 'invalid':
		messagebox.showerror('Invalid E-mail entered', 'Enter correct email to proceed')

	else:
		for widgets in root.winfo_children():
			widgets.destroy()	# special code to clear whole screen in tkinter !! REMEMBER THIS !!

		# logo_img = ImageTk.PhotoImage(Image.open("p03gg1lc.jpg"))
		# image_lable1 = Label(root,image = logo_img)
		# image_lable1.place(x=0,y=0)

		Logged_In = Label(root,text='Sucesfully Logged-In',bg='green',font=('Helvetica',40,'bold'),fg='white')
		Logged_In.place(x=480,y=200)

		book_query = Label(root,text='Enter book name:',bg='green',fg='white',font=('Helvetica',20))
		book_query.place(x=400,y=300)

		global query_string
		query_string = Entry(root,font=('Helvetica',18),width=35)
		query_string.place(x=630,y=305)

		query_submit = Button(root,text='Submit',width=20,font=('Helvetica',13),command=book_data_return)
		root.bind('<Return>', lambda event=None: query_submit.invoke())
		query_submit.place(x=631,y=360)

		# add google ads, google authentication, facebook api


frame1 =Frame(root,background='white',height=553,width=980)
frame1.pack(pady=30)

my_image = ImageTk.PhotoImage(Image.open("p03gg1lc.jpg"))
image_lable = Label(frame1,image = my_image)
image_lable.place(x=0,y=0)


ask_for_name = Label(root,text='Enter your name to proceed:',bg='green',font=('Helvetica',20,'bold'))
ask_for_name.place(x=400,y=600)

name_entey = Entry(root,font=('Helvetica',15),width=20)
name_entey.place(x=815,y=605)

submit_button = Button(root,text='Submit',font=('Helvetica'),width=20,command=print_name)
#submit_button.bind('<Return>', print_name)
root.bind('<Return>', lambda event=None: submit_button.invoke())
submit_button.place(x=835,y=660)



root.mainloop()


"""
{
  "kind": "books#volumes",
  "totalItems": 2253,
  "items": [
    {
      "kind": "books#volume",
      "id": "B7FL6zzN_FsC",
      "etag": "pkamSJ2XZ3c",
      "selfLink": "https://www.googleapis.com/books/v1/volumes/B7FL6zzN_FsC",
      "volumeInfo": {
        "title": "Good Omens",
        "authors": [
          "Neil Gaiman",
          "Terry Pratchett"
        ],
        "publisher": "Random House",
        "publishedDate": "2011-11-22",
        "description": "THE BOOK BEHIND THE AMAZON PRIME/BBC SERIES STARRING DAVID TENNANT, MICHAEL SHEEN, JON HAMM AND BENEDICT CUMBERBATCH 'Ridiculously inventive and gloriously funny' Guardian What if, for once, the predictions are right, and the Apocalypse really is due to arrive next Saturday, just after tea? It's a predicament that Aziraphale, a somewhat fussy angel, and Crowley, a fast-living demon, now find themselves in. They've been living amongst Earth's mortals since The Beginning and, truth be told, have grown rather fond of the lifestyle and, in all honesty, are not actually looking forward to the coming Apocalypse. And then there's the small matter that someone appears to have misplaced the Antichrist . . . _____________________ What readers are saying about Good Omens: ***** 'A superb recipe for disaster. I didn't stop grinning from beginning to end.' ***** 'Both Gaiman and Pratchett are great authors and they complement each other brilliantly' ***** 'Superbly enjoyable read. Seamlessly co-written.'",
        "industryIdentifiers": [
          {
            "type": "ISBN_13",
            "identifier": "9781448110230"
          },
          {
            "type": "ISBN_10",
            "identifier": "1448110238"
          }
        ],
        "readingModes": {
          "text": true,
          "image": false
        },
        "pageCount": 416,
        "printType": "BOOK",
        "categories": [
          "Fiction"
        ],
        "averageRating": 4,
        "ratingsCount": 3389,
        "maturityRating": "NOT_MATURE",
        "allowAnonLogging": true,
        "contentVersion": "0.32.27.0.preview.2",
        "panelizationSummary": {
          "containsEpubBubbles": false,
          "containsImageBubbles": false
        },
        "imageLinks": {
          "smallThumbnail": "http://books.google.com/books/content?id=B7FL6zzN_FsC&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
          "thumbnail": "http://books.google.com/books/content?id=B7FL6zzN_FsC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
        },
        "language": "en",
        "previewLink": "http://books.google.co.in/books?id=B7FL6zzN_FsC&printsec=frontcover&dq=good+omens&hl=&cd=1&source=gbs_api",
        "infoLink": "https://play.google.com/store/books/details?id=B7FL6zzN_FsC&source=gbs_api",
        "canonicalVolumeLink": "https://play.google.com/store/books/details?id=B7FL6zzN_FsC"
      },
      "saleInfo": {
        "country": "IN",
        "saleability": "FOR_SALE",
        "isEbook": true,
        "listPrice": {
          "amount": 400.2,
          "currencyCode": "INR"
        },
        "retailPrice": {
          "amount": 280.14,
          "currencyCode": "INR"
        },
        "buyLink": "https://play.google.com/store/books/details?id=B7FL6zzN_FsC&rdid=book-B7FL6zzN_FsC&rdot=1&source=gbs_api",
        "offers": [
          {
            "finskyOfferType": 1,
            "listPrice": {
              "amountInMicros": 400200000,
              "currencyCode": "INR"
            },
            "retailPrice": {
              "amountInMicros": 280140000,
              "currencyCode": "INR"
            }
          }
        ]
      },
      "accessInfo": {
        "country": "IN",
        "viewability": "PARTIAL",
        "embeddable": true,
        "publicDomain": false,
        "textToSpeechPermission": "ALLOWED_FOR_ACCESSIBILITY",
        "epub": {
          "isAvailable": true,
          "acsTokenLink": "http://books.google.co.in/books/download/Good_Omens-sample-epub.acsm?id=B7FL6zzN_FsC&format=epub&output=acs4_fulfillment_token&dl_type=sample&source=gbs_api"
        },
        "pdf": {
          "isAvailable": false
        },
        "webReaderLink": "http://play.google.com/books/reader?id=B7FL6zzN_FsC&hl=&printsec=frontcover&source=gbs_api",
        "accessViewStatus": "SAMPLE",
        "quoteSharingAllowed": false
      },
      "searchInfo": {
        "textSnippet": "THE BOOK BEHIND THE AMAZON PRIME/BBC SERIES STARRING DAVID TENNANT, MICHAEL SHEEN, JON HAMM AND BENEDICT CUMBERBATCH 'Ridiculously inventive and gloriously funny' Guardian What if, for once, the predictions are right, and the Apocalypse ..."
      }
    },
    {
      "kind": "books#volume",
      "id": "-o-2KpQlFNsC",
      "etag": "vgeANHKKGxA",
      "selfLink": "https://www.googleapis.com/books/v1/volumes/-o-2KpQlFNsC",
      "volumeInfo": {
        "title": "Good Omens",
        "subtitle": "The Nice and Accurate Prophecies of Agnes Nutter, Witch",
        "authors": [
          "Neil Gaiman",
          "Terry Pratchett"
        ],
        "publisher": "Harper Collins",
        "publishedDate": "2011-06-28",
        "description": "The classic collaboration from the internationally bestselling authors Neil Gaiman and Terry Pratchett, soon to be an original series starring Michael Sheen and David Tennant. “Good Omens . . . is something like what would have happened if Thomas Pynchon, Tom Robbins and Don DeLillo had collaborated. Lots of literary inventiveness in the plotting and chunks of very good writing and characterization. It’s a wow. It would make one hell of a movie. Or a heavenly one. Take your pick.”—Washington Post According to The Nice and Accurate Prophecies of Agnes Nutter, Witch (the world's only completely accurate book of prophecies, written in 1655, before she exploded), the world will end on a Saturday. Next Saturday, in fact. Just before dinner. So the armies of Good and Evil are amassing, Atlantis is rising, frogs are falling, tempers are flaring. Everything appears to be going according to Divine Plan. Except a somewhat fussy angel and a fast-living demon—both of whom have lived amongst Earth's mortals since The Beginning and have grown rather fond of the lifestyle—are not actually looking forward to the coming Rapture. And someone seems to have misplaced the Antichrist . . .",
        "industryIdentifiers": [
          {
            "type": "ISBN_13",
            "identifier": "9780061991127"
          },
          {
            "type": "ISBN_10",
            "identifier": "0061991120"
          }
        ],
        "readingModes": {
          "text": true,
          "image": false
        },
        "pageCount": 432,
        "printType": "BOOK",
        "categories": [
          "Fiction"
        ],
        "averageRating": 4,
        "ratingsCount": 3381,
        "maturityRating": "NOT_MATURE",
        "allowAnonLogging": true,
        "contentVersion": "0.12.9.0.preview.2",
        "panelizationSummary": {
          "containsEpubBubbles": false,
          "containsImageBubbles": false
        },
        "imageLinks": {
          "smallThumbnail": "http://books.google.com/books/content?id=-o-2KpQlFNsC&printsec=frontcover&img=1&zoom=5&source=gbs_api",
          "thumbnail": "http://books.google.com/books/content?id=-o-2KpQlFNsC&printsec=frontcover&img=1&zoom=1&source=gbs_api"
        },
        "language": "en",
        "previewLink": "http://books.google.co.in/books?id=-o-2KpQlFNsC&dq=good+omens&hl=&cd=2&source=gbs_api",
        "infoLink": "http://books.google.co.in/books?id=-o-2KpQlFNsC&dq=good+omens&hl=&source=gbs_api",
        "canonicalVolumeLink": "https://books.google.com/books/about/Good_Omens.html?hl=&id=-o-2KpQlFNsC"
      },
      "saleInfo": {
        "country": "IN",
        "saleability": "NOT_FOR_SALE",
        "isEbook": false
      },
      "accessInfo": {
        "country": "IN",
        "viewability": "NO_PAGES",
        "embeddable": false,
        "publicDomain": false,
        "textToSpeechPermission": "ALLOWED",
        "epub": {
          "isAvailable": true
        },
        "pdf": {
          "isAvailable": true
        },
        "webReaderLink": "http://play.google.com/books/reader?id=-o-2KpQlFNsC&hl=&printsec=frontcover&source=gbs_api",
        "accessViewStatus": "NONE",
        "quoteSharingAllowed": false
      },
      "searchInfo": {
        "textSnippet": "The classic collaboration from the internationally bestselling authors Neil Gaiman and Terry Pratchett, soon to be an original series starring Michael Sheen and David Tennant. “Good Omens . . . is something like what would have happened ..."
      }
    },
    {
      "kind": "books#volume",
      "id": "FsN0mxNThYIC",
      "etag": "f6xA0sekDDo",
      "selfLink": "https://www.googleapis.com/books/v1/volumes/FsN0mxNThYIC",
      "volumeInfo": {
        "title": "Good Omens",
        "subtitle": "The Nice and Accurate Prophecies of Agnes Nutter, Witch",
        "authors": [
          "Neil Gaiman",
          "Terry Pratchett"
        ],
        "publisher": "Harper Collins",
        "publishedDate": "2006-02-28",
        "description": "There is a distinct hint of Armageddon in the air. According to The Nice and Accurate Prophecies of Agnes Nutter, Witch (recorded, thankfully, in 1655, before she blew up her entire village and all its inhabitants, who had gathered to watch her burn), the world will end on a Saturday. Next Saturday, in fact. So the armies of Good and Evil are amassing, the Four Bikers of the Apocalypse are revving up their mighty hogs and hitting the road, and the world's last two remaining witch-finders are getting ready to fight the good fight, armed with awkwardly antiquated instructions and stick pins. Atlantis is rising, frogs are falling, tempers are flaring. . . . Right. Everything appears to be going according to Divine Plan. Except that a somewhat fussy angel and a fast-living demon -- each of whom has lived among Earth's mortals for many millennia and has grown rather fond of the lifestyle -- are not particularly looking forward to the coming Rapture. If Crowley and Aziraphale are going to stop it from happening, they've got to find and kill the Antichrist (which is a shame, as he's a really nice kid). There's just one glitch: someone seems to have misplaced him. . . . First published in 1990, Neil Gaiman and Terry Pratchett's brilliantly dark and screamingly funny take on humankind's final judgment is back -- and just in time -- in a new hardcover edition (which includes an introduction by the authors, comments by each about the other, and answers to some still-burning questions about their wildly popular collaborative effort) that the devout and the damned alike will surely cherish until the end of all things.",
        "industryIdentifiers": [
          {
            "type": "ISBN_13",
            "identifier": "9780060853969"
          },
          {
            "type": "ISBN_10",
            "identifier": "0060853964"
          }
        ],
        "readingModes": {
          "text": false,
          "image": false
        },
        "pageCount": 400,
        "printType": "BOOK",
        "categories": [
          "Fiction"
        ],
        "averageRating": 4,
        "ratingsCount": 3383,
        "maturityRating": "NOT_MATURE",
        "allowAnonLogging": false,
        "contentVersion": "preview-1.0.0",
        "panelizationSummary": {
          "containsEpubBubbles": false,
          "containsImageBubbles": false
        },
        "imageLinks": {
          "smallThumbnail": "http://books.google.com/books/content?id=FsN0mxNThYIC&printsec=frontcover&img=1&zoom=5&source=gbs_api",
          "thumbnail": "http://books.google.com/books/content?id=FsN0mxNThYIC&printsec=frontcover&img=1&zoom=1&source=gbs_api"
        },
        "language": "en",
        "previewLink": "http://books.google.co.in/books?id=FsN0mxNThYIC&pg=PP1&dq=good+omens&hl=&cd=3&source=gbs_api",
        "infoLink": "http://books.google.co.in/books?id=FsN0mxNThYIC&dq=good+omens&hl=&source=gbs_api",
        "canonicalVolumeLink": "https://books.google.com/books/about/Good_Omens.html?hl=&id=FsN0mxNThYIC"
      },
      "saleInfo": {
        "country": "IN",
        "saleability": "NOT_FOR_SALE",
        "isEbook": false
      },
      "accessInfo": {
        "country": "IN",
        "viewability": "NO_PAGES",
        "embeddable": false,
        "publicDomain": false,
        "textToSpeechPermission": "ALLOWED",
        "epub": {
          "isAvailable": false
        },
        "pdf": {
          "isAvailable": false
        },
        "webReaderLink": "http://play.google.com/books/reader?id=FsN0mxNThYIC&hl=&printsec=frontcover&source=gbs_api",
        "accessViewStatus": "NONE",
        "quoteSharingAllowed": false
      }
    },
    {
      "kind": "books#volume",
      "id": "_LjorQEACAAJ",
      "etag": "mA55KlcecO8",
      "selfLink": "https://www.googleapis.com/books/v1/volumes/_LjorQEACAAJ",
      "volumeInfo": {
        "title": "Good Omens",
        "authors": [
          "Neil Gaiman",
          "Terry Pratchett"
        ],
        "publisher": "Corgi",
        "publishedDate": "2014-12-11",
        "description": "____________________ NOW ON AMAZON PRIME - STARRING DAVID TENNANT, MICHAEL SHEEN, JON HAMM AND BENEDICT CUMBERBATCH 'Ridiculously inventive and gloriously funny' Guardian ____________________ What if, for once, the predictions are right, and the Apocalypse really is due to arrive next Saturday, just after tea? It's a predicament that Aziraphale, a somewhat fussy angel, and Crowley, a fast-living demon, now find themselves in. They've been living amongst Earth's mortals since The Beginning and, truth be told, have grown rather fond of the lifestyle and, in all honesty, are not actually looking forward to the coming Apocalypse. Now people have been predicting the end of the world almost from its very beginning, so it's only natural to be sceptical when a new date is set for Judgement Day. You could spend the time left drowning your sorrows, giving away all your possessions in preparation for the rapture, or laughing it off as (hopefully) just another hoax. Or you could just try to do something about it. And then there's the small matter that someone appears to have misplaced the Antichrist . . . _____________________ CAST INCLUDES: Crowley - David Tennant Aziraphale - Michael Sheen Angel Gabriel - Jon Hamm Voice of Satan - Benedict Cumberbatch Voice of God - Frances McDormand",
        "industryIdentifiers": [
          {
            "type": "ISBN_10",
            "identifier": "0552171891"
          },
          {
            "type": "ISBN_13",
            "identifier": "9780552171892"
          }
        ],
        "readingModes": {
          "text": false,
          "image": false
        },
        "pageCount": 416,
        "printType": "BOOK",
        "categories": [
          "End of the world"
        ],
        "maturityRating": "NOT_MATURE",
        "allowAnonLogging": false,
        "contentVersion": "preview-1.0.0",
        "panelizationSummary": {
          "containsEpubBubbles": false,
          "containsImageBubbles": false
        },
        "imageLinks": {
          "smallThumbnail": "http://books.google.com/books/content?id=_LjorQEACAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api",
          "thumbnail": "http://books.google.com/books/content?id=_LjorQEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
        },
        "language": "un",
        "previewLink": "http://books.google.co.in/books?id=_LjorQEACAAJ&dq=good+omens&hl=&cd=4&source=gbs_api",
        "infoLink": "http://books.google.co.in/books?id=_LjorQEACAAJ&dq=good+omens&hl=&source=gbs_api",
        "canonicalVolumeLink": "https://books.google.com/books/about/Good_Omens.html?hl=&id=_LjorQEACAAJ"
      },
      "saleInfo": {
        "country": "IN",
        "saleability": "NOT_FOR_SALE",
        "isEbook": false
      },
      "accessInfo": {
        "country": "IN",
        "viewability": "NO_PAGES",
        "embeddable": false,
        "publicDomain": false,
        "textToSpeechPermission": "ALLOWED",
        "epub": {
          "isAvailable": false
        },
        "pdf": {
          "isAvailable": false
        },
        "webReaderLink": "http://play.google.com/books/reader?id=_LjorQEACAAJ&hl=&printsec=frontcover&source=gbs_api",
        "accessViewStatus": "NONE",
        "quoteSharingAllowed": false
      },
      "searchInfo": {
        "textSnippet": "Above all (or, in Aziraphale's case, below all) they need to find and kill the Antichrist, currently the most powerful creature on Earth. This is a shame."
      }
    },
    {
      "kind": "books#volume",
      "id": "UZNxDwAAQBAJ",
      "etag": "tjV/7IBOuis",
      "selfLink": "https://www.googleapis.com/books/v1/volumes/UZNxDwAAQBAJ",
      "volumeInfo": {
        "title": "The Quite Nice and Fairly Accurate Good Omens Script Book",
        "authors": [
          "Neil Gaiman"
        ],
        "publisher": "Hachette UK",
        "publishedDate": "2019-05-21",
        "description": "The Quite Nice and Fairly Accurate Good Omens Script Book contains much that is new and revelatory and even several scenes that are not actually in the final television series. 'One of the most hotly anticipated TV shows of the year' Independent 'Even if you're very familiar with the original novel, this is a different experience... so damned charming and quirky that it feels like a must' Starburst Neil Gaiman's glorious reinvention of the iconic bestseller Good Omens is adapted from the internationally beloved novel by Terry Pratchett and Neil Gaiman and is soon to be a massive new TV launch on Amazon Prime Video and the BBC. The series is written and show-run by Neil himself and stars David Tennant, Michael Sheen, Jon Hamm and Miranda Richardson, to name but a few. **Includes an introduction by Neil Gaiman about bringing Good Omens to the screen** Before he died in 2015, Terry Pratchett asked Neil Gaiman to make a television series of the internationally beloved novel they wrote together about the end of the world. And so, Neil began to write. And continued to write until he had six episodes that brought an angel, Aziraphale, and a demon, Crowley, (the only things standing between us and the inevitable Armageddon) to life for the screen. Contained between the covers of this book are the scripts that Neil wrote, which later turned into some of the most extraordinary television ever made. Take a tour behind the scenes with a text that reveals the secrets of the show, still has the missing bits and, sometimes, asks for the impossible. Step backstage and see the magic for yourself. You may just learn as much from the scenes that never made the final cut as from those that did.",
        "industryIdentifiers": [
          {
            "type": "ISBN_13",
            "identifier": "9781472261243"
          },
          {
            "type": "ISBN_10",
            "identifier": "1472261240"
          }
        ],
        "readingModes": {
          "text": true,
          "image": false
        },
        "pageCount": 400,
        "printType": "BOOK",
        "categories": [
          "Performing Arts"
        ],
        "averageRating": 5,
        "ratingsCount": 2,
        "maturityRating": "NOT_MATURE",
        "allowAnonLogging": true,
        "contentVersion": "1.3.3.0.preview.2",
        "panelizationSummary": {
          "containsEpubBubbles": false,
          "containsImageBubbles": false
        },
        "imageLinks": {
          "smallThumbnail": "http://books.google.com/books/content?id=UZNxDwAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
          "thumbnail": "http://books.google.com/books/content?id=UZNxDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
        },
        "language": "en",
        "previewLink": "http://books.google.co.in/books?id=UZNxDwAAQBAJ&printsec=frontcover&dq=good+omens&hl=&cd=5&source=gbs_api",
        "infoLink": "https://play.google.com/store/books/details?id=UZNxDwAAQBAJ&source=gbs_api",
        "canonicalVolumeLink": "https://play.google.com/store/books/details?id=UZNxDwAAQBAJ"
      },
      "saleInfo": {
        "country": "IN",
        "saleability": "FOR_SALE",
        "isEbook": true,
        "listPrice": {
          "amount": 1209.5,
          "currencyCode": "INR"
        },
        "retailPrice": {
          "amount": 604.75,
          "currencyCode": "INR"
        },
        "buyLink": "https://play.google.com/store/books/details?id=UZNxDwAAQBAJ&rdid=book-UZNxDwAAQBAJ&rdot=1&source=gbs_api",
        "offers": [
          {
            "finskyOfferType": 1,
            "listPrice": {
              "amountInMicros": 1209500000,
              "currencyCode": "INR"
            },
            "retailPrice": {
              "amountInMicros": 604750000,
              "currencyCode": "INR"
            }
          }
        ]
      },
      "accessInfo": {
        "country": "IN",
        "viewability": "PARTIAL",
        "embeddable": true,
        "publicDomain": false,
        "textToSpeechPermission": "ALLOWED_FOR_ACCESSIBILITY",
        "epub": {
          "isAvailable": true,
          "acsTokenLink": "http://books.google.co.in/books/download/The_Quite_Nice_and_Fairly_Accurate_Good-sample-epub.acsm?id=UZNxDwAAQBAJ&format=epub&output=acs4_fulfillment_token&dl_type=sample&source=gbs_api"
        },
        "pdf": {
          "isAvailable": false
        },
        "webReaderLink": "http://play.google.com/books/reader?id=UZNxDwAAQBAJ&hl=&printsec=frontcover&source=gbs_api",
        "accessViewStatus": "SAMPLE",
        "quoteSharingAllowed": false
      },
      "searchInfo": {
        "textSnippet": "'One of the most hotly anticipated TV shows of the year' Independent 'Even if you're very familiar with the original novel, this is a different experience... so damned charming and quirky that it feels like a must' Starburst Neil Gaiman's ..."
      }
    },
    {
      "kind": "books#volume",
      "id": "9ataAAAAMAAJ",
      "etag": "R/hnXc2hFwo",
      "selfLink": "https://www.googleapis.com/books/v1/volumes/9ataAAAAMAAJ",
      "volumeInfo": {
        "title": "Good Omens",
        "subtitle": "The Nice and Accurate Prophecies of Agnes Nutter, Witch : a Novel",
        "authors": [
          "Neil Gaiman",
          "Terry Pratchett"
        ],
        "publisher": "Workman Publishing Company",
        "publishedDate": "1990",
        "description": "When the armies of Heaven and Hell decide it's time for Armageddon, a demon and an angel decide they like life on earth and team up to stop the coming Apocalypse",
        "industryIdentifiers": [
          {
            "type": "OTHER",
            "identifier": "UOM:39015058712145"
          }
        ],
        "readingModes": {
          "text": false,
          "image": false
        },
        "pageCount": 354,
        "printType": "BOOK",
        "categories": [
          "Angels"
        ],
        "averageRating": 4,
        "ratingsCount": 3463,
        "maturityRating": "NOT_MATURE",
        "allowAnonLogging": false,
        "contentVersion": "0.0.2.0.preview.0",
        "panelizationSummary": {
          "containsEpubBubbles": false,
          "containsImageBubbles": false
        },
        "imageLinks": {
          "smallThumbnail": "http://books.google.com/books/content?id=9ataAAAAMAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api",
          "thumbnail": "http://books.google.com/books/content?id=9ataAAAAMAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
        },
        "language": "un",
        "previewLink": "http://books.google.co.in/books?id=9ataAAAAMAAJ&q=good+omens&dq=good+omens&hl=&cd=6&source=gbs_api",
        "infoLink": "http://books.google.co.in/books?id=9ataAAAAMAAJ&dq=good+omens&hl=&source=gbs_api",
        "canonicalVolumeLink": "https://books.google.com/books/about/Good_Omens.html?hl=&id=9ataAAAAMAAJ"
      },
      "saleInfo": {
        "country": "IN",
        "saleability": "NOT_FOR_SALE",
        "isEbook": false
      },
      "accessInfo": {
        "country": "IN",
        "viewability": "NO_PAGES",
        "embeddable": false,
        "publicDomain": false,
        "textToSpeechPermission": "ALLOWED",
        "epub": {
          "isAvailable": false
        },
        "pdf": {
          "isAvailable": false
        },
        "webReaderLink": "http://play.google.com/books/reader?id=9ataAAAAMAAJ&hl=&printsec=frontcover&source=gbs_api",
        "accessViewStatus": "NONE",
        "quoteSharingAllowed": false
      },
      "searchInfo": {
        "textSnippet": "When the armies of Heaven and Hell decide it's time for Armageddon, a demon and an angel decide they like life on earth and team up to stop the coming Apocalypse"
      }
    },
    {
      "kind": "books#volume",
      "id": "I5h1DwAAQBAJ",
      "etag": "s1FVEajt9zA",
      "selfLink": "https://www.googleapis.com/books/v1/volumes/I5h1DwAAQBAJ",
      "volumeInfo": {
        "title": "The Nice and Accurate Good Omens TV Companion",
        "authors": [
          "Matt Whyman"
        ],
        "publisher": "Hachette UK",
        "publishedDate": "2019-05-21",
        "description": "The ultimate TV companion book to Good Omens, a massive new television launch on Amazon Prime Video and the BBC, written and show-run by Neil Gaiman and adapted from the internationally beloved novel by Terry Pratchett and Neil Gaiman. '[It was] absurdly good fun...Terry charged Neil with getting it made, almost as his deathbed wish, so it's a real labour of love' - David Tennant In the beginning there was a book written by Terry Pratchett and Neil Gaiman about the forces of good and evil coming together to prevent the apocalypse, scheduled to happen on a Saturday just after tea. Now, that internationally beloved novel has been transformed into six hour-long episodes of some of the most creative and ambitious television ever made. Written and show-run by Neil Gaiman and directed by Douglas Mackinnon, this BBC Studios creation brings Good Omens spectacularly to life, through a cast that includes David Tennant, Michael Sheen, Jon Hamm, Miranda Richardson, Josie Lawrence, Derek Jacobi, Nick Offerman, Jack Whitehall and Adria Arjona. Keep calm, because The Nice and Accurate Good Omens TV Companion is your ultimate guide to navigating Armageddon. Through character profiles and in-depth interviews with the stars and the crew, stunning behind-the-scenes and stills photography of the cast and locations, and a fascinating insight into costume boards and set designs, you will discover the feats of creativity and mind-boggling techniques that have gone into bringing an angel, a demon, and the Antichrist to the screens of people everywhere. This book will take you inside the world of Heaven and Hell (and Tadfield) and is set to shatter coffee tables around the world.",
        "industryIdentifiers": [
          {
            "type": "ISBN_13",
            "identifier": "9781472263643"
          },
          {
            "type": "ISBN_10",
            "identifier": "1472263642"
          }
        ],
        "readingModes": {
          "text": true,
          "image": false
        },
        "pageCount": 320,
        "printType": "BOOK",
        "categories": [
          "Performing Arts"
        ],
        "averageRating": 5,
        "ratingsCount": 1,
        "maturityRating": "NOT_MATURE",
        "allowAnonLogging": true,
        "contentVersion": "1.2.2.0.preview.2",
        "panelizationSummary": {
          "containsEpubBubbles": false,
          "containsImageBubbles": false
        },
        "imageLinks": {
          "smallThumbnail": "http://books.google.com/books/content?id=I5h1DwAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
          "thumbnail": "http://books.google.com/books/content?id=I5h1DwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
        },
        "language": "en",
        "previewLink": "http://books.google.co.in/books?id=I5h1DwAAQBAJ&printsec=frontcover&dq=good+omens&hl=&cd=7&source=gbs_api",
        "infoLink": "https://play.google.com/store/books/details?id=I5h1DwAAQBAJ&source=gbs_api",
        "canonicalVolumeLink": "https://play.google.com/store/books/details?id=I5h1DwAAQBAJ"
      },
      "saleInfo": {
        "country": "IN",
        "saleability": "FOR_SALE",
        "isEbook": true,
        "listPrice": {
          "amount": 1392.4,
          "currencyCode": "INR"
        },
        "retailPrice": {
          "amount": 696.2,
          "currencyCode": "INR"
        },
        "buyLink": "https://play.google.com/store/books/details?id=I5h1DwAAQBAJ&rdid=book-I5h1DwAAQBAJ&rdot=1&source=gbs_api",
        "offers": [
          {
            "finskyOfferType": 1,
            "listPrice": {
              "amountInMicros": 1392400000,
              "currencyCode": "INR"
            },
            "retailPrice": {
              "amountInMicros": 696200000,
              "currencyCode": "INR"
            }
          }
        ]
      },
      "accessInfo": {
        "country": "IN",
        "viewability": "PARTIAL",
        "embeddable": true,
        "publicDomain": false,
        "textToSpeechPermission": "ALLOWED_FOR_ACCESSIBILITY",
        "epub": {
          "isAvailable": true,
          "acsTokenLink": "http://books.google.co.in/books/download/The_Nice_and_Accurate_Good_Omens_TV_Comp-sample-epub.acsm?id=I5h1DwAAQBAJ&format=epub&output=acs4_fulfillment_token&dl_type=sample&source=gbs_api"
        },
        "pdf": {
          "isAvailable": false
        },
        "webReaderLink": "http://play.google.com/books/reader?id=I5h1DwAAQBAJ&hl=&printsec=frontcover&source=gbs_api",
        "accessViewStatus": "SAMPLE",
        "quoteSharingAllowed": false
      },
      "searchInfo": {
        "textSnippet": "This book will take you inside the world of Heaven and Hell (and Tadfield) and is set to shatter coffee tables around the world."
      }
    },
    {
      "kind": "books#volume",
      "id": "4C25wAEACAAJ",
      "etag": "LLWVeqvks/M",
      "selfLink": "https://www.googleapis.com/books/v1/volumes/4C25wAEACAAJ",
      "volumeInfo": {
        "title": "The Illustrated Good Omens",
        "authors": [
          "Terry Pratchett",
          "Neil Gaiman"
        ],
        "publisher": "Gollancz",
        "publishedDate": "2019-04-04",
        "description": "There is a hint of Armageddon in the air. According to the Nice and Accurate Prophecies of Agnes Nutter, Witch (recorded, thankfully, in 1655, before she blew up her entire village and all its inhabitants, who had gathered to watch her burn), the world will end on a Saturday. Next Saturday, in fact. So the Armies of Good and Evil are massing, the four Bikers of the Apocalypse are revving up their mighty hogs and hitting the road, and the world's last two remaining witchfinders are getting ready to Fight the Good Fight. Atlantis is rising. Frogs are falling. Tempers are flaring, and everything appears to be going to Divine Plan. Except that a somewhat fussy angel and a fast-living demon are not particularly looking forward to the coming Rapture. They've lived amongst Humanity for millennia, and have grown rather fond of the lifestyle. So if Crowley and Aziraphale are going to stop it from happening, they've got to find and kill the AntiChrist (which is a shame, really, as he's a nice kid). There's just one glitch: someone seems to have misplaced him. This edition features a new revised text, approved by Neil Gaiman and the Pratchett Estate, which clears up many typos and errors from previous editions. It also features twelve full colour illustrations from Paul Kidby - Terry Pratchett's artist of choice - and further pencil drawings.",
        "industryIdentifiers": [
          {
            "type": "ISBN_10",
            "identifier": "1473227836"
          },
          {
            "type": "ISBN_13",
            "identifier": "9781473227835"
          }
        ],
        "readingModes": {
          "text": false,
          "image": false
        },
        "pageCount": 400,
        "printType": "BOOK",
        "categories": [
          "Humorous stories"
        ],
        "maturityRating": "NOT_MATURE",
        "allowAnonLogging": false,
        "contentVersion": "preview-1.0.0",
        "panelizationSummary": {
          "containsEpubBubbles": false,
          "containsImageBubbles": false
        },
        "imageLinks": {
          "smallThumbnail": "http://books.google.com/books/content?id=4C25wAEACAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api",
          "thumbnail": "http://books.google.com/books/content?id=4C25wAEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
        },
        "language": "un",
        "previewLink": "http://books.google.co.in/books?id=4C25wAEACAAJ&dq=good+omens&hl=&cd=8&source=gbs_api",
        "infoLink": "http://books.google.co.in/books?id=4C25wAEACAAJ&dq=good+omens&hl=&source=gbs_api",
        "canonicalVolumeLink": "https://books.google.com/books/about/The_Illustrated_Good_Omens.html?hl=&id=4C25wAEACAAJ"
      },
      "saleInfo": {
        "country": "IN",
        "saleability": "NOT_FOR_SALE",
        "isEbook": false
      },
      "accessInfo": {
        "country": "IN",
        "viewability": "NO_PAGES",
        "embeddable": false,
        "publicDomain": false,
        "textToSpeechPermission": "ALLOWED",
        "epub": {
          "isAvailable": false
        },
        "pdf": {
          "isAvailable": false
        },
        "webReaderLink": "http://play.google.com/books/reader?id=4C25wAEACAAJ&hl=&printsec=frontcover&source=gbs_api",
        "accessViewStatus": "NONE",
        "quoteSharingAllowed": false
      },
      "searchInfo": {
        "textSnippet": "There's just one glitch: someone seems to have misplaced him. This edition features a new revised text, approved by Neil Gaiman and the Pratchett Estate, which clears up many typos and errors from previous editions."
      }
    },
    {
      "kind": "books#volume",
      "id": "it5B-Y2EQhoC",
      "etag": "jgjHYLuK0p0",
      "selfLink": "https://www.googleapis.com/books/v1/volumes/it5B-Y2EQhoC",
      "volumeInfo": {
        "title": "Coraline 10th Anniversary Edition",
        "authors": [
          "Neil Gaiman"
        ],
        "publisher": "Harper Collins",
        "publishedDate": "2012-04-24",
        "description": "\"Coraline discovered the door a little while after they moved into the house. . . .\" When Coraline steps through a door to find another house strangely similar to her own (only better), things seem marvelous. But there's another mother there, and another father, and they want her to stay and be their little girl. They want to change her and never let her go. Coraline will have to fight with all her wit and courage if she is to save herself and return to her ordinary life. Celebrating ten years of Neil Gaiman's first modern classic for young readers, this edition is enriched with a brand-new foreword from the author, a reader's guide, and more.",
        "industryIdentifiers": [
          {
            "type": "ISBN_13",
            "identifier": "9780062205728"
          },
          {
            "type": "ISBN_10",
            "identifier": "0062205722"
          }
        ],
        "readingModes": {
          "text": true,
          "image": false
        },
        "pageCount": 208,
        "printType": "BOOK",
        "categories": [
          "Juvenile Fiction"
        ],
        "averageRating": 4,
        "ratingsCount": 27,
        "maturityRating": "NOT_MATURE",
        "allowAnonLogging": true,
        "contentVersion": "1.4.4.0.preview.2",
        "panelizationSummary": {
          "containsEpubBubbles": false,
          "containsImageBubbles": false
        },
        "imageLinks": {
          "smallThumbnail": "http://books.google.com/books/content?id=it5B-Y2EQhoC&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
          "thumbnail": "http://books.google.com/books/content?id=it5B-Y2EQhoC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
        },
        "language": "en",
        "previewLink": "http://books.google.co.in/books?id=it5B-Y2EQhoC&printsec=frontcover&dq=good+omens&hl=&cd=9&source=gbs_api",
        "infoLink": "http://books.google.co.in/books?id=it5B-Y2EQhoC&dq=good+omens&hl=&source=gbs_api",
        "canonicalVolumeLink": "https://books.google.com/books/about/Coraline_10th_Anniversary_Edition.html?hl=&id=it5B-Y2EQhoC"
      },
      "saleInfo": {
        "country": "IN",
        "saleability": "NOT_FOR_SALE",
        "isEbook": false
      },
      "accessInfo": {
        "country": "IN",
        "viewability": "PARTIAL",
        "embeddable": true,
        "publicDomain": false,
        "textToSpeechPermission": "ALLOWED_FOR_ACCESSIBILITY",
        "epub": {
          "isAvailable": true,
          "acsTokenLink": "http://books.google.co.in/books/download/Coraline_10th_Anniversary_Edition-sample-epub.acsm?id=it5B-Y2EQhoC&format=epub&output=acs4_fulfillment_token&dl_type=sample&source=gbs_api"
        },
        "pdf": {
          "isAvailable": false
        },
        "webReaderLink": "http://play.google.com/books/reader?id=it5B-Y2EQhoC&hl=&printsec=frontcover&source=gbs_api",
        "accessViewStatus": "SAMPLE",
        "quoteSharingAllowed": false
      },
      "searchInfo": {
        "textSnippet": "This edition of New York Times bestselling and Newbery Medal-winning author Neil Gaiman’s modern classic, Coraline—also an Academy Award-nominated film—is enriched with a foreword from the author, a reader's guide, and more."
      }
    },
    {
      "kind": "books#volume",
      "id": "RRFKAQAAQBAJ",
      "etag": "ZISYdEsmwSw",
      "selfLink": "https://www.googleapis.com/books/v1/volumes/RRFKAQAAQBAJ",
      "volumeInfo": {
        "title": "Only Begotten Daughter",
        "authors": [
          "James Morrow"
        ],
        "publisher": "Hachette UK",
        "publishedDate": "2013-10-31",
        "description": "It could only happen in New Jersey. Call it a miracle. Call it the Second Coming. Call it a mishap at the sperm bank. But somehow, a baby daughter was born to the virgin Murray Katz, and her name is Julie. She can heal the blind, raise the dead, and generate lots of publicity. In fact, the poor girl needs a break, even if it means a vacation in Hell (which is unseasonably warm). So what did you expect? It ain't easy being the Daughter of God...",
        "industryIdentifiers": [
          {
            "type": "ISBN_13",
            "identifier": "9780575081932"
          },
          {
            "type": "ISBN_10",
            "identifier": "0575081937"
          }
        ],
        "readingModes": {
          "text": true,
          "image": false
        },
        "pageCount": 312,
        "printType": "BOOK",
        "categories": [
          "Fiction"
        ],
        "averageRating": 3.5,
        "ratingsCount": 11,
        "maturityRating": "NOT_MATURE",
        "allowAnonLogging": false,
        "contentVersion": "1.4.5.0.preview.2",
        "panelizationSummary": {
          "containsEpubBubbles": false,
          "containsImageBubbles": false
        },
        "imageLinks": {
          "smallThumbnail": "http://books.google.com/books/content?id=RRFKAQAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
          "thumbnail": "http://books.google.com/books/content?id=RRFKAQAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
        },
        "language": "en",
        "previewLink": "http://books.google.co.in/books?id=RRFKAQAAQBAJ&printsec=frontcover&dq=good+omens&hl=&cd=10&source=gbs_api",
        "infoLink": "https://play.google.com/store/books/details?id=RRFKAQAAQBAJ&source=gbs_api",
        "canonicalVolumeLink": "https://play.google.com/store/books/details?id=RRFKAQAAQBAJ"
      },
      "saleInfo": {
        "country": "IN",
        "saleability": "FOR_SALE",
        "isEbook": true,
        "listPrice": {
          "amount": 551.06,
          "currencyCode": "INR"
        },
        "retailPrice": {
          "amount": 275.53,
          "currencyCode": "INR"
        },
        "buyLink": "https://play.google.com/store/books/details?id=RRFKAQAAQBAJ&rdid=book-RRFKAQAAQBAJ&rdot=1&source=gbs_api",
        "offers": [
          {
            "finskyOfferType": 1,
            "listPrice": {
              "amountInMicros": 551060000,
              "currencyCode": "INR"
            },
            "retailPrice": {
              "amountInMicros": 275530000,
              "currencyCode": "INR"
            }
          }
        ]
      },
      "accessInfo": {
        "country": "IN",
        "viewability": "PARTIAL",
        "embeddable": true,
        "publicDomain": false,
        "textToSpeechPermission": "ALLOWED_FOR_ACCESSIBILITY",
        "epub": {
          "isAvailable": true,
          "acsTokenLink": "http://books.google.co.in/books/download/Only_Begotten_Daughter-sample-epub.acsm?id=RRFKAQAAQBAJ&format=epub&output=acs4_fulfillment_token&dl_type=sample&source=gbs_api"
        },
        "pdf": {
          "isAvailable": false
        },
        "webReaderLink": "http://play.google.com/books/reader?id=RRFKAQAAQBAJ&hl=&printsec=frontcover&source=gbs_api",
        "accessViewStatus": "SAMPLE",
        "quoteSharingAllowed": false
      },
      "searchInfo": {
        "textSnippet": "It could only happen in New Jersey."
      }
    }
  ]
}

"""