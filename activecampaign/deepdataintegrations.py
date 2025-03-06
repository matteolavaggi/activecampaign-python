class DeepDataIntegrations(object):
    def __init__(self, client):
        self.client = client

    def create_a_connection(self, data):
        """
        Create a connection resource


        Args:
            data:

        Returns:

        """
        return self.client._post("/connections", json=data)

    def retrieve_a_connection(self, connection_id):
        """
        Retrieve an existing connection resource


        Args:
            connection_id:

        Returns:

        """
        return self.client._get("/connections/{}".format(connection_id))

    def update_a_connection(self, connection_id, data):
        """
        Update an existing connection resource


        Args:
            connection_id:
            data:

        Returns:

        """
        return self.client._put("/connections/{}".format(connection_id), json=data)

    def delete_a_connection(self, connection_id):
        """
        Delete an existing connection resource


        Args:
            connection_id:

        Returns:

        """
        return self.client._delete("/connections/{}".format(connection_id))

    def list_all_connections(self):
        """List all deep data connections/integrations.

        Returns:
            dict: List of all connections
        """
        return self.client._get("/connections")

    def get_connection_by_name(self, service_name):
        """Get a connection by service name.

        Args:
            service_name (str): Name of the service to find

        Returns:
            dict: Connection details if found, None otherwise
        """
        response = self.list_all_connections()
        for connection in response.get("connections", []):
            if connection["service"] == service_name:
                return connection
        return None

    def create_an_ecommerce_customer(self, data):
        """
        Create a new e-commerce customer resource


        Args:
            data:

        Returns:

        """
        return self.client._post("/ecomCustomers", json=data)

    def retrieve_an_ecommerce_customer(self, customer_id):
        """
        Retrieve an existing e-commerce customer resource


        Args:
            customer_id:

        Returns:

        """
        return self.client._get("/ecomCustomers/{}".format(customer_id))

    def update_an_ecommerce_customer(self, customer_id, data):
        """
        Retrieve an existing e-commerce customer resource


        Args:
            customer_id:
            data:

        Returns:

        """
        return self.client._put("/ecomCustomers/{}".format(customer_id), json=data)

    def delete_an_ecommerce_customer(self, customer_id):
        """
        Delete an existing e-commerce customer resource


        Args:
            customer_id:

        Returns:

        """
        return self.client._delete("/ecomCustomers/{}".format(customer_id))

    def list_all_ecommerce_customer(self):
        raise NotImplementedError

    def create_an_ecommerce_order(self, data):
        """
        Create a new e-commerce order resource


        Args:
            data:

        Returns:

        """
        return self.client._post("/ecomOrders", json=data)

    def retrieve_an_ecommerce_order(self, order_id):
        """
        Retrieve an existing new e-commerce order resource


        Args:
            order_id:

        Returns:

        """
        return self.client._get("/ecomOrders/{}".format(order_id))

    def delete_an_ecommerce_order(self, order_id):
        """
        Delete an existing e-commerce order resource


        Args:
            order_id:

        Returns:

        """
        return self.client._delete("/ecomOrders/{}".format(order_id))

    def list_all_ecommerce_orders(self, filters=None, orders=None):
        """List all existing e-commerce order resources.

        Args:
            filters (dict, optional): Filter parameters. Available filters:
                - connectionid (int): Filter by connection ID
                - externalid (int): Filter by external ID
                - externalcheckoutid (str): Filter by external checkout ID
                - email (str): Filter by customer email
                - state (int): Filter by order state (0=Pending, 1=Completed, 2=Abandoned, 3=Recovered, 4=Waiting)
                - customerid (str): Filter by customer ID
                - external_created_date (str): Filter by external created date
            orders (dict, optional): Order parameters. Same keys as filters, values should be 'ASC' or 'DESC'

        Returns:
            dict: Response containing list of ecommerce orders and metadata
        """
        params = {}

        # Add filters if provided
        if filters:
            for key, value in filters.items():
                params[f"filters[{key}]"] = value

        # Add ordering if provided
        if orders:
            for key, value in orders.items():
                if value.upper() in ["ASC", "DESC"]:
                    params[f"orders[{key}]"] = value.upper()

        # Get first page
        response = self.client._get("/ecomOrders", params=params)
        if not response or "ecomOrders" not in response:
            return response

        all_orders = response["ecomOrders"]
        total = int(response.get("meta", {}).get("total", len(all_orders)))

        # If we have more orders than returned in first page, fetch remaining pages
        while len(all_orders) < total:
            # Add offset parameter for next page
            params["offset"] = len(all_orders)
            next_page = self.client._get("/ecomOrders", params=params)

            if not next_page or "ecomOrders" not in next_page:
                break

            all_orders.extend(next_page["ecomOrders"])

        # Return combined response
        return {"ecomOrders": all_orders, "meta": {"total": str(total)}}

    def update_an_ecommerce_order(self, order_id, data):
        """
        Update an existing ecommerce order/cart resource.


        Args:
            order_id:
            data:

        Returns:

        """
        return self.client._put("/ecomOrders/{}".format(order_id), json=data)

    def list_ecommerce_order_products(self):
        """List all ecommerce order products.

        Returns:
            dict: Response containing list of ecommerce order products
        """
        return self.client._get("/ecomOrderProducts")

    def list_ecommerce_order_products_for_a_specific_ecommerce_order(self, order_id):
        """List ecommerce order products for a specific order.

        Args:
            order_id (str): The ID of the ecommerce order

        Returns:
            dict: Response containing list of ecommerce order products for the specified order
        """
        return self.client._get(f"/ecomOrders/{order_id}/orderProducts")

    def retrieve_an_ecommerce_order_product(self, product_id):
        """Retrieve a specific ecommerce order product.

        Args:
            product_id (str): The ID of the ecommerce order product

        Returns:
            dict: Response containing the ecommerce order product details
        """
        return self.client._get(f"/ecomOrderProducts/{product_id}")
