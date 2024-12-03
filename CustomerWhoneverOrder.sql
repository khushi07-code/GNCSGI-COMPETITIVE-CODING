SELECT Customers.name as customer
FROM Customers
WHERE Customers.id NOT IN (
    SELECT Orders.customerId
    FROM Orders
);
