-- DAY 10: Transactions & ACID (Using Game Sales Dataset)

--ROLLBACK Example


BEGIN;

-- Temporarily boost sales for a specific game (fake update)
UPDATE salesdb.sales_data sd
SET Global_Sales = Global_Sales + 1
WHERE Name = 'Wii Sports';

-- Check temporary values
SELECT Name, Global_Sales
FROM salesdb.sales_data sd
WHERE Name = 'Wii Sports';

-- Undo everything
ROLLBACK;

-- COMMIT Example

BEGIN;

-- Increase EU_Sales for Nintendo games (example)
UPDATE salesdb.sales_data sd
SET EU_Sales = EU_Sales + 0.1
WHERE Publisher = 'Nintendo';

-- Make permanent
COMMIT;


-- C. ACID EXPLANATION (4 PROPERTIES OF TRANSACTIONS IN SQL)
-- A: Atomicity   = Transaction is all-or-nothing.
-- C: Consistency = Database goes from valid state to valid state.
-- I: Isolation   = Simultaneous transactions don't interfere.
-- D: Durability  = Once COMMIT happens, change is permanent.
