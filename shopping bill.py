def calculateElectronicsGST(a, b): return (a + b) * 1.18
def calculateFashionGST(c, d): return (c + d) * 1.13
def calculateFoodGST(e): return e * 1.07
def totalBill(a, b, c, d, e): return calculateElectronicsGST(a, b) + calculateFashionGST(c, d) + calculateFoodGST(e)
def calculateDiscountedBill(a, b, c, d, e):
    tot = totalBill(a, b, c, d, e)
    disc = tot * 0.2
    return tot, disc, tot - disc

# Sample test values
a = b = c = d = e = 100
total, discount, final = calculateDiscountedBill(a, b, c, d, e)

print(f"Total after GST = {total:.2f} | Discount = {discount:.2f} | Final payable amount = {final:.2f}")