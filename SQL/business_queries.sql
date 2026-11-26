-- Project 2: Superstore SQL Business Q&A
-- Database: PostgreSQL 16, table: superstore (9,994 rows)

-- Q1: What are total sales and profit by region?
SELECT region, SUM(sales) AS total_sales, SUM(profit) AS total_profit
FROM superstore
GROUP BY region
ORDER BY total_profit DESC;

-- Q2: Which region has the worst profit margin?
WITH region_totals AS (
    SELECT region, SUM(sales) AS total_sales, SUM(profit) AS total_profit
    FROM superstore GROUP BY region
)
SELECT region, total_sales, total_profit,
       ROUND((total_profit / total_sales * 100)::numeric, 2) AS profit_margin_pct
FROM region_totals
ORDER BY profit_margin_pct ASC;

-- Q3: Which product category is least profitable?
SELECT category, SUM(profit) AS total_profit
FROM superstore
GROUP BY category
ORDER BY total_profit ASC;

-- Q4: Which sub-categories lose money?
SELECT sub_category, SUM(profit) AS total_profit
FROM superstore
GROUP BY sub_category
HAVING SUM(profit) < 0
ORDER BY total_profit ASC;

-- Q5: What is the average discount by category?
SELECT category, ROUND(AVG(discount)::numeric, 3) AS avg_discount
FROM superstore
GROUP BY category
ORDER BY avg_discount DESC;

-- Q6: Which ship mode has the highest average profit per order?
SELECT ship_mode, ROUND(AVG(profit)::numeric, 2) AS avg_profit_per_order
FROM superstore
GROUP BY ship_mode
ORDER BY avg_profit_per_order DESC;

-- Q7: Top 5 states by total profit
SELECT state, SUM(profit) AS total_profit
FROM superstore
GROUP BY state
ORDER BY total_profit DESC
LIMIT 5;

-- Q8: Do high discounts hurt profit? Average profit by discount band
SELECT
    CASE
        WHEN discount = 0 THEN 'No discount'
        WHEN discount <= 0.2 THEN '1-20%'
        WHEN discount <= 0.4 THEN '21-40%'
        ELSE 'Above 40%'
    END AS discount_band,
    COUNT(*) AS num_orders,
    ROUND(AVG(profit)::numeric, 2) AS avg_profit
FROM superstore
GROUP BY discount_band
ORDER BY avg_profit DESC;