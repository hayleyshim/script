ripple=[500, 510, 520, 530, 540, 550]

for close in ripple:
    print(close)

for 좌석 in ['좌석1','좌석2','좌석3','좌석4','좌석5']:
    print(좌석, "확인")

for num in range(1,11,3):
    print(num)

cur_price = {"BTC" : 1000, "XRP":500}

for ticker in cur_price:
    print((ticker))

for ticker, price in cur_price.items():
    print(ticker, price)

for ticker in cur_price:
    print(ticker, cur_price[ticker])

for close in ripple:
    if close >= 520:
        print(close)