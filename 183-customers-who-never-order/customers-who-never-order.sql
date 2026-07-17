SELECT Customers.name AS Customers from Customers 
FULL OUTER JOIN Orders
ON Customers.id = Orders.id
WHERE Customers.id NOT IN (SELECT customerId FROM Orders)
