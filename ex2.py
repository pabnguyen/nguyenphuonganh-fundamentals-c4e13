prices = {
    'banana' : 4,
    'apple'  : 2,
    'orange' : 1.5,
    'pear'   : 3
}

print(prices)

stock = {}

stock ["banana"] = 6
stock ["apple"]  = 0
stock ["orange"] = 22
stock ["pear"]   = 15

print(stock)

for i in prices:
    print("{0}: {1}".format(i, prices[i]))
    print("{0}: {1} \n".format(i, stock[i]))

total = 0

for i in prices:
    product = prices[i] * stock[i]
    print("If I sold all {0}, I will get: ${1}".format(i, product))
    total += product

# for i in prices:
    # print("{0}: {1}".format(i, prices[i]))
    # print("{0}: {1} \n".format(i, stock[i]))
