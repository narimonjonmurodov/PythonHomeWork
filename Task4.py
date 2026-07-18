from machine import Machine

products = {"cofee": {"price": 150}, "tea": {"price": 90}, "hot_chocolate": {"price": 120}, "cola": {"price": 80}}
amount = 10

m = Machine(products, amount)

while True:
    try:
        m.run()
    except Exception as e:
        print(e)
