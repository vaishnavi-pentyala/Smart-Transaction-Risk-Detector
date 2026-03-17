Smart Transaction Risk Detector

 1. Algorithm Explanation
This program first takes the number of transactions as input and then accepts each transaction amount one by one.
All transactions are stored in a list and classified into categories such as normal, large, high risk, and invalid using conditions.
A dictionary is used to store these categorized transactions.
List comprehension is used to filter valid (positive) transactions.
The program then calculates total amount and checks patterns like frequent transactions, large spending, and suspicious activity.
Finally, based on these conditions, the overall risk is classified as Low Risk, Moderate Risk, or High Risk.

 2. Test Cases
Test Case 1:
Input:
Enter number of transactions: 4
Enter transaction: 100
Enter transaction: 600
Enter transaction: 3000
Enter transaction: -50
Output:

Normal: [100]
Large: [600]
High Risk: [3000]
Invalid: [-50]
Total: 3700
Count: 4
Final Risk: Low Risk

 Test Case 2:

Input:
Enter number of transactions: 6
Enter transaction: 1000
Enter transaction: 2500
Enter transaction: 3000
Enter transaction: 4000
Enter transaction: 1500
Enter transaction: 200

Output:

 Normal: [200]
 Large: [1000, 1500]
 High Risk: [2500, 3000, 4000]
 Total: 12200
 Count: 6
 Final Risk: High Risk


 3. Reflection

 I made  how to determine the final risk level based on multiple conditions.
I decided that if there are 3 or more high-risk transactions, the result should immediately be classified as High Risk.
I also considered combining frequent transactions and large spending to increase the risk level.
This approach helps in identifying suspicious transaction patterns more effectively rather than relying on a single condition.
