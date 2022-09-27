from atexit import register
from django.shortcuts import render
from . models import admin_addtax_table,admin_addbrand_table,admin_reg_table,contact_table,reg_table,admin_adduser_table,admin_add_customer_table,admin_add_vendor_table,admin_add_productlist_table,admin_addcategory_table,admin_add_role_table,admin_add_sale_table,admin_add_return_table,admin_add_stock_table,admin_add_purchase_tax_table,admin_add_expense_report_table,admin_add_customer_report_table,admin_add_quotation_table,admin_add_expense_list_table,addtax_table,addbrand_table,adduser_table,add_customer_table,add_vendor_table,add_productlist_table,addcategory_table,add_role_table,add_sale_table,add_return_table,add_stock_table,add_purchase_tax_table,add_expense_report_table,add_customer_report_table,add_quotation_table,add_expense_list_table
from django . contrib import messages
from django . contrib import auth
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
# Create your views here.

#landing page functions
def index(request):
    return render(request,'index.html')
def contact_form_submission(request):
    if request.method=='POST':
        ex1=contact_table(name=request.POST.get('name'),
                            email=request.POST.get('email'),
                            contact_no=request.POST.get('contact_no'),
                            message=request.POST.get('message'))        
        ex1.save()
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact_no=request.POST.get('contact_no')
        message=request.POST.get('message')
        template=render_to_string('message.html',{'name':name,'email':email,'contact_no':contact_no,'message':message})
        send_mail(
            'workssale message',
            template,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
            )
        messages.error(request,'Successfully sent...!')
        return render(request,'index.html')
    else:
        return render(request,'index.html')
def cart(request):
    return render(request,'cart.html')
def invoice(request):
    return render(request,'invoice.html')
def products(request):
    return render(request,'products.html')
def productdetail(request):
    return render(request,'productdetail.html')
#user signin or signup page functions
def sign(request):
    return render(request,'sign.html')
def signup_form_submission(request):
    try:
        if request.method=='POST':
            if reg_table.objects.filter(email=request.POST['email']).exists():
                messages.error(request,'Already Registered...!',extra_tags="taken")
                return render(request,'sign.html')
            else:
                ex1=reg_table(name=request.POST.get('name'),
                            contact_no=request.POST.get('contact_no'),
                            email=request.POST.get('email'),
                            password=request.POST.get('password'))        
                ex1.save()
                name=request.POST.get('name')
                contact_no=request.POST.get('contact_no')
                email=request.POST.get('email')
                password=request.POST.get('password')
                template=render_to_string('regsuccessmail.html',{'name':name,'email':email,'password':password})
                email=EmailMessage(
                    'Thanks for registered with Workssale',
                    template,
                    settings.EMAIL_HOST_USER,
                    [email],
                )
                email.fail_silently=False
                email.send()
                messages.error(request,'Successfully Registered',extra_tags="signup")
                return render(request,'sign.html')
        else:
            return render(request,'sign.html')
    except:
        return render(request,'404.html')

def signin_form_submission(request):
    if reg_table.objects.filter(email=request.POST['email'],password=request.POST['password']).exists():
        ex1=reg_table.objects.get(email=request.POST['email'],password=request.POST['password'])
        take_name=ex1.name
        take_mail=ex1.email
        logger_data=reg_table.objects.get(email=take_mail)
        return render(request,'dashboard.html',{'logger_data':logger_data})
    else:
        messages.error(request,'Invalid email or password',extra_tags="failed_login")
        return render(request,'sign.html')


#user_dashboard functions
def logout(request):
    auth.logout(request)
    return render(request,'sign.html')
def error_page(request):
    return render(request,'404.html')
def dashboard(request,id):
    data=add_sale_table.objects.filter(logger_id=id).count()
    data1=adduser_table.objects.filter(logger_id=id).count()
    data2=add_customer_table.objects.filter(logger_id=id).count()
    data3=add_vendor_table.objects.filter(logger_id=id).count()
    logger_data=reg_table.objects.get(id=id)
    return render(request,'dashboard.html',{'logger_data':logger_data,'data':data,'data1':data1,'data2':data2,'data3':data3})
def addbrand(request,id):
    logger_data=reg_table.objects.get(id=id)
    return render(request,'addbrand.html',{'logger_data':logger_data})
def addcategory(request,id):
    logger_data=reg_table.objects.get(id=id)
    return render(request,'addcategory.html',{'logger_data':logger_data})
def addcategory_form_submission(request,id):
    logger_data=reg_table.objects.get(id=id)
    if request.method=="POST":
        ex1=addcategory_table(category_name=request.POST.get('category_name'),
            logger_id=request.POST.get('logger_id'))
        ex1.save()
        messages.error(request,'Category added Successfully...!',extra_tags='uscategory')
        view_data=addcategory_table.objects.filter(logger_id=id)
        return render(request,'expensecategory.html',{'view_data':view_data,'logger_data':logger_data})
    else:
        return render(request,'addcategory.html',{'logger_data':logger_data})
#***************customer*************************    
def addcustomer(request,id):
    logger_data=reg_table.objects.get(id=id)
    return render(request,'addcustomer.html',{'logger_data':logger_data})

def add_customer_form_submission(request,id):
    logger_data=reg_table.objects.get(id=id)
    if request.method=="POST":
        ex1=add_customer_table(customer_name=request.POST.get('customer_name'),
                                        customer_email=request.POST.get('customer_email'),
                                        customer_phone=request.POST.get('customer_phone'),
                                        customer_city=request.POST.get('customer_city'),
                                        logger_id=request.POST.get('logger_id'))
        ex1.save()           
        view_data=add_customer_table.objects.filter(logger_id=id)
        messages.error(request,'Customer Added Successfully...!',extra_tags='uscustomer')             
        return render(request,'customers.html',{'view_data':view_data,'logger_data':logger_data})
    else:
        return render(request,'addcustomer.html',{'logger_data':logger_data})        

def addexpense(request):
    return render(request,'addexpense.html')

def addtax(request,id):
    logger_data=reg_table.objects.get(id=id)
    return render(request,'addtax.html',{'logger_data':logger_data})


def adduser(request,id):
    logger_data=reg_table.objects.get(id=id)
    return render(request,'adduser.html',{'logger_data':logger_data})
def adduser_form_submission(request,id):
    logger_data=reg_table.objects.get(id=id)
    if request.method=="POST":
        ex1=adduser_table(name=request.POST.get('name'),
            email=request.POST.get('email'),
            role_type=request.POST.get('role_type'),
            status_type=request.POST.get('status_type'),
            logger_id=request.POST.get('logger_id'))
        ex1.save()
        messages.error(request,'User Added Successfully...!',extra_tags='ususer')
        view_data=adduser_table.objects.filter(logger_id=id)
        return render(request,'users.html',{'view_data':view_data,'logger_data':logger_data})
    else:
        return render(request,'adduser.html',{'logger_data':logger_data})

#***************vendors*************************        
def addvendor(request,id):
    logger_data=reg_table.objects.get(id=id)
    return render(request,'addvendor.html',{'logger_data':logger_data})
def add_vendor_form_submission(request,id):
    logger_data=reg_table.objects.get(id=id)
    if request.method=="POST":
        ex1=add_vendor_table(vendor_name=request.POST.get('vendor_name'),
                            vendor_email=request.POST.get('vendor_email'),
                            vendor_phone=request.POST.get('vendor_phone'),
                            vendor_city=request.POST.get('vendor_city'),
                            logger_id=request.POST.get('logger_id'))
        ex1.save()
        view_data=add_vendor_table.objects.filter(logger_id=id)
        messages.error(request,'Vendor Added Successfully...!',extra_tags='usvendor')
        return render(request,'vendors.html',{'view_data':view_data,'logger_data':logger_data})
    else:
        return render(request,'addvendor.html',{'logger_data':logger_data})                        

def brands(request,id):
    view_data=addbrand_table.objects.filter(logger_id=id)
    logger_data=reg_table.objects.get(id=id)
    return render(request,'brands.html',{'view_data':view_data,'logger_data':logger_data})
def addbrand_form_submission(request,id):
    logger_data=reg_table.objects.get(id=id)
    if request.method=="POST":
        ex1=addbrand_table(brand_name=request.POST.get('brand_name'),
                   logger_id=request.POST.get('logger_id'))
        ex1.save()
        view_data=addbrand_table.objects.filter(logger_id=id)
        messages.error(request,'Brand Added Successfully...!',extra_tags='usbrand')
        return render(request,'brands.html',{'view_data':view_data,'logger_data':logger_data})
    else:
        return render(request,'addbrand.html',{'logger_data':logger_data})
def brands_update_form_submission(request,row_id,logger_id):
    logger_data=reg_table.objects.get(id=logger_id)
    if request.method=="POST":
        ex1=addbrand_table.objects.filter(id=row_id).update(brand_name=request.POST.get('brand_name'),
                                       logger_id=request.POST.get('logger_id'))
        view_data=addbrand_table.objects.filter(logger_id=logger_id)
        messages.error(request,'Brand Updated Successfully...!',extra_tags='usrand')
        return render(request,'brands.html',{'view_data':view_data,'logger_data':logger_data})
    else:
        return render(request,'editbrand.html',{'logger_data':logger_data})   
def brands_delete(request,row_id,logger_id):
    ex1=addbrand_table.objects.get(id=row_id)
    ex1.delete()
    view_data=addbrand_table.objects.filter(logger_id=logger_id)
    logger_data=reg_table.objects.get(id=logger_id)
    return render(request,'brands.html',{'view_data':view_data,'logger_data':logger_data})    



            

def calenders(request,id):
    logger_data=reg_table.objects.get(id=id)
    return render(request,'calenders.html',{'logger_data':logger_data})
