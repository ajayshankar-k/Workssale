from unittest.mock import DEFAULT
from django.db import models

# Create your models here.
class contact_table(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    contact_no=models.CharField(max_length=20)
    message=models.TextField()
    def __str__(self):
        return self.name
#user
class reg_table(models.Model):
    name=models.CharField(max_length=30)
    contact_no=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class adduser_table(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    role_type=models.CharField(max_length=100)
    status_type=models.CharField(max_length=100)
    logger_id=models.CharField(max_length=200)
    def __str__(self):
        return self.name
class add_customer_table(models.Model):
    customer_name=models.CharField(max_length=100)
    customer_email=models.EmailField()
    customer_phone=models.CharField(max_length=100)
    customer_city=models.CharField(max_length=100)
    logger_id=models.CharField(max_length=200)
    def __str__(self):
        return self.customer_name
class add_vendor_table(models.Model):
    vendor_name=models.CharField(max_length=100)
    vendor_email=models.EmailField()
    vendor_phone=models.CharField(max_length=100)
    vendor_city=models.CharField(max_length=100)
    logger_id=models.CharField(max_length=200)
    def __str__(self):
        return self.vendor_name
class add_productlist_table(models.Model):
    product_name=models.CharField(max_length=100)
    product_brand=models.CharField(max_length=100)
    product_unit=models.CharField(max_length=100)
    product_selling_price=models.CharField(max_length=100)
    logger_id=models.CharField(max_length=200)
    def __str__(self):
        return self.product_name     
class addcategory_table(models.Model):
    category_name=models.CharField(max_length=100)
    logger_id=models.CharField(max_length=200)
    def __str__(self):
        return self.category_name
class addbrand_table(models.Model):
    brand_name=models.CharField(max_length=100)
    logger_id=models.CharField(max_length=200)
    def __str__(self):
        return self.brand_name
class addtax_table(models.Model):
    tax_name=models.CharField(max_length=100)
    tax_percentage=models.CharField(max_length=100)
    tax_dafault=models.CharField(max_length=100)
    logger_id=models.CharField(max_length=200)
    def __str__(self):
        return self.tax_name    

class add_role_table(models.Model):
    role_type=models.CharField(max_length=100)
    profile=models.CharField(max_length=100)
    notification=models.CharField(max_length=100)
    account=models.CharField(max_length=100)
    logger_id=models.CharField(max_length=100)

    def __str__(self):
        return self.role_type

class add_sale_table(models.Model):
    invoice_id=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    sold_by=models.CharField(max_length=100)
    sold_to=models.CharField(max_length=100)
    items_sold=models.CharField(max_length=100)
    payment=models.CharField(max_length=100)
    logger_id=models.CharField(max_length=100)

    def __str__ (self):
        return self.sold_by

class add_return_table(models.Model):
    c_name=models.CharField(max_length=100)
    c_email=models.EmailField()
    returned_dt=models.CharField(max_length=100)
    returned_item=models.CharField(max_length=100)
    logger_id=models.CharField(max_length=100)

    def __str__ (self):
        return self.c_email 

class add_stock_table(models.Model):
    p_name=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)
    logger_id=models.CharField(max_length=100)

    def __str__ (self):
        return self.p_name

class add_purchase_tax_table(models.Model):
    ref_number=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    vendor=models.CharField(max_length=100)
    p_tax=models.CharField(max_length=100)
    g_tot=models.CharField(max_length=100)
    logger_id=models.CharField(max_length=100)

    def __str__ (self):
        return self.ref_number 

class add_expense_report_table(models.Model):
    date=models.CharField(max_length=100)
    exp_category=models.CharField(max_length=100)
    note=models.CharField(max_length=100)
    created_by=models.CharField(max_length=100)
    logger_id=models.CharField(max_length=100)

    def __str__ (self):
        return self.created_by  

class add_customer_report_table(models.Model):
    name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=100)
    email=models.EmailField()
    tot_sales=models.CharField(max_length=100)
    tot_amt=models.CharField(max_length=100)
    logger_id=models.CharField(max_length=100)

    def __str__ (self):
        return self.email 

