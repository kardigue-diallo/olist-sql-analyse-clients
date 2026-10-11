CREATE INDEX IF NOT EXISTS idx_customers_id ON olist_customers_dataset(customer_id);
CREATE INDEX IF NOT EXISTS idx_customers_unique ON olist_customers_dataset(customer_unique_id);
CREATE INDEX IF NOT EXISTS idx_orders_customer ON olist_orders_dataset(customer_id);
CREATE INDEX IF NOT EXISTS idx_items_order ON olist_order_items_dataset(order_id);