def chat(request,id):
    logger_data=reg_table.objects.get(id=id)
    return render(request,'chat.html',{'logger_data':logger_data})

#***************customer*************************     
def customers(request,id):
    view_data=add_customer_table.objects.filter(logger_id=id)
    logger_data=reg_table.objects.get(id=id)
    return render(request,'customers.html',{'view_data':view_data,'logger_data':logger_data})


def editbrand(request,row_id,logger_id):
    logger_data=reg_table.objects.get(id=logger_id)
    view_data=addbrand_table.objects.get(id=row_id)
    return render(request,'editbrand.html',{'view_data':view_data,'logger_data':logger_data})

def editcategory(request,row_id,logger_id):
    logger_data=reg_table.objects.get(id=logger_id)
    view_data=addcategory_table.objects.get(id=row_id)
    return render(request,'editcategory.html',{'view_data':view_data,'logger_data':logger_data})
def update_category_form_submission(request,row_id,logger_id):
    logger_data=reg_table.objects.get(id=logger_id)
    if request.method=="POST":
        ex1=addcategory_table.objects.filter(id=row_id).update(category_name=request.POST.get('category_name'),
            logger_id=request.POST.get('logger_id'))
        view_data=addcategory_table.objects.filter(logger_id=logger_id)
        messages.error(request,'Category Updated Successfully...!',extra_tags='usategory')
        return render(request,'expensecategory.html',{'view_data':view_data,'logger_data':logger_data})
    else:
        return render(request,'editcategory.html',{'logger_data':logger_data})
def category_delete(request,row_id,logger_id):
    ex1=addcategory_table.objects.get(id=row_id)
    ex1.delete()
    view_data=addcategory_table.objects.filter(logger_id=logger_id)
    logger_data=reg_table.objects.get(id=logger_id)
    return render(request,'expensecategory.html',{'view_data':view_data,'logger_data':logger_data})

#***************customer************************* 
def editcustomer(request,row_id,logger_id):
    logger_data=reg_table.objects.get(id=logger_id)
    view_data=add_customer_table.objects.get(id=row_id)
    return render(request,'editcustomer.html',{'view_data':view_data,'logger_data':logger_data})
def customer_update_form_submission(request,row_id,logger_id):
    logger_data=reg_table.objects.get(id=logger_id)
    if request.method=="POST":
        ex1=add_customer_table.objects.filter(id=row_id).update(customer_name=request.POST.get('customer_name'),
                                        customer_email=request.POST.get('customer_email'),
                                        customer_phone=request.POST.get('customer_phone'),
                                        customer_city=request.POST.get('customer_city'),logger_id=request.POST.get('logger_id'))
        view_data=add_customer_table.objects.filter(logger_id=logger_id)
        messages.error(request,'Customer Updated Successfully...!',extra_tags='usustomer')
        return render(request,'customers.html',{'view_data':view_data,'logger_data':logger_data})
    else:
        return render(request,'editcustomer.html',{'logger_data':logger_data})



def customer_delete(request,row_id,logger_id):
    ex1=add_customer_table.objects.get(id=row_id)
    ex1.delete()
    view_data=add_customer_table.objects.filter(logger_id=logger_id)
    logger_data=reg_table.objects.get(id=logger_id)
    return render(request,'customers.html',{'view_data':view_data,'logger_data':logger_data})                                        

def editexpense(request):
    return render(request,'editexpense.html')

def edittax(request,row_id,logger_id):
    logger_data=reg_table.objects.get(id=logger_id)
    view_data=addtax_table.objects.get(id=row_id)
    return render(request,'edittax.html',{'view_data':view_data,'logger_data':logger_data})
def addtax_form_submission(request,id):
    logger_data=reg_table.objects.get(id=id)
    if request.method=="POST":
        ex1=addtax_table(tax_name=request.POST.get('tax_name'),
                               tax_percentage=request.POST.get('tax_percentage'),
                               tax_dafault=request.POST.get('tax_dafault'),
                               logger_id=request.POST.get('logger_id'))
        ex1.save()
        view_data=addtax_table.objects.filter(logger_id=id)
        messages.error(request,'Tax Added Successfully...!',extra_tags='ustax')
        return render(request,'tax.html',{'view_data':view_data,'logger_data':logger_data})
def tax_update_form_submission(request,row_id,logger_id):
    logger_data=reg_table.objects.get(id=logger_id)
    if request.method=="POST":
        ex1=addtax_table.objects.filter(id=row_id).update(tax_name=request.POST.get('tax_name'),
                                 tax_percentage=request.POST.get('tax_percentage'),
                               tax_dafault=request.POST.get('tax_dafault'),
                               logger_id=request.POST.get('logger_id'))
        view_data=addtax_table.objects.filter(logger_id=logger_id)
        messages.error(request,'Tax Updated Successfully...!',extra_tags='usax')
        return render(request,'tax.html',{'view_data':view_data,'logger_data':logger_data})
    else:
        return render(request,'edittax.html',{'logger_data':logger_data})
def tax_delete(request,row_id,logger_id):
    ex1=addtax_table.objects.get(id=row_id)
    ex1.delete()
    view_data=addtax_table.objects.filter(logger_id=logger_id)
    logger_data=reg_table.objects.get(id=logger_id)
    return render(request,'tax.html',{'view_data':view_data,'logger_data':logger_data})                                    



def edituser(request,row_id,logger_id):
    logger_data=reg_table.objects.get(id=logger_id)
    view_data=adduser_table.objects.get(id=row_id)
    return render(request,'edituser.html',{'view_data':view_data,'logger_data':logger_data})
def update_user_form_submission(request,row_id,logger_id):
    logger_data=reg_table.objects.get(id=logger_id)
    if request.method=="POST":
        ex1=adduser_table.objects.filter(id=row_id).update(name=request.POST.get('name'),
            email=request.POST.get('email'),
            role_type=request.POST.get('role_type'),
            status_type=request.POST.get('status_type'),
            logger_id=request.POST.get('logger_id'))
        view_data=adduser_table.objects.filter(logger_id=logger_id)
        messages.error(request,'User Updated Successfully...!',extra_tags='usser')
        return render(request,'users.html',{'view_data':view_data,'logger_data':logger_data})
    else:
        return render(request,'edituser.html',{'logger_data':logger_data})
def user_delete(request,row_id,logger_id):
    ex1=adduser_table.objects.get(id=row_id)
    ex1.delete()
    view_data=adduser_table.objects.filter(logger_id=logger_id)
    logger_data=reg_table.objects.get(id=logger_id)
    return render(request,'users.html',{'view_data':view_data,'logger_data':logger_data})

#***************vendors*************************
def editvendor(request,row_id,logger_id):
    logger_data=reg_table.objects.get(id=logger_id)
    view_data=add_vendor_table.objects.get(id=row_id)
    return render(request,'editvendor.html',{'view_data':view_data,'logger_data':logger_data})
def vendor_update_form_submission(request,row_id,logger_id):
    logger_data=reg_table.objects.get(id=logger_id)
    if request.method=="POST":
        ex1=add_vendor_table.objects.filter(id=row_id).update(vendor_name=request.POST.get('vendor_name'),
                            vendor_email=request.POST.get('vendor_email'),
                            vendor_phone=request.POST.get('vendor_phone'),
                            vendor_city=request.POST.get('vendor_city'),
                            logger_id=request.POST.get('logger_id'))
        view_data=add_vendor_table.objects.filter(logger_id=logger_id)
        messages.error(request,'Vendor Updated Successfully...!',extra_tags='usendor')
        return render(request,'vendors.html',{'view_data':view_data,'logger_data':logger_data})
    else:
        return render(request,'editvendor.html',{'logger_data':logger_data})     
def vendor_delete(request,row_id,logger_id):
    ex1=add_vendor_table.objects.get(id=row_id)
    ex1.delete()
    view_data=add_vendor_table.objects.filter(logger_id=logger_id)
    logger_data=reg_table.objects.get(id=logger_id)
    return render(request,'vendors.html',{'view_data':view_data,'logger_data':logger_data})



def expensecategory(request,id):
    view_data=addcategory_table.objects.filter(logger_id=id)
    logger_data=reg_table.objects.get(id=id)
    return render(request,'expensecategory.html',{'view_data':view_data,'logger_data':logger_data})
def expenselist(request):
    return render(request,'expenselist.html')
def profile(request,id):
    logger_data=reg_table.objects.get(id=id)
    return render(request,'profile.html',{'logger_data':logger_data})

def tax(request,id):
    view_data=addtax_table.objects.filter(logger_id=id)
    logger_data=reg_table.objects.get(id=id)
    return render(request,'tax.html',{'view_data':view_data,'logger_data':logger_data})
def users(request,id):
    view_data=adduser_table.objects.filter(logger_id=id)
    logger_data=reg_table.objects.get(id=id)
    return render(request,'users.html',{'view_data':view_data,'logger_data':logger_data})

#***************vendors*************************     
def vendors(request,id):
    view_data=add_vendor_table.objects.filter(logger_id=id)
    logger_data=reg_table.objects.get(id=id)
    return render(request,'vendors.html',{'view_data':view_data,'logger_data':logger_data})

#*****************product_list******************

def addproduct(request,id):
    logger_data=reg_table.objects.get(id=id)
    return render(request,'addproduct.html',{'logger_data':logger_data})
def editproduct(request,row_id,logger_id):
    logger_data=reg_table.objects.get(id=logger_id)
    view_data=add_productlist_table.objects.get(id=row_id)
    return render(request,'editproduct.html',{'view_data':view_data,'logger_data':logger_data})
def productlist(request,id):
    view_data=add_productlist_table.objects.filter(logger_id=id)
    logger_data=reg_table.objects.get(id=id)
    return render(request,'productlist.html',{'view_data':view_data,'logger_data':logger_data})
