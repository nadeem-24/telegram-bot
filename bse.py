# python 3
# bse.py
from bsedata.bse import BSE


class Data:

    global obj
    obj = BSE(update_codes=True)

    # function to fetch today's top gainers
    def top_gainers():
        gainers = obj.topGainers()
        li = []

        for i in range(len(gainers)):
            li.append(gainers[i]['securityID'])

        return li

    # function to fetch today's top losers
    def top_losers():
        losers = obj.topLosers()
        li = []

        for i in range(len(losers)):
            li.append(losers[i]['securityID'])

        return li


if __name__ == "__main__":
    Data.top_gainers()
    Data.top_losers()
