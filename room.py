import requests
from bs4 import BeautifulSoup as Bs

urls_new = ['-11-pro-max/', '-11-pro/', '-xs-max/', '-xs/', '-xr/', '-x/', '-8-plus/', '-8/']
urls_used = ['-11-pro-max-bu/', '-11-pro-bu/', '-xs-max-bu/', '-xs-bu/', '-xr-bu/', '-x-bu/', '-8-plus-bu/', '-8-bu/']
pages = []


class AppleRoom:
    def new(self):
        room_new_p1 = []
        room_new_p2 = []
        for x in urls_new:
            pages.append(requests.get('https://appleroom.ua/category/iphone' + x))
            for r in pages:
                pages.clear()
                html = Bs(r.content, 'html.parser')
                for el in html.select('.product-card'):
                    name = el.select('div[itemprop="name"] > a')
                    if 'Dual Sim' in name[0].text or 'Dual-Sim' in name[0].text:
                        continue
                    else:
                        price = el.select('.product-card__price > .usd')
                        new = name[0].text + price[0].text
                        if len(room_new_p1) > 50:
                            room_new_p2.append(new)
                        else:
                            room_new_p1.append(new)
        return "".join(room_new_p1) + "".join(room_new_p2)

    def used(self):
        room_used_p1 = []
        room_used_p2 = []
        for x in urls_used:
            pages.append(requests.get('https://appleroom.ua/category/iphone' + x))
            for r in pages:
                pages.clear()
                html = Bs(r.content, 'html.parser')
                for el in html.select('.product-card'):
                    name = el.select('div[itemprop="name"] > a')
                    aviability = el.select('.availability')
                    if 'В наявності' in aviability[0].text:
                        if 'Dual Sim' in name[0].text or 'Dual-Sim' in name[0].text:
                            continue
                        else:
                            price = el.select('.product-card__price > .usd')
                            used = name[0].text + price[0].text
                            if len(room_used_p1) > 50:
                                room_used_p2.append(used)
                            else:
                                room_used_p1.append(used)
        return "".join(room_used_p1) + "".join(room_used_p1)

