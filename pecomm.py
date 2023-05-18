## import libraries
import pandas as pd
import streamlit as st
import pickle
import numpy as np
from datetime import datetime

model=pickle.load(open(r"C:\PROJECT\BIA\Thane branch 2 Capstone project\ECom\ecom 3 - Vicky Dalvi\rf_model_updated.pkl",'rb'))     ## Load pickeled ml model

## Main Function
def main():
    """ main() contains all UI structure elements; getting and storing user data can be done within it"""
    st.title("Price Prediction")                                                                              ## Title/main heading
    
    ## Side Bar Configurations
    st.sidebar.header("More Details:")
    st.title("-----          Check Your Price-----")

    ## Framing UI Structure
    discount = st.slider("discount :", 1, 1000, 30)                                                                  # slider for user input(ranges from 1 to 75 & default 30)

    quantity = st.slider("Quantity :", 1, 50, 1)                                                        # slider for user input(ranges from 15 to 500 & default 40)

    Year = st.selectbox("Year?", [2015,2016,2017,2018,2019,2020]) # Select box
    
    Month = st.selectbox("Month?", [1,2,3,4,5,6,7,8,9,10,11,12])
    

    categories = st.selectbox("Select Category:", ['Beauty & Grooming', 'Books','Computing', 'Entertainment','Health & Sports', 'Home & Living','Kids & Baby', 'Mens Fashion','Mobiles & Tablets', 'Others','School & Education', 'Soghaat','Superstore', 'Womens Fashion'])                         # select box for gender[Male|Female]
    category_name_1_Beauty_Grooming = 0
    category_name_1_Books = 0
    category_name_1_Computing = 0
    category_name_1_Entertainment = 0
    category_name_1_Health___Sports = 0
    category_name_1_Home___Living = 0
    category_name_1_Kids___Baby = 0
    category_name_1_Mens_Fashion = 0
    category_name_1_Mobiles___Tablets = 0
    category_name_1_Others = 0
    category_name_1_School___Education = 0    
    category_name_1_Soghaat = 0    
    category_name_1_Superstore = 0  
    category_name_1_Womens_Fashion = 0    
        
    if (categories == 'Beauty & Grooming'):                                                             # selected gender changes to [Male:0 Female:1]
        category_name_1_Beauty_Grooming = 1
    elif (categories == 'Books'):
        category_name_1_Books = 1
    elif categories == 'Computing':
        category_name_1_Computing = 1
    elif categories == 'Entertainment':
        category_name_1_Entertainment = 1
    elif categories == 'Health & Sports':
        category_name_1_Health___Sports = 1
    elif categories == 'Home & Living':
        category_name_1_Home___Living = 1
    elif categories == 'Kids & Baby':
        category_name_1_Kids___Baby = 1
    elif categories == 'Mens Fashion':
        category_name_1_Mens_Fashion = 1
    elif categories == 'Mobiles & Tablets':
        category_name_1_Mobiles___Tablets = 1
    elif categories == 'Others':
        category_name_1_Others = 1
    elif categories == 'School & Education':
        category_name_1_School___Education = 1    
    elif categories == 'Soghaat':
        category_name_1_Soghaat = 1    
    elif categories == 'Superstore':
        category_name_1_Superstore = 1  
    elif categories == 'Womens Fashion':
        category_name_1_Womens_Fashion = 1    
      
    payment_type = st.selectbox("Select Category:", ['cod', 'others', 'customercredit', 'Payaxis', 'jazzvoucher','jazzwallet', 'Easypay', 'Easypay_MA', 'easypay_voucher','bankalfalah'])                         # select box for gender[Male|Female]
    payment_method_cod = 0
    payment_method_others = 0
    payment_method_customercredit = 0
    payment_method_Payaxis = 0
    payment_method_jazzvoucher = 0
    payment_method_jazzwallet = 0
    payment_method_others = 0
    payment_method_Easypay_MA = 0
    payment_method_easypay_voucher = 0
    payment_method_bankalfalah = 0  
    
    if (payment_type == 'cod'):                                                             # selected Payment tpye
        payment_method_cod = 1
    elif payment_type == 'others':
        payment_method_others = 1
    elif payment_type == 'customercredit':
        payment_method_customercredit = 1
    elif payment_type == 'Payaxis':
        payment_method_Payaxis = 1
    elif payment_type == 'jazzvoucher':
        payment_method_jazzvoucher = 1
    elif payment_type == 'jazzwallet':
        payment_method_jazzwallet = 1
    elif payment_type == 'Easypay':
        payment_method_others = 1
    elif payment_type == 'Easypay_MA':
        payment_method_Easypay_MA = 1
    elif payment_type == 'easypay_voucher':
        payment_method_easypay_voucher = 1
    elif payment_type == 'bankalfalah':
        payment_method_bankalfalah = 1  
        
    FY_Year = st.selectbox("FY Year?", [2017,2018,2019])
    FY_FY18 = FY_FY19 = FY_FY17 = 0
    
    if FY_Year == 2018:
        FY_FY18 = 1
    elif FY_FY19 == 2019:
        FY_FY19 = 1
    else:
        FY_FY17 = 1

    # Create a date input for selecting month and year
    selected_date = st.date_input("Select a date", datetime.now())

    # Extract the year and month from the selected date
    selected_year = selected_date.year
    selected_month = selected_date.month
    Customer_Since_2016_7 = 0
    Customer_Since_2016_8 = 0
    Customer_Since_2016_9 = 0
    Customer_Since_2016_10 = 0
    Customer_Since_2016_11 = 0
    Customer_Since_2016_12 = 0
    Customer_Since_2017_1 = 0
    Customer_Since_2017_2 = 0
    Customer_Since_2017_3 = 0
    Customer_Since_2017_4 = 0
    Customer_Since_2017_5 = 0
    Customer_Since_2017_6 = 0
    Customer_Since_2017_7 = 0
    Customer_Since_2017_8 = 0
    Customer_Since_2017_9 = 0
    Customer_Since_2017_10 = 0
    Customer_Since_2017_11 = 0
    Customer_Since_2017_12 = 0
    Customer_Since_2018_1 = 0
    Customer_Since_2018_2 = 0 
    Customer_Since_2018_3 = 0
    Customer_Since_2018_4 = 0  
    Customer_Since_2018_5 = 0
    Customer_Since_2018_6 = 0
    Customer_Since_2018_7 = 0    
    Customer_Since_2018_8 = 0
    
    if (selected_month == 7) and (selected_year == 2016):
        Customer_Since_2016_7 = 1
    elif(selected_month == 8) and (selected_year == 2016):
        Customer_Since_2016_8 = 1
    elif(selected_month == 9) and (selected_year == 2016):
        Customer_Since_2016_9 = 1
    elif(selected_month == 10) and (selected_year == 2016):
        Customer_Since_2016_10 = 1
    elif(selected_month == 11) and (selected_year == 2016):
        Customer_Since_2016_11 = 1
    elif(selected_month == 12) and (selected_year == 2016):
        Customer_Since_2016_12 = 1
    elif(selected_month == 1) and (selected_year == 2017):
        Customer_Since_2017_1 = 1
    elif(selected_month == 2) and (selected_year == 2017):
        Customer_Since_2017_2 = 1
    elif(selected_month == 3) and (selected_year == 2017):
        Customer_Since_2017_3 = 1
    elif(selected_month == 4) and (selected_year == 2017):
        Customer_Since_2017_4 = 1
    elif(selected_month == 5) and (selected_year == 2017):
        Customer_Since_2017_5 = 1
    elif(selected_month == 6) and (selected_year == 2017):
        Customer_Since_2017_6 = 1
    elif(selected_month == 7) and (selected_year == 2017):
        Customer_Since_2017_7 = 1
    elif(selected_month == 8) and (selected_year == 2017):
        Customer_Since_2017_8 = 1
    elif(selected_month == 9) and (selected_year == 2017):
        Customer_Since_2017_9 = 1
    elif(selected_month == 10) and (selected_year == 2017):
        Customer_Since_2017_10 = 1
    elif(selected_month == 11) and (selected_year == 2017):
        Customer_Since_2017_11 = 1
    elif(selected_month == 12) and (selected_year == 2017):
        Customer_Since_2017_12 = 1
    elif(selected_month == 1) and (selected_year == 2018):
        Customer_Since_2018_1 = 1
    elif(selected_month == 2) and (selected_year == 2018):
        Customer_Since_2018_2 = 1
    elif(selected_month == 3) and (selected_year == 2018):
        Customer_Since_2018_3 = 1
    elif(selected_month == 4) and (selected_year == 2018):
        Customer_Since_2018_4 = 1
    elif(selected_month == 5) and (selected_year == 2018):
        Customer_Since_2018_5 = 1
    elif(selected_month == 6) and (selected_year == 2018):
        Customer_Since_2018_6 = 1
    elif(selected_month == 7) and (selected_year == 2018):
        Customer_Since_2018_7 = 1
    elif(selected_month == 8) and (selected_year == 2018):
        Customer_Since_2018_8 = 1


    
    ## Getting & Framing Data: Collecting user-input into dictionary
    data={"qty_ordered":quantity,"discount_amount":discount,"Year":Year,"Month":Month,
            'category_name_1_Beauty___Grooming'	:	category_name_1_Beauty_Grooming 	,
            'category_name_1_Books'	:	category_name_1_Books	,
            'category_name_1_Computing' 	:	category_name_1_Computing 	,
            'category_name_1_Entertainment'	:	category_name_1_Entertainment	,
            'category_name_1_Health___Sports' 	:	category_name_1_Health___Sports 	,
            'category_name_1_Home___Living'	:	category_name_1_Home___Living	,
            'category_name_1_Kids___Baby'	:	category_name_1_Kids___Baby 	,
            'category_name_1_Mens_Fashion'	:	category_name_1_Mens_Fashion	,
            'category_name_1_Mobiles___Tablets' 	:	category_name_1_Mobiles___Tablets 	,
            'category_name_1_Others'	:	category_name_1_Others	,
            'category_name_1_School___Education' 	:	category_name_1_School___Education 	,
            'category_name_1_Soghaat'	:	category_name_1_Soghaat	,
            'category_name_1_Superstore' 	:	category_name_1_Superstore 	,
            'category_name_1_Womens_Fashion'	:	category_name_1_Womens_Fashion	,
            'Customer_Since_2016_11'	:	Customer_Since_2016_11 	,
            'Customer_Since_2016_12'	:	Customer_Since_2016_12	,
            'Customer_Since_2016_7' 	:	Customer_Since_2016_7 	,
            'Customer_Since_2016_8'	:	Customer_Since_2016_8	,
            'Customer_Since_2016_9' 	:	Customer_Since_2016_9 	,
            'Customer_Since_2017_1'	:	Customer_Since_2017_1	,
            'Customer_Since_2017_10' 	:	Customer_Since_2017_10 	,
            'Customer_Since_2017_11'	:	Customer_Since_2017_11	,
            'Customer_Since_2017_12' 	:	Customer_Since_2017_12 	,
            'Customer_Since_2017_2'	:	Customer_Since_2017_2	,
            'Customer_Since_2017_3' 	:	Customer_Since_2017_3 	,
            'Customer_Since_2017_4'	:	Customer_Since_2017_4	,
            'Customer_Since_2017_5' 	:	Customer_Since_2017_5 	,
            'Customer_Since_2017_6'	:	Customer_Since_2017_6	,
            'Customer_Since_2017_7' 	:	Customer_Since_2017_7 	,
            'Customer_Since_2017_8'	:	Customer_Since_2017_8	,
            'Customer_Since_2017_9' 	:	Customer_Since_2017_9 	,
            'Customer_Since_2018_1'	:	Customer_Since_2018_1	,
            'Customer_Since_2018_2' 	:	Customer_Since_2018_2 	,
            'Customer_Since_2018_3'	:	Customer_Since_2018_3	,
            'Customer_Since_2018_4' 	:	Customer_Since_2018_4 	,
            'Customer_Since_2018_5'	:	Customer_Since_2018_5	,
            'Customer_Since_2018_6' 	:	Customer_Since_2018_6 	,
            'Customer_Since_2018_7'	:	Customer_Since_2018_7	,
            'Customer_Since_2018_8' 	:	Customer_Since_2018_8 	,
            'payment_method_Easypay_MA'	:	payment_method_Easypay_MA	,
            'payment_method_Payaxis' 	:	payment_method_Payaxis 	,
            'payment_method_bankalfalah'	:	payment_method_bankalfalah	,
            'payment_method_cod' 	:	payment_method_cod 	,
            'payment_method_customercredit'	:	payment_method_customercredit	,
            'payment_method_easypay_voucher' 	:	payment_method_easypay_voucher 	,
            'payment_method_jazzvoucher'	:	payment_method_jazzvoucher	,
            'payment_method_jazzwallet' 	:	payment_method_jazzwallet 	,
            'payment_method_others' 	:	payment_method_others 	,
            'FY_FY18'	:	FY_FY18	,
            'FY_FY19'	:	FY_FY19        
        }

    df=pd.DataFrame(data,index=[0])      ## converting dictionary to Dataframe
    return df

data=main()                             ## calling Main()

## Prediction:
if st.button("Predict"):                                                                ## prediction button created,which returns predicted value from ml model(pickle file)
    result = model.predict(data)                                                    ## probabilty prediction of user-input
    #st.success('The output is {}'.format(result))

    st.write("**The price is  :** : {}".format(result))
   

## Author Info.
if st.button("Author"):
    st.write("## @ Vicky")