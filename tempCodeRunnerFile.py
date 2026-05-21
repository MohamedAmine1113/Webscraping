 def get_firma_infos(section):

        firma_name = section.find_all('div', {'class' : 'angebotskontakt'}).text.strip() 

        print(firma_name)