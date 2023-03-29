from flask import jsonify, Blueprint, request, abort
from dotenv import load_dotenv
from sqlalchemy import text
from utilities.dbConnection import connect_to_db
from models.models import *


load_dotenv()

bp = Blueprint('api', __name__)

#
#
#
# vendors CRUD operations
#
#
#

@bp.route('/vendor', methods=['GET'])
def get_vendor():
    engine, session = connect_to_db()
    vendors = session.query(Vendor).all()
    if vendors:
        vendor_list = [
            {
                'vendor_id': vendor.vendor_id,
                'vendor_name': vendor.vendor_name,
                'vendor_phone': vendor.vendor_phone
            } 
            for vendor in vendors
        ]
        return jsonify(vendor_list)
    else:
        return jsonify({'error': 'Vendor not found'}), 404


# endpoint to add vendor as POST
@bp.route('/vendor', methods=['POST'])  # set endpoint information for API
def add_vendor():
    engine, session = connect_to_db()
    vendor_name = request.json['vendor_name']
    vendor_phone = request.json['vendor_phone']
    add_vendor_sql = f"INSERT INTO vendor (vendor_name, vendor_phone) VALUES ('{vendor_name}', '{vendor_phone}')"
    session.execute(text(add_vendor_sql)) # execute the sql code from above and commit the changes using the next line 
    session.commit()
    return 'Add request was successful'  # reciept
    # This endpoint will allow the user to POST a new record into the vendors table of the sql database.

# update the vendors with PUT
@bp.route('/vendor', methods=['PUT'])  # set endpoint information for API
def update_vendor():
    if 'vendor_id' in request.args: 
        vendor_id = (request.args['vendor_id'])  # get specific name for the desired vendor to update
    else:
        return 'ERROR: No name provided!'  # error code 
    engine, session = connect_to_db()
    vendor_name = request.json['vendor_name']
    vendor_phone = request.json['vendor_phone']
    update_vendor_sql= f"UPDATE vendor SET vendor_name = '{vendor_name}', vendor_phone = '{vendor_phone}' WHERE vendor_id = '{vendor_id}'"  
    session.execute(text(update_vendor_sql))  
    session.commit()
    return 'Update request was successful'  #receipt

# endpoint to delete a vendor using DELETE
@bp.route('/vendor', methods=['DELETE'])  # set enpoint information for API
def delete_vendor():
    if 'vendor_id' in request.args: 
        vendor_id = (request.args['vendor_id'])  # get specific id for the desired vendor to delete
    else:
        return 'ERROR: No ID provided!'  # error code 
    engine, session = connect_to_db()
    delete_vendor_sql = f"DELETE FROM vendor WHERE vendor_id = '{vendor_id}'"  # sql code to delete a vendor using the id
    session.execute(text(delete_vendor_sql))
    session.commit()
    return 'Delete request was successful'  # receipt

#
#
#
# products CRUD operations
#
#
#

@bp.route('/products', methods=['GET']) 
def get_products():
    engine, session = connect_to_db()
    products = session.query(Product).all()
    if products:
        product_list = [
            {
                'product_id': product.product_id,
                'product_name': product.product_name,
                'product_description': product.product_description,
                'product_price': product.product_price,
                'vendor_id': product.vendor_id
            } 
            for product in products
        ]
        return jsonify(product_list)
    else:
        return jsonify({'error': 'Products not found'}), 404

# endpoint to add products as POST
@bp.route('/products', methods=['POST'])  # set endpoint information for API
def add_products():
    engine, session = connect_to_db()
    product_name = request.json['product_name']
    product_description = request.json['product_description']
    product_price = request.json['product_price']
    vendor_id = request.json['vendor_id']
    add_products_sql = f"INSERT INTO products (product_name, product_description, product_price, vendor_id) VALUES ('{product_name}', '{product_description}', {product_price}, {vendor_id})"
    result = session.execute(text(add_products_sql)) # execute the sql code from above and commit the changes using the next line 
    session.commit()
    inserted_product = request.json
    inserted_product["product_id"] = result.lastrowid
    return inserted_product # reciept
    # This endpoint will allow the user to POST a new record into the products table of the sql database.

