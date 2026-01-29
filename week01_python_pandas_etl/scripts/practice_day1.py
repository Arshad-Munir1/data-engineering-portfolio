sales = [120, 300, 450, 200]

total_sales = sum(sales)
average_sales = total_sales / len(sales)
max_sales = max(sales)

print("Total Sales:", total_sales)
print("Average Sales:", average_sales)
print("Highest Sales", max_sales)

product = {
    "name": "T-Shirt",
    "price": 25,
    "stock": 120
}

stock_value = product["price"] * product["stock"]

print("Product Name:", product["name"])
print("Stock Value:", stock_value)