CREATE TABLE products (
    Product_ID INT PRIMARY KEY,
    Product_Name VARCHAR(255),
    Category VARCHAR(100),
    Brand VARCHAR(100),
    Cost_Price INT,
    Selling_Price INT,
    Supplier_ID INT,
    Launch_Date DATE,
    Status VARCHAR(20)
);

SELECT * FROM products ;


 ---Show only Active products
 SELECT *
 FROM products
 WHERE status = 'Active';

 ---Show products with Selling Price greater than or equal to ₹10,000

 SELECT *
 FROM products
 WHERE selling_price >= 10000;

 --- total product count

 SELECT COUNT(*) as Total_products
 FROM products;


 ---Show Active Logitech or Sony products

 SELECT *
 FROM products
 WHERE status = 'Active'
 AND Brand IN ('Logitech','Sony');

 ---Average Selling Price by Category

 SELECT category,
 ROUND(AVG(selling_price),2) AS Avg_selling_price
 FROM products
 GROUP BY category;

 ---Total Selling Price by Category

SELECT category,
SUM(selling_price) AS Total_selling_price
FROM products
GROUP BY category;


---Product Count by Category
SELECT category,
COUNT(product_id) AS product_count
FROM products
GROUP BY category;


---Minimum and Maximum Selling Price by Category

SELECT category,
MIN(selling_price) AS Minimum_selling_price,
MAX(selling_price) AS Maximum_selling_price
FROM products
GROUP BY category;


---Show the 10 most expensive products.

SELECT *
FROM products
ORDER BY selling_price DESC
LIMIT 10;

---Show only those categories whose average selling price is greater than ₹5000.

SELECT category,
AVG(selling_price) AS avg_price
FROM products
GROUP BY category
HAVING AVG(selling_price) > 5000;



