# Buy and sell books. Follow-up: if with expiration time
# You operate a marketplace for buying & selling used textbooks. For a given textbook, e.g. “Theory of Cryptography,” there are people who want to buy this textbook and people who want to sell.
#   Offers to BUY: $100, $100, $99, $99, $97, $90
#   Offers to SELL: $109, $110, $110, $114, $115, $119
# A match occurs when two people agree on a price. Some new offers do not match. These offers should be added to the active set of offers. For example:
#   Tim offers to SELL at $150. This will not match. No one is willing to buy at that price so we save the offer.
#   Offers to SELL:: $109, $110, $110, $114, $115, $119, $150
# When matching we want to give the customer the “best price”. Example matches:
#   If Jane offers to BUY at $120, she will match and buy a book for $109 (the lowest offer to sell is the best price). The sell offers should be updated to reflect the match
#   Offers to SELL: $110, $110, $114, $115, $119, $150
# If Connie offers to SELL at $99 she will match and sell her book for $100 (the highest offer to buy is the best price). The buy offers should be updated to reflect the match
#   Offers to BUY: $100, $99, $99, $97, $90
# Our system will need to:
#   Accept incoming offers to buy & sell
#   Output if the price matches
#   Keep an updated collections of buys & sells

# Follow up: implement an order which can expire，e.g. buyer’s order valid for 10 min，and then auto expire
# O(logn) complicity
import heapq
class buy_sell_books:
    def __init__(self,buy_list=[],sell_list=[]):
        self.buy_list=buy_list
        self.sell_list=sell_list
    
    def buy(self,buy_value):
        # update buy and sell_list
        temp=[]
        for i in self.sell_list:
            if i>=buy_value:
                temp.append(i)
        if not temp:
            heapq.heappush(self.buy_list,buy_value)
            return -1
        best_buy_price=heapq.nsmallest(1, self.sell_list, key=None)
        heapq.heappop(best_buy_price)
        return best_buy_price

    def sell(self,sell_value):
        temp=[]
        for i in self.buy_list:
            if i>=sell_value:
                temp.append(i)
        if not temp:
            heapq.heappush(self.sell_list,sell_value)
            return -1
        best_sell_price=heapq.nsmallest(1, self.buy_list, key=None)
        heapq.heappop(best_sell_price)
        return best_sell_price

buy=[100, 100, 99, 99, 97, 90]
sell=[109, 110, 110, 114, 115, 119]
buy_sell_books=buy_sell_books(buy,sell)
print(buy_sell_books.sell(150))
print(buy_sell_books.buy_list)
print(buy_sell_books.sell_list)

print(buy_sell_books.buy(120))
print(buy_sell_books.buy_list)
print(buy_sell_books.sell_list)

