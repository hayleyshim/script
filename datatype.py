mycoin = 'nft'

print(mycoin[0])
print(mycoin[1])

greeting = "hello"
greeting[0:5]

bitcoin = 9744000
ripple = 711

bitcoin *= 10
ripple *= 430

print(bitcoin+ripple)

hold1 = "bitcoin"
hold2 = "ripple"
hold3 = "ethereum"

hold = ["bit_krw","xrp_krw","eth_krw"]
hold[0] = "bch_krw"
print(hold[0])
print(hold[1])
print(hold[2])

portfolio = ["BTC", "ETH", "XRP", "BCH", "DASH"]
print(portfolio[0:3])

portfolio = []
portfolio.append("BTC")
portfolio.append("ETH")
portfolio.append("XRP")
print(portfolio)

portfolio.insert(1,"DASH")
print(portfolio)

del portfolio[1]
print(portfolio)

ripple_close = [503, 505, 508, 501, 530]
print(max(ripple_close))
print(min(ripple_close))

a = [1,2,3,4]
average = sum(a) / len(a)
print(average)

print(portfolio[0])
print(portfolio[1])

print(portfolio[0:2])

portfolio = ("ETC", "ETH", "BTC")

#portfolio.append("XRP")

#del portfolio[0]
#print(portfolio)

icecream_price = [500, 1000]

prices = {'BTC': 8300000, 'XRP': 514}

prices = {}
prices['BTC'] = 8300000
prices['XRP'] = 514

prices['ETH'] = 60000

prices['XRP'] = 500
del prices['XRP']
print(prices)
print(prices.keys())
print(prices.values())