def add_product_form_submission(request,id):
    logger_data=reg_table.objects.get(id=id)
    if request.method=="POST":
        ex1=add_productlist_table(product_name=request.POST.get('product_name'),
                                  product_brand=request.POST.get('product_brand'),
                                  product_unit=request.POST.get('product_unit'),
                                  product_selling_price=request.POST.get('product_selling_price'),logger_id=request.POST.get('logger_id') )
        ex1.save()
        view_data=add_productlist_table.objects.filter(logger_id=id)
        messages.error(request,'Product Added Successfully...!',extra_tags='usproduct')
        return render(request,'productlist.html',{'view_data':view_data,'logger_data':logger_data}) 
    else:
        return render(request,'addproduct.html',{'logger_data':logger_data})
def product_update_form_submission(request,row_id,logger_id):
    logger_data=reg_table.objects.get(id=logger_id)
    if request.method=="POST":
        ex1=add_productlist_table.objects.filter(id=row_id).update(product_name=request.POST.get('product_name'),
                                  product_brand=request.POST.get('product_brand'),
                                  product_unit=request.POST.get('product_unit'),
                                  product_selling_price=request.POST.get('product_selling_price'),logger_id=request.POST.get('logger_id'))
        view_data=add_productlist_table.objects.filter(logger_id=logger_id)
        messages.error(request,'Product Updated Successfully...!',extra_tags='usroduct')
        return render(request,'productlist.html',{'view_data':view_data,'logger_data':logger_data})
    else:
        return render(request,'editproduct.html',{'logger_data':logger_data})
def product_delete(request,row_id,logger_id):
    ex1=add_productlist_table.objects.get(id=row_id)
    ex1.delete()
    view_data=add_productlist_table.objects.filter(logger_id=logger_id)
    logger_data=reg_table.objects.get(id=logger_id)
    return render(request,'productlist.html',{'view_data':view_data,'logger_data':logger_data})                                    
                                        
# ------- Roles ------- #

def roles(request,id):
    view_data=add_role_table.objects.filter(logger_id=id)
    logger_data=reg_table.objects.get(id=id)
    return render(request,'roles.html',{'view_data':view_data,'logger_data':logger_data})

def addrole(request,id):
    logger_data=reg_table.objects.get(id=id)
    return render(request,'addrole.html',{'logger_data':logger_data})

def add_role_form_submission(request,id):
    logger_data=reg_table.objects.get(id=id)
    if request.method=="POST":
        ex1=add_role_table(role_type=request.POST.get('role_type'),
                                profile=request.POST.getlist('profile'),
                                notification=request.POST.getlist('notification'),
                                account=request.POST.getlist('account'),
                                logger_id=request.POST.get('logger_id'))                        
        ex1.save()           
        view_data=add_role_table.objects.filter(logger_id=id)
        messages.error(request,'Role Added Successfully...!',extra_tags='usrole')             
        return render(request,'roles.html',{'view_data':view_data,'logger_data':logger_data})
    else:
        return render(request,'addrole.html',{'logger_data':logger_data})        


def editrole(request,row_id,logger_id):
    logger_data=reg_table.objects.get(id=logger_id)
    view_data=add_role_table.objects.get(id=row_id)
    return render(request,'editrole.html',{'view_data':view_data,'logger_data':logger_data})


def update_role_form_submission(request,row_id,logger_id):
    logger_data=reg_table.objects.get(id=logger_id)
    if request.method=="POST":
        ex1=add_role_table.objects.filter(id=row_id).update(role_type=request.POST.get('role_type'),
                                profile=request.POST.getlist('profile'),
                                notification=request.POST.getlist('notification'),
                                account=request.POST.getlist('account'),
                                logger_id=request.POST.get('logger_id'))
        view_data=add_role_table.objects.filter(logger_id=logger_id)
        messages.error(request,'Role Updated Successfully...!',extra_tags='usole')
        return render(request,'roles.html',{'view_data':view_data,'logger_data':logger_data})
    else:
        return render(request,'editrole.html',{'logger_data':logger_data})
def role_delete(request,row_id,logger_id):
    ex1=add_role_table.objects.get(id=row_id)
    ex1.delete()
    view_data=add_role_table.objects.filter(logger_id=logger_id)
    logger_data=reg_table.objects.get(id=logger_id)
    return render(request,'roles.html',{'view_data':view_data,'logger_data':logger_data})                                    

# ---------- Sales ---------- #

def sales(request,id):
    view_data=add_sale_table.objects.filter(logger_id=id)
    logger_data=reg_table.objects.get(id=id)
    return render(request,'sales.html',{'view_data':view_data,'logger_data':logger_data})

def addsale(request,id):
    logger_data=reg_table.objects.get(id=id)
    return render(request,'addsale.html',{'logger_data':logger_data})

def add_sale_form_submission(request,id):
    logger_data=reg_table.objects.get(id=id)
    if request.method=="POST":
        ex1=add_sale_table(invoice_id=request.POST.get('invoice_id'),
            date=request.POST.get('date'),
            sold_by=request.POST.get('sold_by'),
            sold_to=request.POST.get('sold_to'),
            items_sold=request.POST.get('items_sold'),
            payment=request.POST.get('payment'),
            logger_id=request.POST.get('logger_id'))
        ex1.save()
        messages.error(request,'Sale Added Successfully...!',extra_tags='ussale')
        view_data=add_sale_table.objects.filter(logger_id=id)
        return render(request,'sales.html',{'view_data':view_data,'logger_data':logger_data})
    else:
        return render(request,'addsale.html',{'logger_data':logger_data})

def editsale(request,row_id,logger_id):
    logger_data=reg_table.objects.get(id=logger_id)
    view_data=add_sale_table.objects.get(id=row_id)
    return render(request,'editsale.html',{'view_data':view_data,'logger_data':logger_data})

def update_sale_form_submission(request,row_id,logger_id):
    logger_data=reg_table.objects.get(id=logger_id)
    if request.method=="POST":
        ex1=add_sale_table.objects.filter(id=row_id).update(invoice_id=request.POST.get('invoice_id'),
            date=request.POST.get('date'),
            sold_by=request.POST.get('sold_by'),
            sold_to=request.POST.get('sold_to'),
            items_sold=request.POST.get('items_sold'),
            payment=request.POST.get('payment'),
            logger_id=request.POST.get('logger_id'))
        view_data=add_sale_table.objects.filter(logger_id=logger_id)
        messages.error(request,'Sale Updated Successfully...!',extra_tags='usale')
        return render(request,'sales.html',{'view_data':view_data,'logger_data':logger_data})
    else:
        return render(request,'editsale.html',{'logger_data':logger_data})
def sale_delete(request,row_id,logger_id):
    ex1=add_sale_table.objects.get(id=row_id)
    ex1.delete()
    view_data=add_sale_table.objects.filter(logger_id=logger_id)
    logger_data=reg_table.objects.get(id=logger_id)
    return render(request,'sales.html',{'view_data':view_data,'logger_data':logger_data})                                    

# ---------- Return --------- #

def returns(request,id):
    view_data=add_return_table.objects.filter(logger_id=id)
    logger_data=reg_table.objects.get(id=id)
    return render(request,'returns.html',{'view_data':view_data,'logger_data':logger_data})

def addreturn(request,id):
    logger_data=reg_table.objects.get(id=id)
    return render(request,'addreturn.html',{'logger_data':logger_data})

def add_return_form_submission(request,id):
    logger_data=reg_table.objects.get(id=id)
    if request.method=="POST":
        ex1=add_return_table(c_name=request.POST.get('c_name'),
            c_email=request.POST.get('c_email'),
            returned_dt=request.POST.get('returned_dt'),
            returned_item=request.POST.get('returned_item'),
            logger_id=request.POST.get('logger_id'))
        ex1.save()
        messages.error(request,'Return Added Successfully...!',extra_tags='usreturn')
        view_data=add_return_table.objects.filter(logger_id=id)
        return render(request,'returns.html',{'view_data':view_data,'logger_data':logger_data})
    else:
        return render(request,'addreturn.html',{'logger_data':logger_data})

def editreturn(request,row_id,logger_id):
    logger_data=reg_table.objects.get(id=logger_id)
    view_data=add_return_table.objects.get(id=row_id)
    return render(request,'editreturn.html',{'view_data':view_data,'logger_data':logger_data})

def update_return_form_submission(request,row_id,logger_id):
    logger_data=reg_table.objects.get(id=logger_id)
    if request.method=="POST":
        ex1=add_return_table.objects.filter(id=row_id).update(c_name=request.POST.get('c_name'),
            c_email=request.POST.get('c_email'),
            returned_dt=request.POST.get('returned_dt'),
            returned_item=request.POST.get('returned_item'),
            logger_id=request.POST.get('logger_id'))
        view_data=add_return_table.objects.filter(logger_id=logger_id)
        messages.error(request,'Return Updated Successfully...!',extra_tags='useturn')
        return render(request,'returns.html',{'view_data':view_data,'logger_data':logger_data})
    else:
        return render(request,'editreturn.html',{'logger_data':logger_data})
def return_delete(request,row_id,logger_id):
    ex1=add_return_table.objects.get(id=row_id)
    ex1.delete()
    view_data=add_return_table.objects.filter(logger_id=logger_id)
    logger_data=reg_table.objects.get(id=logger_id)
    return render(request,'returns.html',{'view_data':view_data,'logger_data':logger_data})                                    

# ------------- Stock_Analysis ------------- #

def stockanalysis(request,id):
    view_data=add_stock_table.objects.filter(logger_id=id)
    logger_data=reg_table.objects.get(id=id)
    return render(request,'stockanalysis.html',{'view_data':view_data,'logger_data':logger_data})

