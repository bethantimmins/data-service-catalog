from lib.catalog import register_service

@register_service("services/customer_orders.yml")
def customer_orders_pipeline(run_date=None):
    # Example: your extract/transform/load steps would go here
    # This function being imported is enough to register its metadata.
    return "ok"
