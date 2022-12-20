import xmlrpc.client
from xmlrpc import client

url_db1 = "http://cybrosys:8015"
db_1 = 'odoo15_1'
username_db_1 = 'admin'
password_db_1 = 'admin'
common_1 = client.ServerProxy('{}/xmlrpc/2/common'.format(url_db1))
models_1 = client.ServerProxy('{}/xmlrpc/2/object'.format(url_db1))
version_db1 = common_1.version()

url_db2 = "http://cybrosys:8069"
db_2 = 'odoo16_3'
username_db_2 = 'admin'
password_db_2 = 'admin'
common_2 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url_db2))
models_2 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url_db2))
version_db2 = common_2.version()

uid_db1 = common_1.authenticate(db_1, username_db_1, password_db_1, {})
uid_db2 = common_2.authenticate(db_2, username_db_2, password_db_2, {})

db_1_product = models_1.execute_kw(db_1, uid_db1, password_db_1, 'product.template', 'search_read', [[]],
                                   {'fields': ['name', 'detailed_type', 'list_price']})
db_2_product = models_2.execute_kw(db_2, uid_db2, password_db_2, 'product.template', 'search_read', [[]],
                                   {'fields': ['name', 'detailed_type', 'list_price']})

w = 0
list_16 = []
list_16.clear()
for j in db_2_product:
    name_16 = db_2_product[w]['name']
    type_16 = db_2_product[w]['detailed_type']
    price_16 = db_2_product[w]['list_price']
    w += 1
    list_16.append([name_16, type_16, price_16])

x = 0
final_product = []
final_product.clear()
for k in db_1_product:
    name_15 = db_1_product[x]['name']
    type_15 = db_1_product[x]['detailed_type']
    price_15 = db_1_product[x]['list_price']
    x += 1
    temp_list = [name_15, type_15, price_15]
    if temp_list not in list_16:
        final_product.append(k)
print(final_product)

# print(db_1_product)
# print(db_2_product)


new_lead = models_2.execute_kw(db_2, uid_db2, password_db_2, 'product.template', 'create', [final_product])

# print(new_lead)