# update the products with PUT
@bp.route('/products', methods=['PUT'])  # set endpoint information for API
def update_products():
    if 'product_id' in request.args: 
        product_id = (request.args['product_id'])  # get specific id for the desired product to update
    else:
        return 'ERROR: No ID provided!'  # error code 
    engine, session = connect_to_db()
    product_name = request.json['product_name']
    product_description = request.json['product_description']
    product_price = request.json['product_price']
    vendor_id = request.json['vendor_id']
    update_products_sql=f"UPDATE products SET product_name = '{product_name}', product_description = '{product_description}', product_price = {product_price}, vendor_id = {vendor_id} WHERE product_id = '{product_id}'"  
    session.execute(text(update_products_sql))  
    session.commit()
    return 'Update request was successful'  #receipt

# endpoint to delete a product using DELETE
@bp.route('/products', methods=['DELETE'])  # set enpoint information for API
def delete_products():
    if 'product_id' in request.args: 
        product_id = (request.args['product_id'])  # get specific id for the desired product to delete
    else:
        return 'ERROR: No ID provided!'  # error code 
    engine, session = connect_to_db()
    delete_products_sql = f"DELETE FROM products WHERE product_id = '{product_id}'"  # sql code to delete a product using the name
    session.execute(text(delete_products_sql))
    session.commit()
    return 'Delete request was successful'  # receipt

#
#
#
# Employees CRUD Operations
#
#
#

#endpoint to get all employees using GET
@bp.route('/employees', methods=['GET']) 
def get_employees():
    engine, session = connect_to_db()
    employees = session.query(Employee).all()
    if employees:
        employee_list = [
            {
                'employee_id': employee.employee_id,
                'employee_firstname': employee.employee_firstName,
                'employee_lastname': employee.employee_lastName,
                'employee_address': employee.employee_address,
                'employee_phone': employee.employee_phone,
                'employee_role': employee.employee_role,
                'employee_startdate': employee.employee_startDate,
                'employee_enddate': employee.employee_endDate
            } 
            for employee in employees
        ]
        return jsonify(employee_list)
    else:
        return jsonify({'error': 'Employees not found'}), 404

# endpoint to add employees as POST
@bp.route('/employees', methods=['POST'])  # set endpoint information for API
def add_employees():
    engine, session = connect_to_db()
    employee_firstname = request.json['employee_firstname']
    employee_lastname = request.json['employee_lastname']
    employee_address = request.json['employee_address']
    employee_phone = request.json['employee_phone']
    employee_role = request.json['employee_role']
    employee_startdate = request.json['employee_startdate']
    employee_enddate = request.json['employee_enddate']
    add_employees_sql = f"INSERT INTO employees (employee_firstname, employee_lastname, employee_address, employee_phone, employee_role, employee_startdate, employee_enddate) VALUES ('{employee_firstname}', '{employee_lastname}', '{employee_address}', '{employee_phone}', '{employee_role}', '{employee_startdate}', '{employee_enddate}')"
    session.execute(text(add_employees_sql)) # execute the sql code from above and commit the changes using the next line 
    session.commit()
    return 'Add request was successful'  # reciept
    # This endpoint will allow the user to POST a new employee into the employees table of the sql database.

