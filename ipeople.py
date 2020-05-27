from bs4 import BeautifulSoup as Bs
import cfscrape

scraper = cfscrape.create_scraper()

urls_new = ['iphone-11', 'iphone-11-pro', 'iphone-11-pro-max', 'iphone-xs-max', 'iphone-xs', 'iphone-x', 'iphone-xr',
            'iphone-8-plus', 'iphone-8']
urls_used = ['bu-iphone-11', 'bu-iphone-11-pro', 'bu-iphone-11-pro-max', '-bu-iphone-xs-max', 'bu-iphone-xs',
             'bu-iphone-xr', 'bu-iphone-x', 'bu-iphone-8-plus', 'bu-iphone-8', 'bu-iphone-7-plus', 'bu-iphone-7']
pages =[]


class Ipeople:
    def new(self):
        people_new = []
        for x in urls_new:
            pages.append(scraper.get("http://www.ipeople.in.ua/catalog/" + x))
            for r in pages:
                pages.clear()
                html = Bs(r.content, 'html.parser')
                for el in html.select('.product'):
                    name = el.select('.fixed > a')
                    formated_name = []
                    if '(' not in name[0].text:
                        formated_name.append(name[0].text)
                    for i in name[0].text:
                        if i == '(':
                            formated_name.append(name[0].text[0:name[0].text.index(i)])
                    name_string = "".join(formated_name)
                    if 'Dual Sim' in name_string or 'Dual-Sim' in name_string:
                        continue
                    else:
                        price = el.select('.yui3-u-1-3.usd')
                        new = name_string + price[0].text
                        people_new.append(new + '\n')
        return "".join(people_new)
    def used(self):
        people_used = []
        for x in urls_used:
            pages.append(scraper.get("http://www.ipeople.in.ua/catalog/" + x))
            for r in pages:
                pages.clear()
                html = Bs(r.content, 'html.parser')
                for el in html.select('.product'):
                    name = el.select('.fixed > a')
                    formated_name = []
                    if '(' not in name[0].text:
                        formated_name.append(name[0].text)
                    for i in name[0].text:
                        if i == '(':
                            formated_name.append(name[0].text[3:name[0].text.index(i)])
                        if len(formated_name) > 1:
                            del formated_name[0]
                    name_string = "".join(formated_name).replace('GB', '')
                    if 'Dual Sim' in name_string or 'Dual-Sim' in name_string:
                        continue
                    else:
                        price = el.select('.yui3-u-1-3.usd')
                        used = name_string + price[0].text
                        people_used.append(used + '\n')
        return "".join(people_used)

