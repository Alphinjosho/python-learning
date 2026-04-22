stocks = [
    {"symbol": "INFY", "price": 1500, "volume": 2000000},
    {"symbol": "TCS", "price": 3200, "volume": 1500000},
    {"symbol": "INFY", "price": 1520, "volume": 1800000},
    {"symbol": "TCS", "price": 3300, "volume": 1700000},
    {"symbol": "WIPRO", "price": 450, "volume": 800000}
]
g_stock = {}

for stock in stocks :
    symbol = stock ["symbol"]
    price  = stock ["price"]
    volume = stock ["volume"]

    if symbol not in g_stock :
       g_stock [symbol]={
         "prices" : [price],
         "total_volume":volume
       }
    else : 
       g_stock [symbol]["prices"].append(price) 
       g_stock [symbol]["total_volume"] += volume

final_output = {} 

for a_stock in g_stock:
   data = g_stock[a_stock]
   all_prices = data ["prices"]
   avg=sum (all_prices)/len(all_prices)

          
   final_output [a_stock] = {
       "avg_price":avg,
       "Total_volume":data["total_volume"]
 }
print(final_output)