## Synopsis

```
from cinnamon_sdk import Cinnamon, VendorInput, FilterInput, FilterOperator

cinna = Cinnamon(url="https://api.adgo.io/v1/graphql")
cinna.login(email="my@email.com", password="password")

my_marketplace = cinna.marketplace(id=1)
print(my_marketplace.name)

new_vendor = self.cinnamon.create_vendor(
    input=VendorInput(name="My Vendor", marketplace_id=my_marketplace.id)
)

# Complex query
vendors_query = self.cinnamon.vendors_each(
    filter=FilterInput(
        field="id", operator=FilterOperator.IN, value=[1, 2, 3]
    ),
    fields=[
        VendorConnectionFields.edges.node.id,
        VendorConnectionFields.edges.node.id.name,
        VendorConnectionFields.edges.node.products.edges.node.name
    ],
)
# When iterating using `_each` methods, all pages from the API are automatically fetched.
for vendor in vendors_query:
    print(vendor.name)
    # There are two ways to iterate over connections.  The first is according to the schema:
    for edge in vendor.products.edges:
        print(edge.node.name)
    # The second is a shortcut iterator:
    for product in vendor.products:
        print(product.name)
```

## Updating The SDK

```
export CINNAMON_PYTHON_SDK_URL=https://api.adgo.io/v1/graphql
export CINNAMON_PYTHON_SDK_EMAIL=my@email.com
export CINNAMON_PYTHON_SDK_PASSWORD=password
python ./generate.py
```
