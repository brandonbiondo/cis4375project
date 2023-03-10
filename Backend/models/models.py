from sqlalchemy import Column, Integer, String, ForeignKey, Date, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData
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
    product_price = Column(Integer)

    vendor = relationship("Vendor", back_populates="products")
    categories = relationship("Category", back_populates="product")
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
    def password(self):
        return self.login_password
    
    def set_password(self, password):
        hashed_password = bcrypt.hash(password.encode('utf-8'))
        self.login_password = hashed_password.decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.login_password.encode('utf-8'))

class Inventory(Base):
    __tablename__ = 'inventory'
    inventory_id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.product_id'))
    store_id = Column(Integer, ForeignKey('store.store_id'))
    item_name = Column(String(50))
    item_quantity = Column(Integer)
    inventory_value = Column(Numeric(8,2))

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