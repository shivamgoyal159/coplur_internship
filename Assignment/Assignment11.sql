--1. Total amount each customer spent:

SELECT s.customer_id, SUM(m.price) AS total_spent
FROM sales s
JOIN menu m ON s.product_id = m.product_id
GROUP BY s.customer_id;

--2.How many days each customer visited the restaurant:

SELECT customer_id, COUNT(DISTINCT order_date) AS visit_days
FROM sales
GROUP BY customer_id;

--3. First item purchased by each customer:

SELECT customer_id, product_name
FROM (
  SELECT s.customer_id, s.order_date, m.product_name,
         RANK() OVER (PARTITION BY s.customer_id ORDER BY s.order_date) AS rk
  FROM sales s
  JOIN menu m ON s.product_id = m.product_id
) x
WHERE rk = 1;

--4. Most purchased item overall and how many times:

SELECT m.product_name, COUNT(*) AS total_purchases
FROM sales s
JOIN menu m ON s.product_id = m.product_id
GROUP BY m.product_name
ORDER BY total_purchases DESC
LIMIT 1;

--5. Most popular item for each customer:

SELECT customer_id, product_name, COUNT(*) AS total
FROM sales s
JOIN menu m ON s.product_id = m.product_id
GROUP BY customer_id, product_name
QUALIFY RANK() OVER (PARTITION BY customer_id ORDER BY COUNT(*) DESC) = 1;

--6. First item after becoming a member:

SELECT s.customer_id, s.order_date, m.product_name
FROM sales s
JOIN menu m ON s.product_id = m.product_id
JOIN members mem ON s.customer_id = mem.customer_id
WHERE s.order_date >= mem.join_date
  AND s.order_date = (
    SELECT MIN(order_date)
    FROM sales
    WHERE customer_id = s.customer_id AND order_date >= mem.join_date
  );

--7. Item just before becoming a member:

SELECT s.customer_id, s.order_date, m.product_name
FROM sales s
JOIN menu m ON s.product_id = m.product_id
JOIN members mem ON s.customer_id = mem.customer_id
WHERE s.order_date < mem.join_date
  AND s.order_date = (
    SELECT MAX(order_date)
    FROM sales
    WHERE customer_id = s.customer_id AND order_date < mem.join_date
  );

--8. Total items and amount spent before becoming a member:

SELECT s.customer_id, COUNT(*) AS total_items, SUM(m.price) AS total_amount
FROM sales s
JOIN menu m ON s.product_id = m.product_id
JOIN members mem ON s.customer_id = mem.customer_id
WHERE s.order_date < mem.join_date
GROUP BY s.customer_id;

--9. Points per customer (10 pts per $1, sushi ×2 points):

SELECT s.customer_id,
       SUM(
         CASE
           WHEN m.product_name = 'sushi' THEN m.price * 10 * 2
           ELSE m.price * 10
         END
       ) AS total_points
FROM sales s
JOIN menu m ON s.product_id = m.product_id
GROUP BY s.customer_id;

--10. Points till end of January with double points in first week after joining:

SELECT s.customer_id,
       SUM(
         CASE
           WHEN s.order_date BETWEEN mem.join_date AND mem.join_date + INTERVAL '6 day'
           THEN m.price * 10 * 2
           WHEN m.product_name = 'sushi'
           THEN m.price * 10 * 2
           ELSE m.price * 10
         END
       ) AS jan_points
FROM sales s
JOIN menu m ON s.product_id = m.product_id
JOIN members mem ON s.customer_id = mem.customer_id
WHERE s.order_date <= '2021-01-31'
GROUP BY s.customer_id;