def addstock(request,id):
    logger_data=reg_table.objects.get(id=id)
    return render(request,'addstock.html',{'logger_data':logger_data})

def add_stock_form_submission(request,id):
    logger_data=reg_table.objects.get(id=id)
    if request.method=="POST":
        ex1=add_stock_table(p_name=request.POST.get('p_name'),
            quantity=request.POST.get('quantity'),
            logger_id=request.POST.get('logger_id'))
        ex1.save()
        messages.error(request,'Stock Added Successfully...!',extra_tags='usstock')
        view_data=add_stock_table.objects.filter(logger_id=id)
        return render(request,'stockanalysis.html',{'view_data':view_data,'logger_data':logger_data})
    else:
        return render(request,'addstock.html',{'logger_data':logger_data})

def editstock(request,row_id,logger_id):
    logger_data=reg_table.objects.get(id=logger_id)
    view_data=add_stock_table.objects.get(id=row_id)
    return render(request,'editstock.html',{'view_data':view_data,'logger_data':logger_data})

def update_stock_form_submission(request,row_id,logger_id):
    logger_data=reg_table.objects.get(id=logger_id)
    if request.method=="POST":
        ex1=add_stock_table.objects.filter(id=row_id).update(p_name=request.POST.get('p_name'),
            quantity=request.POST.get('quantity'),
            logger_id=request.POST.get('logger_id'))
        view_data=add_stock_table.objects.filter(logger_id=logger_id)
        messages.error(request,'Stock Updated Successfully...!',extra_tags='ustock')
        return render(request,'stockanalysis.html',{'view_data':view_data,'logger_data':logger_data})
    else:
        return render(request,'editstock.html',{'logger_data':logger_data})
def stock_delete(request,row_id,logger_id):
    ex1=add_stock_table.objects.get(id=row_id)
    ex1.delete()
    view_data=add_stock_table.objects.filter(logger_id=logger_id)
    logger_data=reg_table.objects.get(id=logger_id)
    return render(request,'stockanalysis.html',{'view_data':view_data,'logger_data':logger_data})                                    

# ----------- Purchase_Tax_Report ----------- #

def purchasetaxreport(request,id):
    view_data=add_purchase_tax_table.objects.filter(logger_id=id)
    logger_data=reg_table.objects.get(id=id)
    return render(request,'purchasetaxreport.html',{'view_data':view_data,'logger_data':logger_data})

def addpurchasetax(request,id):
    logger_data=reg_table.objects.get(id=id)
    return render(request,'addpurchasetax.html',{'logger_data':logger_data})

def add_purchase_tax_form_submission(request,id):
    logger_data=reg_table.objects.get(id=id)
    if request.method=="POST":
        ex1=add_purchase_tax_table(ref_number=request.POST.get('ref_number'),
            date=request.POST.get('date'),
            vendor=request.POST.get('vendor'),
            p_tax=request.POST.get('p_tax'),
            g_tot=request.POST.get('g_tot'),
            logger_id=request.POST.get('logger_id'))
        ex1.save()
        messages.error(request,'Purchase Tax Added Successfully...!',extra_tags='uspurchase_tax')
        view_data=add_purchase_tax_table.objects.filter(logger_id=id)
        return render(request,'purchasetaxreport.html',{'view_data':view_data,'logger_data':logger_data})
    else:
        return render(request,'addpurchasetax.html',{'logger_data':logger_data})

def editpurchasetax(request,row_id,logger_id):
    logger_data=reg_table.objects.get(id=logger_id)
    view_data=add_purchase_tax_table.objects.get(id=row_id)
    return render(request,'editpurchasetax.html',{'view_data':view_data,'logger_data':logger_data})

def update_purchase_tax_form_submission(request,row_id,logger_id):
    logger_data=reg_table.objects.get(id=logger_id)
    if request.method=="POST":
        ex1=add_purchase_tax_table.objects.filter(id=row_id).update(ref_number=request.POST.get('ref_number'),
            date=request.POST.get('date'),
            vendor=request.POST.get('vendor'),
            p_tax=request.POST.get('p_tax'),
            g_tot=request.POST.get('g_tot'),
            logger_id=request.POST.get('logger_id'))
        view_data=add_purchase_tax_table.objects.filter(logger_id=logger_id)
        messages.error(request,'Purchase Tax Updated Successfully...!',extra_tags='usurchase_tax')
        return render(request,'purchasetaxreport.html',{'view_data':view_data,'logger_data':logger_data})
    else:
        return render(request,'editpurchasetax.html',{'logger_data':logger_data})
def purchase_tax_delete(request,row_id,logger_id):
    ex1=add_purchase_tax_table.objects.get(id=row_id)
    ex1.delete()
    view_data=add_purchase_tax_table.objects.filter(logger_id=logger_id)
    logger_data=reg_table.objects.get(id=logger_id)
    return render(request,'purchasetaxreport.html',{'view_data':view_data,'logger_data':logger_data}) 
    

# ---------- Expense_Report ------------ #

def expensereport(request,id):
    view_data=add_expense_report_table.objects.filter(logger_id=id)
    logger_data=reg_table.objects.get(id=id)
    return render(request,'expensereport.html',{'view_data':view_data,'logger_data':logger_data})

def addexpensereport(request,id):
    logger_data=reg_table.objects.get(id=id)
    return render(request,'addexpensereport.html',{'logger_data':logger_data})

def add_expense_report_form_submission(request,id):
    logger_data=reg_table.objects.get(id=id)
    if request.method=="POST":
        ex1=add_expense_report_table(date=request.POST.get('date'),
            exp_category=request.POST.get('exp_category'),
            note=request.POST.get('note'),
            created_by=request.POST.get('created_by'),
            logger_id=request.POST.get('logger_id'))
        ex1.save()
        messages.error(request,'Expense Report Added Successfully...!',extra_tags='usexpense_report')
        view_data=add_expense_report_table.objects.filter(logger_id=id)
        return render(request,'expensereport.html',{'view_data':view_data,'logger_data':logger_data})
    else:
        return render(request,'addexpensereport.html',{'logger_data':logger_data})

def editexpensereport(request,row_id,logger_id):
    logger_data=reg_table.objects.get(id=logger_id)
    view_data=add_expense_report_table.objects.get(id=row_id)
    return render(request,'editexpensereport.html',{'view_data':view_data,'logger_data':logger_data})

def update_expense_report_form_submission(request,row_id,logger_id):
    logger_data=reg_table.objects.get(id=logger_id)
    if request.method=="POST":
        ex1=add_expense_report_table.objects.filter(id=row_id).update(date=request.POST.get('date'),
            exp_category=request.POST.get('exp_category'),
            note=request.POST.get('note'),
            created_by=request.POST.get('created_by'),
            logger_id=request.POST.get('logger_id'))
        view_data=add_expense_report_table.objects.filter(logger_id=logger_id)
        messages.error(request,'Expense Report Updated Successfully...!',extra_tags='usxpense_report')
        return render(request,'expensereport.html',{'view_data':view_data,'logger_data':logger_data})
    else:
        return render(request,'editexpensereport.html',{'logger_data':logger_data})
def expense_report_delete(request,row_id,logger_id):
    ex1=add_expense_report_table.objects.get(id=row_id)
    ex1.delete()
    view_data=add_expense_report_table.objects.filter(logger_id=logger_id)
    logger_data=reg_table.objects.get(id=logger_id)
    return render(request,'expensereport.html',{'view_data':view_data,'logger_data':logger_data}) 

# --------- Customer_Report --------- #

def customerreport(request,id):
    view_data=add_customer_report_table.objects.filter(logger_id=id)
    logger_data=reg_table.objects.get(id=id)
    return render(request,'customerreport.html',{'view_data':view_data,'logger_data':logger_data})

def addcustomerreport(request,id):
    logger_data=reg_table.objects.get(id=id)
    return render(request,'addcustomerreport.html',{'logger_data':logger_data})

def add_customer_report_form_submission(request,id):
    logger_data=reg_table.objects.get(id=id)
    if request.method=="POST":
        ex1=add_customer_report_table(name=request.POST.get('name'),
            phone_number=request.POST.get('phone_number'),
            email=request.POST.get('email'),
            tot_sales=request.POST.get('tot_sales'),
            tot_amt=request.POST.get('tot_amt'),
            logger_id=request.POST.get('logger_id'))
        ex1.save()
        messages.error(request,'Customer Report Added Successfully...!',extra_tags='uscustomer_report')
        view_data=add_customer_report_table.objects.filter(logger_id=id)
        return render(request,'customerreport.html',{'view_data':view_data,'logger_data':logger_data})
    else:
        return render(request,'addcustomerreport.html',{'logger_data':logger_data})

def editcustomerreport(request,row_id,logger_id):
    logger_data=reg_table.objects.get(id=logger_id)
    view_data=add_customer_report_table.objects.get(id=row_id)
    return render(request,'editcustomerreport.html',{'view_data':view_data,'logger_data':logger_data})

def update_customer_report_form_submission(request,row_id,logger_id):
    logger_data=reg_table.objects.get(id=logger_id)
    if request.method=="POST":
        ex1=add_customer_report_table.objects.filter(id=row_id).update(name=request.POST.get('name'),
            phone_number=request.POST.get('phone_number'),
            email=request.POST.get('email'),
            tot_sales=request.POST.get('tot_sales'),
            tot_amt=request.POST.get('tot_amt'),
            logger_id=request.POST.get('logger_id'))
        view_data=add_customer_report_table.objects.filter(logger_id=logger_id)
        messages.error(request,'Customer Report Updated Successfully...!',extra_tags='usustomer_report')
        return render(request,'customerreport.html',{'view_data':view_data,'logger_data':logger_data})
    else:
        return render(request,'editcustomerreport.html',{'logger_data':logger_data})
