-- Synthetic fixture cafe-v1. Amounts are integer VND.
PRAGMA foreign_keys = ON;
CREATE TABLE customers (
  customer_id INTEGER PRIMARY KEY,
  customer_name TEXT NOT NULL
);
CREATE TABLE orders (
  order_id INTEGER PRIMARY KEY,
  customer_id INTEGER REFERENCES customers(customer_id),
  business_date TEXT NOT NULL,
  amount_vnd INTEGER NOT NULL CHECK (amount_vnd >= 0),
  status TEXT NOT NULL CHECK (status IN ('paid', 'cancelled'))
);
CREATE TABLE payments (
  payment_id INTEGER PRIMARY KEY,
  order_id INTEGER NOT NULL REFERENCES orders(order_id),
  status TEXT NOT NULL CHECK (status IN ('success', 'failed'))
);
INSERT INTO customers VALUES (1,'An'),(2,'Bình'),(3,'Chi');
INSERT INTO orders VALUES
 (101,1,'2026-09-01',40000,'paid'),
 (102,1,'2026-09-01',60000,'paid'),
 (103,2,'2026-09-02',50000,'paid'),
 (104,NULL,'2026-09-02',30000,'cancelled');
INSERT INTO payments VALUES (1,101,'failed'),(2,101,'success'),(3,102,'success'),(4,103,'success');
