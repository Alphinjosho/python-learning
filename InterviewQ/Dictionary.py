stocks = [
    {"symbol": "INFY", "price": 1500, "volume": 2000000},
    {"symbol": "TCS", "price": 3200, "volume": 1500000},
    {"symbol": "WIPRO", "price": 450, "volume": 800000},
    {"symbol": "INFY", "price": 1520, "volume": 1800000},
    {"symbol": "TCS", "price": 3300, "volume": 1700000},
]
g_stock={}

# for stock in stocks:
#   symbol = stock ["symbol"]
#   price = stock ["price"] 
#   if(symbol not in g_stock):
#     g_stock[symbol]=[price]
#   else: g_stock [symbol].append(price)

# print (g_stock)

# g_stock["TCS"] = [3200]
# g_stock["TCS"].append(3300)
# print(g_stock) # this is How Manually DO 

#Lets Update this code to Loop and IF condiction 

for stk in stocks:
     symbol = stk ["symbol"]
     price = stk ["price"]
     if(symbol not in g_stock):
        g_stock [symbol]=[price]     # This was i write in My Own 
     else:
         g_stock [symbol].append(price)
print(g_stock)


# NOW Going To Using Data

avg_result={}

for r_stock in g_stock:
    prices = g_stock[r_stock]
    add = 0
    for A_price in prices:
     add = add + A_price 
    avarage = add / len(prices)

    avg_result [r_stock]=avarage

print(avg_result)