def customer_report_delete(request,row_id,logger_id):
    ex1=add_customer_report_table.objects.get(id=row_id)
    ex1.delete()
    view_data=add_customer_report_table.objects.filter(logger_id=logger_id)
    logger_data=reg_table.objects.get(id=logger_id)
    return render(request,'customerreport.html',{'view_data':view_data,'logger_data':logger_data}) 

# ---------- Quotation ------------ #

def quotations(request,id):
    view_data=add_quotation_table.objects.filter(logger_id=id)
    logger_data=reg_table.objects.get(id=id)
    return render(request,'quotations.html',{'view_data':view_data,'logger_data':logger_data})

def addquotation(request,id):
    logger_data=reg_table.objects.get(id=id)
    return render(request,'addquotation.html',{'logger_data':logger_data})

def add_quotation_form_submission(request,id):
    logger_data=reg_table.objects.get(id=id)
    if request.method=="POST":
        ex1=add_quotation_table(date=request.POST.get('date'),
            ref_number=request.POST.get('ref_number'),
            customer=request.POST.get('customer'),
            customer_email=request.POST.get('customer_email'),
            g_total=request.POST.get('g_total'),
            quo_note=request.POST.get('quo_note'),
            logger_id=request.POST.get('logger_id'))
        ex1.save()
        messages.error(request,'Quotation Added Successfully...!',extra_tags='usquotation')
        view_data=add_quotation_table.objects.filter(logger_id=id)
        return render(request,'quotations.html',{'view_data':view_data,'logger_data':logger_data})
    else:
        return render(request,'addquotation.html',{'logger_data':logger_data})

def editquotation(request,row_id,logger_id):
    logger_data=reg_table.objects.get(id=logger_id)
    view_data=add_quotation_table.objects.get(id=row_id)
    return render(request,'editquotation.html',{'view_data':view_data,'logger_data':logger_data})

def update_quotation_form_submission(request,row_id,logger_id):
    logger_data=reg_table.objects.get(id=logger_id)
    if request.method=="POST":
        ex1=add_quotation_table.objects.filter(id=row_id).update(date=request.POST.get('date'),
            ref_number=request.POST.get('ref_number'),
            customer=request.POST.get('customer'),
            customer_email=request.POST.get('customer_email'),
            g_total=request.POST.get('g_total'),
            quo_note=request.POST.get('quo_note'),
            logger_id=request.POST.get('logger_id'))
        view_data=add_quotation_table.objects.filter(logger_id=logger_id)
        messages.error(request,'Quotation Updated Successfully...!',extra_tags='usuotation')
        return render(request,'quotations.html',{'view_data':view_data,'logger_data':logger_data})
    else:
        return render(request,'editquotation.html',{'logger_data':logger_data})
def quotation_delete(request,row_id,logger_id):
    ex1=add_quotation_table.objects.get(id=row_id)
    ex1.delete()
    view_data=add_quotation_table.objects.filter(logger_id=logger_id)
    logger_data=reg_table.objects.get(id=logger_id)
    return render(request,'quotations.html',{'view_data':view_data,'logger_data':logger_data}) 

# ---------- Expense_List ------------ #

def expenselist(request,id):
    view_data=add_expense_list_table.objects.filter(logger_id=id)
    logger_data=reg_table.objects.get(id=id)
    return render(request,'expenselist.html',{'view_data':view_data,'logger_data':logger_data})

def addexpense(request,id):
    logger_data=reg_table.objects.get(id=id)
    return render(request,'addexpense.html',{'logger_data':logger_data})

def add_expense_list_form_submission(request,id):
    logger_data=reg_table.objects.get(id=id)
    if request.method=="POST":
        ex1=add_expense_list_table(branch=request.POST.get('branch'),
            exp_date=request.POST.get('exp_date'),
            exp_category=request.POST.get('exp_category'),
            amount=request.POST.get('amount'),
            note=request.POST.get('note'),
            logger_id=request.POST.get('logger_id'))
        ex1.save()
        messages.error(request,'Expense List Added Successfully...!',extra_tags='usexpense_list')
        view_data=add_expense_list_table.objects.filter(logger_id=id)
        return render(request,'expenselist.html',{'view_data':view_data,'logger_data':logger_data})
    else:
        return render(request,'addexpense.html',{'logger_data':logger_data})

def editexpense(request,row_id,logger_id):
    logger_data=reg_table.objects.get(id=logger_id)
    view_data=add_expense_list_table.objects.get(id=row_id)
    return render(request,'editexpense.html',{'view_data':view_data,'logger_data':logger_data})

def update_expense_list_form_submission(request,row_id,logger_id):
    logger_data=reg_table.objects.get(id=logger_id)
    if request.method=="POST":
        ex1=add_expense_list_table.objects.filter(id=row_id).update(branch=request.POST.get('branch'),
            exp_date=request.POST.get('exp_date'),
            exp_category=request.POST.get('exp_category'),
            amount=request.POST.get('amount'),
            note=request.POST.get('note'),
            logger_id=request.POST.get('logger_id'))
        view_data=add_expense_list_table.objects.filter(logger_id=logger_id)
        messages.error(request,'Expense List Updated Successfully...!',extra_tags='usxpense_list')
        return render(request,'expenselist.html',{'view_data':view_data,'logger_data':logger_data})
    else:
        return render(request,'editexpense.html',{'logger_data':logger_data})
def expense_list_delete(request,row_id,logger_id):
    ex1=add_expense_list_table.objects.get(id=row_id)
    ex1.delete()
    view_data=add_expense_list_table.objects.filter(logger_id=logger_id)
    logger_data=reg_table.objects.get(id=logger_id)
    return render(request,'expenselist.html',{'view_data':view_data,'logger_data':logger_data})

def compose(request,id):
    logger_data=reg_table.objects.get(id=id)
    return render(request,'compose.html',{'logger_data':logger_data})
def viewmail(request,id):
    logger_data=reg_table.objects.get(id=id)
    return render(request,'viewmail.html',{'logger_data':logger_data})
def inbox(request,id):
    logger_data=reg_table.objects.get(id=id)
    return render(request,'inbox.html',{'logger_data':logger_data})



#admin_dashboard functions
def admin_signin(request):
    return render(request,'admin_signin.html')
def admin_signup(request):
    return render(request,'admin_signup.html')
def admin_signup_form_submission(request):
        if request.method=='POST':
            if admin_reg_table.objects.filter(email=request.POST['email']).exists():
                messages.error(request,'Already Registered...!',extra_tags="taken")
                return render(request,'admin_signup.html')
            else:
                ex1=admin_reg_table(username=request.POST.get('username'),
                            email=request.POST.get('email'),
                            password=request.POST.get('password'))        
                ex1.save()
                messages.error(request,'Successfully Registered',extra_tags="signup")
                return render(request,'admin_signin.html')
        else:
            return render(request,'admin_signup.html')
def admin_signin_form_submission(request):
    if admin_reg_table.objects.filter(email=request.POST['email'],password=request.POST['password']).exists():
        ex1=admin_reg_table.objects.get(email=request.POST['email'],password=request.POST['password'])
        take_name=ex1.username
        take_mail=ex1.email
        logger_data=admin_reg_table.objects.get(email=take_mail)
        return render(request,'admin_dashboard.html',{'logger_data':logger_data})
    else:
        messages.error(request,'Invalid email or password',extra_tags="failed_login")
        return render(request,'admin_signin.html')
def admin_logout(request):
    auth.admin_logout(request)
    return render(request,'admin_signin.html')
def error_page(request):
    return render(request,'404.html')
def admin_dashboard(request):
    data=admin_add_sale_table.objects.all().count()
    data1=admin_adduser_table.objects.all().count()
    data2=admin_add_customer_table.objects.all().count()
    data3=admin_add_vendor_table.objects.all().count()
    return render(request,'admin_dashboard.html',{'data':data,'data1':data1,'data2':data2,'data3':data3})
def admin_addbrand(request):

    return render(request,'admin_addbrand.html')
def admin_addcategory(request):
        return render(request,'admin_addcategory.html')
def admin_addcategory_form_submission(request):

    if request.method=="POST":
        ex1=admin_addcategory_table(category_name=request.POST.get('category_name'))
        ex1.save()
        messages.error(request,'Category added Successfully...!',extra_tags='adcategory')
        view_data=admin_addcategory_table.objects.all()
        return render(request,'admin_expensecategory.html',{'view_data':view_data})
    else:
        return render(request,'admin_addcategory.html')
#***************admin_customer*************************    
def admin_addcustomer(request):

    return render(request,'admin_addcustomer.html')

def admin_add_customer_form_submission(request):

    if request.method=="POST":
        ex1=admin_add_customer_table(customer_name=request.POST.get('customer_name'),
                                        customer_email=request.POST.get('customer_email'),
                                        customer_phone=request.POST.get('customer_phone'),
                                        customer_city=request.POST.get('customer_city'))
        ex1.save()           
        view_data=admin_add_customer_table.objects.all()
        messages.error(request,'Customer Added Successfully...!',extra_tags='adcustomer')             
        return render(request,'admin_customers.html',{'view_data':view_data})
    else:
        return render(request,'admin_addcustomer.html')        

def admin_addexpense(request):
    return render(request,'admin_addexpense.html')

def admin_addtax(request):

    return render(request,'admin_addtax.html')


def admin_adduser(request):

    return render(request,'admin_adduser.html')
def admin_adduser_form_submission(request):

    if request.method=="POST":
        ex1=admin_adduser_table(name=request.POST.get('name'),
            email=request.POST.get('email'),
            role_type=request.POST.get('role_type'),
            status_type=request.POST.get('status_type'))
        ex1.save()
        messages.error(request,'User Added Successfully...!',extra_tags='aduser')
        view_data=admin_adduser_table.objects.all()
        return render(request,'admin_users.html',{'view_data':view_data})
    else:
        return render(request,'admin_adduser.html')

