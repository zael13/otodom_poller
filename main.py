import time
from datetime import date

from otodom import otodom
from offer import offer
import csv

if __name__ == '__main__':
    offers = otodom.find_sell_offers(otodom.construct_url(14))
    links = set()
    for i in offers:
        links.add(f"https://www.otodom.pl{i.get('href')}")
    print(f"Offers number: {len(links)}")

    today = date.today()
    with open(f"offers_{today.strftime('%Y%m%d')}.csv", 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(offer.Offer.get_csv_header())

        for link in links:
            data = otodom.parse_offer(link)
            if data:
                res = offer.Offer(data)
                print(res)
                csv_writer.writerow(res.to_csv())
            if not data:
                time.sleep(10)
            time.sleep(1)
