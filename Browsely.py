####################################################################################################################################
####################################################################################################################################
####################################################################################################################################

########################################### Work Done by- **Unown** & **simpfordeath** #############################################
#################################################### media bot for telegram ########################################################
############################## Uses beautifulSoup , pafy ,wikipediaapi and youtube_search ##########################################
############################### CUrrent commands include /start,/down,/search,/wiki,/help ##########################################

####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
# import module 
import requests  
import bs4  
  

def google(query):         #simpfordeath

    url = "https://google.com/search?q=" + query 
  
    # Sending HTTP request  
    request_result = requests.get( url ) 
    
    # Pulling HTTP data from internet  
    soup = bs4.BeautifulSoup( request_result.text  
                            , "html.parser" ) 
    
    #class "BNeawe".  
    res = soup.find( "div" , class_='BNeawe' ).text
    return res


def bele():
    import sys
    import telebot
    def tele():
        bot = telebot.TeleBot("1615198888:AAEko0OahhRTrY2V7cr2YWbgjcXzWVkTYNQ", parse_mode=None)
        @bot.message_handler(commands=['start', 'help'])
        def send_welcome(message):
            bot.reply_to(message, '''
            WELCOME TO BROWSELY!!!
            
            Ver-1.01 Release 
            YOUR ONE STOP BOT FOR ENTERTAINMENT AND WEBSCRAPING : 0

            *******************************************************
            ********MADE BY **UNOWN** & **SIMPFORDEATH*************
            *******************************************************
            Current commands list includes-
            /down -- To download a youtube video 
            /search -- To search for a search term on google
            /wiki -- To search for a term on wikipedia 
            -------------------------------------------------------
            Thank you for using BROWSELY                    
            ''')


###############DOWNLOAD COMMAND BLOCK 
        @bot.message_handler(commands=['down'])       
        def youtube(message):
            import re
            ss=message.text+' 1969so420'
            wtemp=re.search('/down (.+?) 1969so420',ss)
            print(ss)
            if wtemp:
                pterm=wtemp.group(1)
                print(pterm)
                from youtube_search import YoutubeSearch
                results = YoutubeSearch(pterm, max_results=1).to_dict()
                pterm='www.youtube.com/'+results[0]['url_suffix']
                import pafy 
                v=pafy.new(pterm)
                v=v.getbest()
                bot.reply_to(message,v.url)
            else:
                bot.reply_to(message,'Please input a proper search term')


#######SEARCH COMMAND BLOCK 
        @bot.message_handler(commands=['search'])
        def gsearch(message):
            import re
            ss=message.text+' 1969so420'
            wtemp=re.search('/search (.+?) 1969so420',ss)
            print(ss)
            if wtemp:
                wterm=wtemp.group(1)
                bot.reply_to(message,google(wterm))
            else:
                bot.reply_to(message,"Please add search term")

                
#######Wikipedia COMMAND BLOCK
        @bot.message_handler(commands=['wiki'])
        def wiki(message):
            import re
            ss=message.text+' 1969so420'
            wtemp=re.search('/wiki (.+?) 1969so420',ss)
            print(ss)
            if wtemp:
                wterm=wtemp.group(1)
                print(wterm)
                import wikipediaapi
                wiki=wikipediaapi.Wikipedia('en')
                page=wiki.page(wterm)
                print(page.summary)
                if page.exists()==False:
                    bot.reply_to(message,"Invalid page name please re enter proper name")
                else:
                    link="Link to url: "+page.fullurl
                    if len(page.summary)<200:
                        bot.reply_to(message,page.summary)
                    else:
                        sumtemp=re.search('(.+?)$',page.summary,re.MULTILINE)
                        bot.reply_to(message,sumtemp.group(1))
                    bot.reply_to(message,link)
            else:
                bot.reply_to(message,"Please input a search term")


        @bot.message_handler(func=lambda message: True)
        def getmessage(message):
            return message.text

        bot.polling()

    try:
        tele()
    except:
        print(sys.exc_info()[0])
        bele()
bele()