#***************admin_vendors*************************        
def admin_addvendor(request):

    return render(request,'admin_addvendor.html')
def admin_add_vendor_form_submission(request):

    if request.method=="POST":
        ex1=admin_add_vendor_table(vendor_name=request.POST.get('vendor_name'),
                            vendor_email=request.POST.get('vendor_email'),
                            vendor_phone=request.POST.get('vendor_phone'),
                            vendor_city=request.POST.get('vendor_city'))
        ex1.save()
        view_data=admin_add_vendor_table.objects.all()
        messages.error(request,'Vendor Added Successfully...!',extra_tags='advendor')
        return render(request,'admin_vendors.html',{'view_data':view_data})
    else:
        return render(request,'admin_addvendor.html')                        


def admin_brands(request):
    view_data=admin_addbrand_table.objects.all()

    return render(request,'admin_brands.html',{'view_data':view_data})
def admin_addbrand_form_submission(request):

    if request.method=="POST":
        ex1=admin_addbrand_table(brand_name=request.POST.get('brand_name'))
        ex1.save()
        view_data=admin_addbrand_table.objects.all()
        messages.error(request,'Brand Added Successfully...!',extra_tags='adbrand')
        return render(request,'admin_brands.html',{'view_data':view_data})
    else:
        return render(request,'admin_addbrand.html')
def admin_brands_update_form_submission(request,row_id):
    
    if request.method=="POST":
        ex1=admin_addbrand_table.objects.filter(id=row_id).update(brand_name=request.POST.get('brand_name'))
        view_data=admin_addbrand_table.objects.all()
        messages.error(request,'Brand Updated Successfully...!',extra_tags='adrand')
        return render(request,'admin_brands.html',{'view_data':view_data})
    else:
        return render(request,'admin_editbrand.html')   
def admin_brands_delete(request,row_id):
    ex1=admin_addbrand_table.objects.get(id=row_id)
    ex1.delete()
    view_data=admin_addbrand_table.objects.all()
    
    return render(request,'admin_brands.html',{'view_data':view_data})    



            

def admin_calenders(request):
    return render(request,'admin_calenders.html')
def admin_chat(request):
    return render(request,'admin_chat.html')

#***************admin_customer*************************     
def admin_customers(request):
    view_data=admin_add_customer_table.objects.all()

    return render(request,'admin_customers.html',{'view_data':view_data})


def admin_editbrand(request,row_id):
    
    view_data=admin_addbrand_table.objects.get(id=row_id)
    return render(request,'admin_editbrand.html',{'view_data':view_data})

def admin_editcategory(request,row_id):
    
    view_data=admin_addcategory_table.objects.get(id=row_id)
    return render(request,'admin_editcategory.html',{'view_data':view_data})
def update_admin_category_form_submission(request,row_id):
    
    if request.method=="POST":
        ex1=admin_addcategory_table.objects.filter(id=row_id).update(category_name=request.POST.get('category_name'),
            )
        view_data=admin_addcategory_table.objects.all()
        messages.error(request,'Category Updated Successfully...!',extra_tags='adategory')
        return render(request,'admin_expensecategory.html',{'view_data':view_data})
    else:
        return render(request,'admin_editcategory.html')
def admin_category_delete(request,row_id):
    ex1=admin_addcategory_table.objects.get(id=row_id)
    ex1.delete()
    view_data=admin_addcategory_table.objects.all()
    
    return render(request,'admin_expensecategory.html',{'view_data':view_data})

#***************admin_customer************************* 
def admin_editcustomer(request,row_id):
    
    view_data=admin_add_customer_table.objects.get(id=row_id)
    return render(request,'admin_editcustomer.html',{'view_data':view_data})
def admin_customer_update_form_submission(request,row_id):
    
    if request.method=="POST":
        ex1=admin_add_customer_table.objects.filter(id=row_id).update(customer_name=request.POST.get('customer_name'),
                                        customer_email=request.POST.get('customer_email'),
                                        customer_phone=request.POST.get('customer_phone'),
                                        customer_city=request.POST.get('customer_city'))
        view_data=admin_add_customer_table.objects.all()
        messages.error(request,'Customer Updated Successfully...!',extra_tags='adustomer')
        return render(request,'admin_customers.html',{'view_data':view_data})
    else:
        return render(request,'admin_editcustomer.html')



def admin_customer_delete(request,row_id):
    ex1=admin_add_customer_table.objects.get(id=row_id)
    ex1.delete()
    view_data=admin_add_customer_table.objects.all()
    
    return render(request,'admin_customers.html',{'view_data':view_data})                                        

def admin_editexpense(request):
    return render(request,'admin_editexpense.html')

def admin_edittax(request,row_id):
    
    view_data=admin_addtax_table.objects.get(id=row_id)
    return render(request,'admin_edittax.html',{'view_data':view_data})
def admin_addtax_form_submission(request):

    if request.method=="POST":
        ex1=admin_addtax_table(tax_name=request.POST.get('tax_name'),
                               tax_percentage=request.POST.get('tax_percentage'),
                               tax_dafault=request.POST.get('tax_dafault'))
        ex1.save()
        view_data=admin_addtax_table.objects.all()
        messages.error(request,'Tax Added Successfully...!',extra_tags='adtax')
        return render(request,'admin_tax.html',{'view_data':view_data})
def admin_tax_update_form_submission(request,row_id):
    
    if request.method=="POST":
        ex1=admin_addtax_table.objects.filter(id=row_id).update(tax_name=request.POST.get('tax_name'),
                                 tax_percentage=request.POST.get('tax_percentage'),
                               tax_dafault=request.POST.get('tax_dafault'))
        view_data=admin_addtax_table.objects.all()
        messages.error(request,'Tax Updated Successfully...!',extra_tags='adax')
        return render(request,'admin_tax.html',{'view_data':view_data})
    else:
        return render(request,'admin_edittax.html')
def admin_tax_delete(request,row_id):
    ex1=admin_addtax_table.objects.get(id=row_id)
    ex1.delete()
    view_data=admin_addtax_table.objects.all()
    
    return render(request,'admin_tax.html',{'view_data':view_data})                                    



def admin_edituser(request,row_id):
    
    view_data=admin_adduser_table.objects.get(id=row_id)
    return render(request,'admin_edituser.html',{'view_data':view_data})
def update_admin_user_form_submission(request,row_id):
    
    if request.method=="POST":
        ex1=admin_adduser_table.objects.filter(id=row_id).update(name=request.POST.get('name'),
            email=request.POST.get('email'),
            role_type=request.POST.get('role_type'))
        view_data=admin_adduser_table.objects.all()
        messages.error(request,'User Updated Successfully...!',extra_tags='adser')
        return render(request,'admin_users.html',{'view_data':view_data})
    else:
        return render(request,'admin_edituser.html')
def admin_user_delete(request,row_id):
    ex1=admin_adduser_table.objects.get(id=row_id)
    ex1.delete()
    view_data=admin_adduser_table.objects.all()
    
    return render(request,'admin_users.html',{'view_data':view_data})

#***************admin_vendors*************************
def admin_editvendor(request,row_id):
    
    view_data=admin_add_vendor_table.objects.get(id=row_id)
    return render(request,'admin_editvendor.html',{'view_data':view_data})
def admin_vendor_update_form_submission(request,row_id):
    
    if request.method=="POST":
        ex1=admin_add_vendor_table.objects.filter(id=row_id).update(vendor_name=request.POST.get('vendor_name'),
                            vendor_email=request.POST.get('vendor_email'),
                            vendor_phone=request.POST.get('vendor_phone'),
                            vendor_city=request.POST.get('vendor_city'))
        view_data=admin_add_vendor_table.objects.all()
        messages.error(request,'Vendor Updated Successfully...!',extra_tags='adendor')
        return render(request,'admin_vendors.html',{'view_data':view_data})
    else:
        return render(request,'admin_editvendor.html')     
def admin_vendor_delete(request,row_id):
    ex1=admin_add_vendor_table.objects.get(id=row_id)
    ex1.delete()
    view_data=admin_add_vendor_table.objects.all()
    
    return render(request,'admin_vendors.html',{'view_data':view_data})



def admin_expensecategory(request):
    view_data=admin_addcategory_table.objects.all()

    return render(request,'admin_expensecategory.html',{'view_data':view_data})
def admin_expenselist(request):
    return render(request,'admin_expenselist.html')
def admin_profile(request):
    return render(request,'admin_profile.html')

def admin_tax(request):
    view_data=admin_addtax_table.objects.all()

    return render(request,'admin_tax.html',{'view_data':view_data})
def admin_users(request):
    view_data=admin_adduser_table.objects.all()

    return render(request,'admin_users.html',{'view_data':view_data})

#***************admin_vendors*************************     
def admin_vendors(request):
    view_data=admin_add_vendor_table.objects.all()

    return render(request,'admin_vendors.html',{'view_data':view_data})

#*****************admin_product_list******************

def admin_addproduct(request):

    return render(request,'admin_addproduct.html')
def admin_editproduct(request,row_id):
    
    view_data=admin_add_productlist_table.objects.get(id=row_id)
    return render(request,'admin_editproduct.html',{'view_data':view_data})
def admin_productlist(request):
    view_data=admin_add_productlist_table.objects.all()

    return render(request,'admin_productlist.html',{'view_data':view_data})