# update the employees with PUT
@bp.route('/employees', methods=['PUT'])  # set endpoint information for API
def update_employees():
    if 'employee_id' in request.args: 
        employee_id = request.args['employee_id']  # get specific id for desired employee to update
    else:
        return 'ERROR: No ID provided!'  # error message
    engine, session = connect_to_db()
    employee_firstname = request.json['employee_firstname']
    employee_lastname = request.json['employee_lastname']
    employee_address = request.json['employee_address']
    employee_phone = request.json['employee_phone']
    employee_role = request.json['employee_role']
    employee_startdate = request.json['employee_startdate']
    employee_enddate = request.json['employee_enddate']
    update_employees_sql=f"UPDATE employees SET employee_firstname = '{employee_firstname}', employee_lastname = '{employee_lastname}', employee_address = '{employee_address}', employee_phone = '{employee_phone}', employee_role = '{employee_role}', employee_startdate = '{employee_startdate}', employee_enddate = '{employee_enddate}' WHERE employee_id = '{employee_id}'"  
    session.execute(text(update_employees_sql))  
    session.commit()
    return 'Update request was successful'  #receipt

# endpoint to delete a employee using DELETE
@bp.route('/employees', methods=['DELETE'])  # set enpoint information for API
def delete_employees():
    if 'employee_id' in request.args: 
        employee_id = request.args['employee_id']  # get specific id for desired employee to delete
    else:
        return 'ERROR: No ID provided!'  # error message
    engine, session = connect_to_db()
    delete_employee_sql = f"DELETE FROM employees WHERE employee_id = '{employee_id}'"  # sql code to delete a employee using their ID
    session.execute(text(delete_employee_sql))
    session.commit()
    return 'Delete request was successful'  # receipt

#
#
#
# Login CRUD Operations
#
#
#

#endpoint to retrieve user login information using GET
@bp.route('/login', methods=['GET'])
def get_login():
    engine, session = connect_to_db()
    logins = session.query(Login).all()
    if logins:
        login_list = [
            {
                'employee_id': login.employee_id,
                'login_id': login.login_id,
                'login_username': login.login_username
            }
            for login in logins
        ]
        return jsonify(login_list)
    else:
        return jsonify({'error': 'Login(s) not found'}), 404
    
# endpoint to add login as POST
@bp.route('/login', methods=['POST'])
def add_login():
    # connect to the DB
    engine, session = connect_to_db()
    # login information from request
    data = request.get_json()
    employee_id = data.get('employee_id')
    username = data.get('login_username')
    password = data.get('login_password')

    # query database for employee with given ID
    employee = session.query(Employee).get(employee_id)

    # if employee is not found, return a 404 error
    if not employee:
        abort(404)
    
    # creates a new login object
    new_login = Login(employee_id=employee_id, login_username=username, login_password=password)

    session.add(new_login)
    session.commit()

    # returns JSON response with new login information and 201 code
    return jsonify({
        'login_id': new_login.login_id,
        'employee_id': new_login.employee_id,
        'login_username': new_login.login_username
    }), 201
#
#
#
# Store CRUD Operations
#
#
#

#endpoint to get store information using GET
@bp.route('/store', methods=['GET']) 
def get_store():
    engine, session = connect_to_db()
    stores = session.query(Store).all()
    if stores:
        store_list = [
            {
                'store_id': store.store_id,
                'store_name': store.store_name,
                'store_address': store.store_address,
                'store_city': store.store_city,
                'store_state': store.store_state,
                'store_phone': store.store_phone,
                'store_email': store.store_email
            } 
            for store in stores
        ]
        return jsonify(store_list)
    else:
        return jsonify({'error': 'Store(s) not found'}), 404

# endpoint to add store as POST
@bp.route('/store', methods=['POST'])  # set endpoint information for API
def add_store():
    engine, session = connect_to_db()
    store_name = request.json['store_name']
    store_address = request.json['store_address']
    store_city = request.json['store_city']
    store_state = request.json['store_state']
    store_phone = request.json['store_phone']
    store_email = request.json['store_email']
    add_store_sql = f"INSERT INTO store (store_name, store_address, store_city, store_state, store_phone, store_email) VALUES ('{store_name}', '{store_address}', '{store_city}', '{store_state}', '{store_phone}', '{store_email}')"
    session.execute(text(add_store_sql)) # execute the sql code from above and commit the changes using the next line 
    session.commit()
    return 'Add request was successful'  # reciept
    # This endpoint will allow the user to POST a new store into the store table of the sql database.

