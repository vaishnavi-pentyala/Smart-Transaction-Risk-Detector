n = int(input("Enter number of transactions: "))
transactions = []
for i in range(n):
    t = int(input("Enter transaction: "))
    transactions.append(t)
data = {
    "normal": [],
    "large": [],
    "high_risk": [],
    "invalid": []
}
for t in transactions:
    if t <= 0:
        data["invalid"].append(t)
    elif t <= 500:
        data["normal"].append(t)
    elif t <= 2000:
        data["large"].append(t)
    else:
        data["high_risk"].append(t)

valid = [t for t in transactions if t > 0]

count = len(valid)
total = sum(valid)

frequent = n > 5
large_spending = total > 5000
suspicious = len(data["high_risk"]) >= 3

if suspicious or (frequent and large_spending):
    risk = "High Risk"
elif frequent or large_spending:
    risk = "Moderate Risk"
else:
    risk = "Low Risk"

print("\nCategorized:", data)
print("Total:", total)
print("Count:", n)
print("Final Risk:", risk)