def admin_add_product_form_submission(request):

    if request.method=="POST":
        ex1=admin_add_productlist_table(product_name=request.POST.get('product_name'),
                                  product_brand=request.POST.get('product_brand'),
                                  product_unit=request.POST.get('product_unit'),
                                  product_selling_price=request.POST.get('product_selling_price'))
        ex1.save()
        view_data=admin_add_productlist_table.objects.all()
        messages.error(request,'Product Added Successfully...!',extra_tags='adproduct')
        return render(request,'admin_productlist.html',{'view_data':view_data}) 
    else:
        return render(request,'admin_addproduct.html')
def admin_product_update_form_submission(request,row_id):
    
    if request.method=="POST":
        ex1=admin_add_productlist_table.objects.filter(id=row_id).update(product_name=request.POST.get('product_name'),
                                  product_brand=request.POST.get('product_brand'),
                                  product_unit=request.POST.get('product_unit'),
                                  product_selling_price=request.POST.get('product_selling_price'))
        view_data=admin_add_productlist_table.objects.all()
        messages.error(request,'Product Updated Successfully...!',extra_tags='adroduct')
        return render(request,'admin_productlist.html',{'view_data':view_data})
    else:
        return render(request,'admin_editproduct.html')
def admin_product_delete(request,row_id):
    ex1=admin_add_productlist_table.objects.get(id=row_id)
    ex1.delete()
    view_data=admin_add_productlist_table.objects.all()
    
    return render(request,'admin_productlist.html',{'view_data':view_data})                                    
                                        
# ------- Admin_Roles ------- #

def admin_roles(request):
    view_data=admin_add_role_table.objects.all()

    return render(request,'admin_roles.html',{'view_data':view_data})

def admin_addrole(request):

    return render(request,'admin_addrole.html')

def admin_add_role_form_submission(request):

    if request.method=="POST":
        ex1=admin_add_role_table(role_type=request.POST.get('role_type'),
                                profile=request.POST.getlist('profile'),
                                notification=request.POST.getlist('notification'),
                                account=request.POST.getlist('account'))                        
        ex1.save()           
        view_data=admin_add_role_table.objects.all()
        messages.error(request,'Role Added Successfully...!',extra_tags='adrole')             
        return render(request,'admin_roles.html',{'view_data':view_data})
    else:
        return render(request,'admin_addrole.html')        


def admin_editrole(request,row_id):
    
    view_data=admin_add_role_table.objects.get(id=row_id)
    return render(request,'admin_editrole.html',{'view_data':view_data})


def update_admin_role_form_submission(request,row_id):
    
    if request.method=="POST":
        ex1=admin_add_role_table.objects.filter(id=row_id).update(role_type=request.POST.get('role_type'),
                                profile=request.POST.getlist('profile'),
                                notification=request.POST.getlist('notification'),
                                account=request.POST.getlist('account'))
        view_data=admin_add_role_table.objects.all()
        messages.error(request,'Role Updated Successfully...!',extra_tags='adole')
        return render(request,'admin_roles.html',{'view_data':view_data})
    else:
        return render(request,'admin_editrole.html')
def admin_role_delete(request,row_id):
    ex1=admin_add_role_table.objects.get(id=row_id)
    ex1.delete()
    view_data=admin_add_role_table.objects.all()
    
    return render(request,'admin_roles.html',{'view_data':view_data})                                    

# ---------- Admin_Sales ---------- #

def admin_sales(request):
    view_data=admin_add_sale_table.objects.all()

    return render(request,'admin_sales.html',{'view_data':view_data})

def admin_addsale(request):

    return render(request,'admin_addsale.html')

def admin_add_sale_form_submission(request):

    if request.method=="POST":
        ex1=admin_add_sale_table(invoice_id=request.POST.get('invoice_id'),
            date=request.POST.get('date'),
            sold_by=request.POST.get('sold_by'),
            sold_to=request.POST.get('sold_to'),
            items_sold=request.POST.get('items_sold'),
            payment=request.POST.get('payment'))
        ex1.save()
        messages.error(request,'Sale Added Successfully...!',extra_tags='adsale')
        view_data=admin_add_sale_table.objects.all()
        return render(request,'admin_sales.html',{'view_data':view_data})
    else:
        return render(request,'admin_addsale.html')

def admin_editsale(request,row_id):
    
    view_data=admin_add_sale_table.objects.get(id=row_id)
    return render(request,'admin_editsale.html',{'view_data':view_data})

def update_admin_sale_form_submission(request,row_id):
    
    if request.method=="POST":
        ex1=admin_add_sale_table.objects.filter(id=row_id).update(invoice_id=request.POST.get('invoice_id'),
            date=request.POST.get('date'),
            sold_by=request.POST.get('sold_by'),
            sold_to=request.POST.get('sold_to'),
            items_sold=request.POST.get('items_sold'),
            payment=request.POST.get('payment'))
        view_data=admin_add_sale_table.objects.all()
        messages.error(request,'Sale Updated Successfully...!',extra_tags='adale')
        return render(request,'admin_sales.html',{'view_data':view_data})
    else:
        return render(request,'admin_editsale.html')
def admin_sale_delete(request,row_id):
    ex1=admin_add_sale_table.objects.get(id=row_id)
    ex1.delete()
    view_data=admin_add_sale_table.objects.all()
    
    return render(request,'admin_sales.html',{'view_data':view_data})                                    

# ---------- Admin_Return --------- #

def admin_returns(request):
    view_data=admin_add_return_table.objects.all()

    return render(request,'admin_returns.html',{'view_data':view_data})

def admin_addreturn(request):

    return render(request,'admin_addreturn.html')

def admin_add_return_form_submission(request):

    if request.method=="POST":
        ex1=admin_add_return_table(c_name=request.POST.get('c_name'),
            c_email=request.POST.get('c_email'),
            returned_dt=request.POST.get('returned_dt'),
            returned_item=request.POST.get('returned_item'))
        ex1.save()
        messages.error(request,'Return Added Successfully...!',extra_tags='adreturn')
        view_data=admin_add_return_table.objects.all()
        return render(request,'admin_returns.html',{'view_data':view_data})
    else:
        return render(request,'admin_addreturn.html')

def admin_editreturn(request,row_id):
    
    view_data=admin_add_return_table.objects.get(id=row_id)
    return render(request,'admin_editreturn.html',{'view_data':view_data})

def update_admin_return_form_submission(request,row_id):
    
    if request.method=="POST":
        ex1=admin_add_return_table.objects.filter(id=row_id).update(c_name=request.POST.get('c_name'),
            c_email=request.POST.get('c_email'),
            returned_dt=request.POST.get('returned_dt'),
            returned_item=request.POST.get('returned_item'))
        view_data=admin_add_return_table.objects.all()
        messages.error(request,'Return Updated Successfully...!',extra_tags='adeturn')
        return render(request,'admin_returns.html',{'view_data':view_data})
    else:
        return render(request,'admin_editreturn.html')
def admin_return_delete(request,row_id):
    ex1=admin_add_return_table.objects.get(id=row_id)
    ex1.delete()
    view_data=admin_add_return_table.objects.all()
    
    return render(request,'admin_returns.html',{'view_data':view_data})                                    

# ------------- Admin_Stock_Analysis ------------- #

def admin_stockanalysis(request):
    view_data=admin_add_stock_table.objects.all()

    return render(request,'admin_stockanalysis.html',{'view_data':view_data})

def admin_addstock(request):

    return render(request,'admin_addstock.html')

def admin_add_stock_form_submission(request):

    if request.method=="POST":
        ex1=admin_add_stock_table(p_name=request.POST.get('p_name'),
            quantity=request.POST.get('quantity'))
        ex1.save()
        messages.error(request,'Stock Added Successfully...!',extra_tags='adstock')
        view_data=admin_add_stock_table.objects.all()
        return render(request,'admin_stockanalysis.html',{'view_data':view_data})
    else:
        return render(request,'admin_addstock.html')

def admin_editstock(request,row_id):
    
    view_data=admin_add_stock_table.objects.get(id=row_id)
    return render(request,'admin_editstock.html',{'view_data':view_data})

def update_admin_stock_form_submission(request,row_id):
    
    if request.method=="POST":
        ex1=admin_add_stock_table.objects.filter(id=row_id).update(p_name=request.POST.get('p_name'),
            quantity=request.POST.get('quantity'))
        view_data=admin_add_stock_table.objects.all()
        messages.error(request,'Stock Updated Successfully...!',extra_tags='adtock')
        return render(request,'admin_stockanalysis.html',{'view_data':view_data})
    else:
        return render(request,'admin_editstock.html')
def admin_stock_delete(request,row_id):
    ex1=admin_add_stock_table.objects.get(id=row_id)
    ex1.delete()
    view_data=admin_add_stock_table.objects.all()
    
    return render(request,'admin_stockanalysis.html',{'view_data':view_data})                                    

# ----------- Admin_Purchase_Tax_Report ----------- #

def admin_purchasetaxreport(request):
    view_data=admin_add_purchase_tax_table.objects.all()

    return render(request,'admin_purchasetaxreport.html',{'view_data':view_data})

def admin_addpurchasetax(request):

    return render(request,'admin_addpurchasetax.html')

def admin_add_purchase_tax_form_submission(request):

    if request.method=="POST":
        ex1=admin_add_purchase_tax_table(ref_number=request.POST.get('ref_number'),
            date=request.POST.get('date'),
            vendor=request.POST.get('vendor'),
            p_tax=request.POST.get('p_tax'),
            g_tot=request.POST.get('g_tot'))
        ex1.save()
        messages.error(request,'Purchase Tax Added Successfully...!',extra_tags='adpurchase_tax')
        view_data=admin_add_purchase_tax_table.objects.all()
        return render(request,'admin_purchasetaxreport.html',{'view_data':view_data})
    else:
        return render(request,'admin_addpurchasetax.html')

