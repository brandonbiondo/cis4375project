from sqlalchemy import Column, Integer, String, ForeignKey, Date, Numeric, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from passlib.hash import bcrypt
from dotenv import load_dotenv


load_dotenv()

Base = declarative_base()
metadata = MetaData()

# Creating tables and relationships for database
class Vendor(Base):
    __tablename__ = 'vendor'
    vendor_id = Column(Integer, primary_key=True)
    vendor_name = Column(String(50))
    vendor_phone = Column(String(20))

    products = relationship("Product", back_populates="vendor")

class Product(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True, autoincrement=True)
    vendor_id = Column(Integer, ForeignKey('vendor.vendor_id'))
    product_name = Column(String(50))
    product_description = Column(String(50))
    product_price = Column(Numeric(precision=10, scale=2, asdecimal=True))

    vendor = relationship("Vendor", back_populates="products")
    category = relationship("Category", back_populates="product")
    inventory = relationship("Inventory", back_populates="product")
    reorder = relationship("Reorder", back_populates="product")


class Category(Base):
    __tablename__ = 'category'
    category_id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.product_id'))
    category_name = Column(String(50))

    product = relationship("Product", back_populates="category")

class Store(Base):
    __tablename__ = 'store'
    store_id = Column(Integer, primary_key=True, autoincrement=True)
    store_name = Column(String(30))
    store_address = Column(String(30))
    store_city = Column(String(30))
    store_state = Column(String(15))
    store_phone = Column(String(25))
    store_email = Column(String(30))

    inventory = relationship("Inventory", back_populates="store")

class Employee(Base):
    __tablename__ = 'employees'
    employee_id = Column(Integer, primary_key=True, autoincrement=True)
    employee_firstName = Column(String(30))
    employee_lastName = Column(String(30))
    employee_address = Column(String(30))
    employee_phone = Column(String(25))
    employee_role = Column(String(20))
    employee_startDate = Column(Date)
    employee_endDate = Column(Date)

    login = relationship("Login", back_populates="employee")

class Login(Base):
    __tablename__ = 'login'
    login_id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey('employees.employee_id'))
    login_username = Column(String(30))
    login_password = Column(String(60))

    employee = relationship("Employee", back_populates="login")

    # Password encrpytion
    def __init__(self, employee_id, login_username, login_password):
        self.employee_id = employee_id
        self.login_username = login_username
        # Encrypting and storing password in login_password
        self.login_password = bcrypt.hash(login_password)
        
    # Comparing plaintext and encrypted password using bcrypt.verify    
    def check_password(self, login_password):
        password_matched = bcrypt.verify(login_password, self.login_password)
        # If password verified
        if password_matched:
            print('Password was hashed')
        else:
        # If password not verified
            print('Password was not hashed')
        return password_matched

class Inventory(Base):
    __tablename__ = 'inventory'
    inventory_id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.product_id'))
    store_id = Column(Integer, ForeignKey('store.store_id'))
    item_name = Column(String(50))
    item_quantity = Column(Integer)
    inventory_value = Column(Numeric(precision=10, scale=2, asdecimal=True))

    product = relationship("Product", back_populates="inventory")
    store = relationship("Store", back_populates="inventory")
    reorder = relationship("Reorder", back_populates="inventory")

class Reorder(Base):
    __tablename__ = 'reorder'
    reorder_id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.product_id'))
    inventory_id = Column(Integer, ForeignKey('inventory.inventory_id'))
    reorder_level = Column(Integer)
    reorder_time_in_days = Column(Integer)
    quantity_in_reorder = Column(Integer)
    
    product = relationship("Product", back_populates="reorder")
    inventory = relationship("Inventory", back_populates="reorder")

class Quote(Base):
    __tablename__ = 'quote'
    quote_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    phone = Column(String(25))
    email = Column(String(30))
    message = Column(String(250))

class AuditLog(Base):
    __tablename__ = 'auditlog'
    audit_log_id = Column(Integer, primary_key=True, autoincrement=True)
    item_name = Column(String(50))
    date = Column(Date)
    crud_operation = Column(String(10))
    table = Column(String(25))
    user = Column(String(30))