# update the store with PUT
@bp.route('/store', methods=['PUT'])  # set endpoint information for API
def update_store():
    if 'store_id' in request.args: 
        store_id = request.args['store_id']  # get specific id for desired store to update
    else:
        return 'ERROR: No ID provided!'  # error message
    engine, session = connect_to_db()
    store_name = request.json['store_name']
    store_address = request.json['store_address']
    store_city = request.json['store_city']
    store_state = request.json['store_state']
    store_phone = request.json['store_phone']
    store_email = request.json['store_email']
    update_store_sql=f"UPDATE store SET store_name = '{store_name}', store_address = '{store_address}', store_city = '{store_city}', store_state = '{store_state}', store_phone = '{store_phone}', store_email = '{store_email}' WHERE store_id = '{store_id}'"  
    session.execute(text(update_store_sql))  
    session.commit()
    return 'Update request was successful'  #receipt

# endpoint to delete a store using DELETE
@bp.route('/store', methods=['DELETE'])  # set enpoint information for API
def delete_store():
    if 'store_id' in request.args: 
        store_id = request.args['store_id']  # get specific id for desired store to delete
    else:
        return 'ERROR: No ID provided!'  # error message
    engine, session = connect_to_db()
    delete_store_sql = f"DELETE FROM store WHERE store_id = '{store_id}'"  # sql code to delete a store using their ID
    session.execute(text(delete_store_sql))
    session.commit()
    return 'Delete request was successful'  # receipt

#
#
#
# Inventory CRUD Operations
#
#
#

# endpoint to get inventory information using GET
@bp.route('/inventory', methods=['GET']) 
def get_inventory():
    engine, session = connect_to_db()
    inventorys = session.query(Inventory).all()
    if inventorys:
        inventorys_list = [
            {
                'inventory_id': inventory.inventory_id,
                'item_name': inventory.item_name,
                'item_quantity': inventory.item_quantity,
                'inventory_value': inventory.inventory_value,
                'product_id': inventory.product_id,
                'store_id': inventory.store_id
            } 
            for inventory in inventorys
        ]
        return jsonify(inventorys_list)
    else:
        return jsonify({'error': 'Inventory not found'}), 404

# endpoint to add inventory as POST
@bp.route('/inventory', methods=['POST'])  # set endpoint information for API
def add_inventory():
    engine, session = connect_to_db()
    item_name = request.json['item_name']
    item_quantity = request.json['item_quantity']
    inventory_value = request.json['inventory_value']
    product_id = request.json['product_id']
    store_id = request.json['store_id']
    add_invenotry_sql = f"INSERT INTO inventory (item_name, item_quantity, inventory_value, product_id, store_id) VALUES ('{item_name}', '{item_quantity}', '{inventory_value}', '{product_id}', '{store_id}')"
    result = session.execute(text(add_invenotry_sql)) # execute the sql code from above and commit the changes using the next line 
    session.commit()
    inserted_inventory = request.json
    inserted_inventory["inventory_id"] = result.lastrowid
    return inserted_inventory # reciept
 
    return 'Add request was successful'  # reciept
    # This endpoint will allow the user to POST new inventory into the invenotry table of the sql database.