def admin_editpurchasetax(request,row_id):
    
    view_data=admin_add_purchase_tax_table.objects.get(id=row_id)
    return render(request,'admin_editpurchasetax.html',{'view_data':view_data})

def update_admin_purchase_tax_form_submission(request,row_id):
    
    if request.method=="POST":
        ex1=admin_add_purchase_tax_table.objects.filter(id=row_id).update(ref_number=request.POST.get('ref_number'),
            date=request.POST.get('date'),
            vendor=request.POST.get('vendor'),
            p_tax=request.POST.get('p_tax'),
            g_tot=request.POST.get('g_tot'))
        view_data=admin_add_purchase_tax_table.objects.all()
        messages.error(request,'Purchase Tax Updated Successfully...!',extra_tags='adurchase_tax')
        return render(request,'admin_purchasetaxreport.html',{'view_data':view_data})
    else:
        return render(request,'admin_editpurchasetax.html')
def admin_purchase_tax_delete(request,row_id):
    ex1=admin_add_purchase_tax_table.objects.get(id=row_id)
    ex1.delete()
    view_data=admin_add_purchase_tax_table.objects.all()
    
    return render(request,'admin_purchasetaxreport.html',{'view_data':view_data}) 
    

# ---------- Admin_Expense_Report ------------ #

def admin_expensereport(request):
    view_data=admin_add_expense_report_table.objects.all()

    return render(request,'admin_expensereport.html',{'view_data':view_data})

def admin_addexpensereport(request):

    return render(request,'admin_addexpensereport.html')

def admin_add_expense_report_form_submission(request):

    if request.method=="POST":
        ex1=admin_add_expense_report_table(date=request.POST.get('date'),
            exp_category=request.POST.get('exp_category'),
            note=request.POST.get('note'),
            created_by=request.POST.get('created_by'))
        ex1.save()
        messages.error(request,'Expense Report Added Successfully...!',extra_tags='adexpense_report')
        view_data=admin_add_expense_report_table.objects.all()
        return render(request,'admin_expensereport.html',{'view_data':view_data})
    else:
        return render(request,'admin_addexpensereport.html')

def admin_editexpensereport(request,row_id):
    
    view_data=admin_add_expense_report_table.objects.get(id=row_id)
    return render(request,'admin_editexpensereport.html',{'view_data':view_data})

def update_admin_expense_report_form_submission(request,row_id):
    
    if request.method=="POST":
        ex1=admin_add_expense_report_table.objects.filter(id=row_id).update(date=request.POST.get('date'),
            exp_category=request.POST.get('exp_category'),
            note=request.POST.get('note'),
            created_by=request.POST.get('created_by'))
        view_data=admin_add_expense_report_table.objects.all()
        messages.error(request,'Expense Report Updated Successfully...!',extra_tags='adxpense_report')
        return render(request,'admin_expensereport.html',{'view_data':view_data})
    else:
        return render(request,'admin_editexpensereport.html')
def admin_expense_report_delete(request,row_id):
    ex1=admin_add_expense_report_table.objects.get(id=row_id)
    ex1.delete()
    view_data=admin_add_expense_report_table.objects.all()
    
    return render(request,'admin_expensereport.html',{'view_data':view_data}) 

# --------- Admin_Customer_Report --------- #

def admin_customerreport(request):
    view_data=admin_add_customer_report_table.objects.all()

    return render(request,'admin_customerreport.html',{'view_data':view_data})

def admin_addcustomerreport(request):

    return render(request,'admin_addcustomerreport.html')

def admin_add_customer_report_form_submission(request):

    if request.method=="POST":
        ex1=admin_add_customer_report_table(name=request.POST.get('name'),
            phone_number=request.POST.get('phone_number'),
            email=request.POST.get('email'),
            tot_sales=request.POST.get('tot_sales'),
            tot_amt=request.POST.get('tot_amt'))
        ex1.save()
        messages.error(request,'Customer Report Added Successfully...!',extra_tags='adcustomer_report')
        view_data=admin_add_customer_report_table.objects.all()
        return render(request,'admin_customerreport.html',{'view_data':view_data})
    else:
        return render(request,'admin_addcustomerreport.html')

def admin_editcustomerreport(request,row_id):
    
    view_data=admin_add_customer_report_table.objects.get(id=row_id)
    return render(request,'admin_editcustomerreport.html',{'view_data':view_data})

def update_admin_customer_report_form_submission(request,row_id):
    
    if request.method=="POST":
        ex1=admin_add_customer_report_table.objects.filter(id=row_id).update(name=request.POST.get('name'),
            phone_number=request.POST.get('phone_number'),
            email=request.POST.get('email'),
            tot_sales=request.POST.get('tot_sales'),
            tot_amt=request.POST.get('tot_amt'))
        view_data=admin_add_customer_report_table.objects.all()
        messages.error(request,'Customer Report Updated Successfully...!',extra_tags='adustomer_report')
        return render(request,'admin_customerreport.html',{'view_data':view_data})
    else:
        return render(request,'admin_editcustomerreport.html')
def admin_customer_report_delete(request,row_id):
    ex1=admin_add_customer_report_table.objects.get(id=row_id)
    ex1.delete()
    view_data=admin_add_customer_report_table.objects.all()
    
    return render(request,'admin_customerreport.html',{'view_data':view_data}) 

# ---------- Admin_Quotation ------------ #

def admin_quotations(request):
    view_data=admin_add_quotation_table.objects.all()

    return render(request,'admin_quotations.html',{'view_data':view_data})

def admin_addquotation(request):

    return render(request,'admin_addquotation.html')

def admin_add_quotation_form_submission(request):

    if request.method=="POST":
        ex1=admin_add_quotation_table(date=request.POST.get('date'),
            ref_number=request.POST.get('ref_number'),
            customer=request.POST.get('customer'),
            customer_email=request.POST.get('customer_email'),
            g_total=request.POST.get('g_total'),
            quo_note=request.POST.get('quo_note'))
        ex1.save()
        messages.error(request,'Quotation Added Successfully...!',extra_tags='adquotation')
        view_data=admin_add_quotation_table.objects.all()
        return render(request,'admin_quotations.html',{'view_data':view_data})
    else:
        return render(request,'admin_addquotation.html')

def admin_editquotation(request,row_id):
    
    view_data=admin_add_quotation_table.objects.get(id=row_id)
    return render(request,'admin_editquotation.html',{'view_data':view_data})

def update_admin_quotation_form_submission(request,row_id):
    
    if request.method=="POST":
        ex1=admin_add_quotation_table.objects.filter(id=row_id).update(date=request.POST.get('date'),
            ref_number=request.POST.get('ref_number'),
            customer=request.POST.get('customer'),
            customer_email=request.POST.get('customer_email'),
            g_total=request.POST.get('g_total'),
            quo_note=request.POST.get('quo_note'))
        view_data=admin_add_quotation_table.objects.all()
        messages.error(request,'Quotation Updated Successfully...!',extra_tags='aduotation')
        return render(request,'admin_quotations.html',{'view_data':view_data})
    else:
        return render(request,'admin_editquotation.html')
def admin_quotation_delete(request,row_id):
    ex1=admin_add_quotation_table.objects.get(id=row_id)
    ex1.delete()
    view_data=admin_add_quotation_table.objects.all()
    
    return render(request,'admin_quotations.html',{'view_data':view_data}) 

# ---------- Admin_Expense_List ------------ #

def admin_expenselist(request):
    view_data=admin_add_expense_list_table.objects.all()

    return render(request,'admin_expenselist.html',{'view_data':view_data})

def admin_addexpense(request):

    return render(request,'admin_addexpense.html')

def admin_add_expense_list_form_submission(request):

    if request.method=="POST":
        ex1=admin_add_expense_list_table(branch=request.POST.get('branch'),
            exp_date=request.POST.get('exp_date'),
            exp_category=request.POST.get('exp_category'),
            amount=request.POST.get('amount'),
            note=request.POST.get('note'))
        ex1.save()
        messages.error(request,'Expense List Added Successfully...!',extra_tags='adexpense_list')
        view_data=admin_add_expense_list_table.objects.all()
        return render(request,'admin_expenselist.html',{'view_data':view_data})
    else:
        return render(request,'admin_addexpense.html')

def admin_editexpense(request,row_id):
    
    view_data=admin_add_expense_list_table.objects.get(id=row_id)
    return render(request,'admin_editexpense.html',{'view_data':view_data})

def update_admin_expense_list_form_submission(request,row_id):
    
    if request.method=="POST":
        ex1=admin_add_expense_list_table.objects.filter(id=row_id).update(branch=request.POST.get('branch'),
            exp_date=request.POST.get('exp_date'),
            exp_category=request.POST.get('exp_category'),
            amount=request.POST.get('amount'),
            note=request.POST.get('note'))
        view_data=admin_add_expense_list_table.objects.all()
        messages.error(request,'Expense List Updated Successfully...!',extra_tags='adxpense_list')
        return render(request,'admin_expenselist.html',{'view_data':view_data})
    else:
        return render(request,'admin_editexpense.html')
def admin_expense_list_delete(request,row_id):
    ex1=admin_add_expense_list_table.objects.get(id=row_id)
    ex1.delete()
    view_data=admin_add_expense_list_table.objects.all()
    
    return render(request,'admin_expenselist.html',{'view_data':view_data})

def admin_compose(request):
    return render(request,'admin_compose.html')
def admin_viewmail(request):
    return render(request,'admin_viewmail.html')
def admin_inbox(request):
    return render(request,'admin_inbox.html')

# views counting #
# -------------- #

def  index(request):
    num_visits=request.session.get('num_visits',0)
    request.session['num_visits']=num_visits + 1
    context={'num_visits':num_visits }
    return render(request,'index.html',context=context)