class add_quotation_table(models.Model):
    date=models.CharField(max_length=100)
    ref_number=models.CharField(max_length=100)
    customer=models.EmailField()
    customer_email=models.CharField(max_length=100)
    g_total=models.CharField(max_length=100)
    quo_note=models.CharField(max_length=200)
    logger_id=models.CharField(max_length=100)

    def __str__ (self):
        return self.customer_email    

class add_expense_list_table(models.Model):
    branch=models.CharField(max_length=100)
    exp_date=models.CharField(max_length=100)
    exp_category=models.EmailField()
    amount=models.CharField(max_length=100)
    note=models.CharField(max_length=100)
    logger_id=models.CharField(max_length=100)

    def __str__ (self):
        return self.branch            
#user
#admin
class admin_adduser_table(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    role_type=models.CharField(max_length=100)
    status_type=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
class admin_reg_table(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.username
class admin_add_customer_table(models.Model):
    customer_name=models.CharField(max_length=100)
    customer_email=models.EmailField()
    customer_phone=models.CharField(max_length=100)
    customer_city=models.CharField(max_length=100)
    
    def __str__(self):
        return self.customer_name
class admin_add_vendor_table(models.Model):
    vendor_name=models.CharField(max_length=100)
    vendor_email=models.EmailField()
    vendor_phone=models.CharField(max_length=100)
    vendor_city=models.CharField(max_length=100)
    
    def __str__(self):
        return self.vendor_name
class admin_add_productlist_table(models.Model):
    product_name=models.CharField(max_length=100)
    product_brand=models.CharField(max_length=100)
    product_unit=models.CharField(max_length=100)
    product_selling_price=models.CharField(max_length=100)
    
    def __str__(self):
        return self.product_name     
class admin_addcategory_table(models.Model):
    category_name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.category_name
class admin_addbrand_table(models.Model):
    brand_name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.brand_name
class admin_addtax_table(models.Model):
    tax_name=models.CharField(max_length=100)
    tax_percentage=models.CharField(max_length=100)
    tax_dafault=models.CharField(max_length=100)
    
    def __str__(self):
        return self.tax_name    

class admin_add_role_table(models.Model):
    role_type=models.CharField(max_length=100)
    profile=models.CharField(max_length=100)
    notification=models.CharField(max_length=100)
    account=models.CharField(max_length=100)


    def __str__(self):
        return self.role_type

class admin_add_sale_table(models.Model):
    invoice_id=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    sold_by=models.CharField(max_length=100)
    sold_to=models.CharField(max_length=100)
    items_sold=models.CharField(max_length=100)
    payment=models.CharField(max_length=100)


    def __str__ (self):
        return self.sold_by

class admin_add_return_table(models.Model):
    c_name=models.CharField(max_length=100)
    c_email=models.EmailField()
    returned_dt=models.CharField(max_length=100)
    returned_item=models.CharField(max_length=100)


    def __str__ (self):
        return self.c_email 

class admin_add_stock_table(models.Model):
    p_name=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)


    def __str__ (self):
        return self.p_name

class admin_add_purchase_tax_table(models.Model):
    ref_number=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    vendor=models.CharField(max_length=100)
    p_tax=models.CharField(max_length=100)
    g_tot=models.CharField(max_length=100)


    def __str__ (self):
        return self.ref_number 

class admin_add_expense_report_table(models.Model):
    date=models.CharField(max_length=100)
    exp_category=models.CharField(max_length=100)
    note=models.CharField(max_length=100)
    created_by=models.CharField(max_length=100)


    def __str__ (self):
        return self.created_by  

class admin_add_customer_report_table(models.Model):
    name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=100)
    email=models.EmailField()
    tot_sales=models.CharField(max_length=100)
    tot_amt=models.CharField(max_length=100)


    def __str__ (self):
        return self.email 

class admin_add_quotation_table(models.Model):
    date=models.CharField(max_length=100)
    ref_number=models.CharField(max_length=100)
    customer=models.EmailField()
    customer_email=models.CharField(max_length=100)
    g_total=models.CharField(max_length=100)
    quo_note=models.CharField(max_length=200)


    def __str__ (self):
        return self.customer_email    

class admin_add_expense_list_table(models.Model):
    branch=models.CharField(max_length=100)
    exp_date=models.CharField(max_length=100)
    exp_category=models.EmailField()
    amount=models.CharField(max_length=100)
    note=models.CharField(max_length=100)


    def __str__ (self):
        return self.branch            