# update the inventory with PUT
@bp.route('/inventory', methods=['PUT'])  # set endpoint information for API
def update_inventory():
    if 'inventory_id' in request.args: 
        inventory_id = request.args['inventory_id']  # get specific id for desired inventory item to update
    else:
        return 'ERROR: No ID provided!'  # error message
    engine, session = connect_to_db()
    item_name = request.json['item_name']
    item_quantity = request.json['item_quantity']
    inventory_value = request.json['inventory_value']
    product_id = request.json['product_id']
    store_id = request.json['store_id']
    update_inventory_sql=f"UPDATE inventory SET item_name = '{item_name}', item_quantity = '{item_quantity}', inventory_value = '{inventory_value}', product_id = '{product_id}', store_id = '{store_id}' WHERE inventory_id = '{inventory_id}'"  
    session.execute(text(update_inventory_sql))  
    session.commit()
    return 'Update request was successful'  #receipt

# endpoint to delete inventory items using DELETE
@bp.route('/inventory', methods=['DELETE'])  # set enpoint information for API
def delete_inventory():
    if 'inventory_id' in request.args: 
        inventory_id = request.args['inventory_id']  # get specific id for desired inventory item to delete
    else:
        return 'ERROR: No ID provided!'  # error message
    engine, session = connect_to_db()
    delete_inventory_sql = f"DELETE FROM inventory WHERE inventory_id = '{inventory_id}'"  # sql code to delete an inventory item using its ID
    session.execute(text(delete_inventory_sql))
    session.commit()
    return 'Delete request was successful'  # receipt

#
#
#
# Reorder CRUD Operations
#
#
#

# endpoint to get reorder information using GET
@bp.route('/reorder', methods=['GET']) 
def get_reorder():
    engine, session = connect_to_db()
    reorders = session.query(Reorder).all()
    if reorders:
        reorders_list = [
            {
                'reorder_id': reorder.reorder_id,
                'reorder_level': reorder.reorder_level,
                'reorder_time_in_days': reorder.reorder_time_in_days,
                'quantity_in_reorder': reorder.quantity_in_reorder,
                'product_id': reorder.product_id,
                'inventory_id': reorder.inventory_id
            } 
            for reorder in reorders
        ]
        return jsonify(reorders_list)
    else:
        return jsonify({'error': 'Reorders not found'}), 404

# endpoint to add reorder info as POST
@bp.route('/reorder', methods=['POST'])  # set endpoint information for API
def add_reorder():
    engine, session = connect_to_db()
    reorder_level = request.json['reorder_level']
    reorder_time_in_days = request.json['reorder_time_in_days']
    quantity_in_reorder = request.json['quantity_in_reorder']
    product_id = request.json['product_id']
    inventory_id = request.json['inventory_id']
    add_reorder_sql = f"INSERT INTO reorder (reorder_level, reorder_time_in_days, quantity_in_reorder, product_id, inventory_id) VALUES ('{reorder_level}', '{reorder_time_in_days}', '{quantity_in_reorder}', '{product_id}', '{inventory_id}')"
    result = session.execute(text(add_reorder_sql)) # execute the sql code from above and commit the changes using the next line 
    session.commit()
    new_reorder = request.json
    new_reorder["reorder_id"] = result.lastrowid
    return new_reorder # reciept
    # This endpoint will allow the user to POST new reorder info into the reorder table of the sql database.

# update the reorder info with PUT
@bp.route('/reorder', methods=['PUT'])  # set endpoint information for API
def update_reorder():
    if 'reorder_id' in request.args: 
        reorder_id = request.args['reorder_id']  # get specific id for desired reorder item to update
    else:
        return 'ERROR: No ID provided!'  # error message
    engine, session = connect_to_db()
    reorder_level = request.json['reorder_level']
    reorder_time_in_days = request.json['reorder_time_in_days']
    quantity_in_reorder = request.json['quantity_in_reorder']
    product_id = request.json['product_id']
    inventory_id = request.json['inventory_id']
    update_reorder_sql=f"UPDATE reorder SET reorder_level = '{reorder_level}', reorder_time_in_days = '{reorder_time_in_days}', quantity_in_reorder = '{quantity_in_reorder}', product_id = '{product_id}', inventory_id = '{inventory_id}' WHERE reorder_id = '{reorder_id}'"  
    session.execute(text(update_reorder_sql))  
    session.commit()
    return 'Update request was successful'  #receipt

# endpoint to delete reorder items using DELETE
@bp.route('/reorder', methods=['DELETE'])  # set enpoint information for API
def delete_reorder():
    if 'reorder_id' in request.args: 
        reorder_id = request.args['reorder_id']  # get specific id for desired reorder item to delete
    else:
        return 'ERROR: No ID provided!'  # error message
    engine, session = connect_to_db()
    delete_reorder_sql = f"DELETE FROM reorder WHERE reorder_id = '{reorder_id}'"  # sql code to delete a reorder item using its ID
    session.execute(text(delete_reorder_sql))
    session.commit()
    return 'Delete request was successful'  # receipt


#
#
#
# Category CRUD Operations
#
#
#

# endpoint to get category information using GET
@bp.route('/category', methods=['GET']) 
def get_category():
    engine, session = connect_to_db()
    categorys = session.query(Category).all()
    if categorys:
        categorys_list = [
            {
                'category_id': reorder.category_id,
                'category_name': reorder.category_name,
                'product_id': reorder.product_id
            } 
            for reorder in categorys
        ]
        return jsonify(categorys_list)
    else:
        return jsonify({'error': 'Category(s) not found'}), 404

# endpoint to add category info as POST
@bp.route('/category', methods=['POST'])  # set endpoint information for API
def add_category():
    engine, session = connect_to_db()
    category_name = request.json['category_name']
    product_id = request.json['product_id']
    add_category_sql = f"INSERT INTO category (category_name, product_id) VALUES ('{category_name}', '{product_id}')"
    result = session.execute(text(add_category_sql)) # execute the sql code from above and commit the changes using the next line G
    session.commit()
    new_category = request.json
    new_category["category_id"] = result.lastrowid
    
    return new_category  # reciept
    # This endpoint will allow the user to POST a new category into the category table of the sql database.

# update the category info with PUT
@bp.route('/category', methods=['PUT'])  # set endpoint information for API
def update_category():
    if 'category_id' in request.args: 
        category_id = request.args['category_id']  # get specific id for desired category to update
    else:
        return 'ERROR: No ID provided!'  # error message
    engine, session = connect_to_db()
    category_name = request.json['category_name']
    product_id = request.json['product_id']
    update_category_sql=f"UPDATE category SET category_name = '{category_name}', product_id = '{product_id}' WHERE category_id = '{category_id}'"  
    session.execute(text(update_category_sql))  
    session.commit()
    return 'Update request was successful'  #receipt

# endpoint to delete reorder items using DELETE
@bp.route('/category', methods=['DELETE'])  # set enpoint information for API
def delete_category():
    if 'category_id' in request.args: 
        category_id = request.args['category_id']  # get specific id for desired category to delete
    else:
        return 'ERROR: No ID provided!'  # error message
    engine, session = connect_to_db()
    print(category_id)
    delete_category_sql = f"DELETE FROM category WHERE category_id = '{category_id}'"  # sql code to delete a category using its ID
    print(delete_category_sql)
    session.execute(text(delete_category_sql))
    session.commit()
    return 'Delete request was successful'  # receipt


#get products combined with inventory, vendor, category, and store
@bp.route('/combined_products', methods=["GET"])
def get_combined_products():
    engine, session = connect_to_db()
    combined_products = session.execute(text(("SELECT * FROM products p INNER JOIN inventory i ON p.product_id = i.product_id INNER JOIN vendor v ON v.vendor_id = p.vendor_id INNER JOIN category c ON c.product_id = p.product_id INNER JOIN store s ON s.store_id = i.store_id INNER JOIN reorder r ON r.product_id = p.product_id ORDER BY p.product_id"))).all()
    combined_products_list = [dict(c._mapping) for c in combined_products]
            
    return jsonify(combined_products_list)
# all endpoints are working and have been tested with postman
