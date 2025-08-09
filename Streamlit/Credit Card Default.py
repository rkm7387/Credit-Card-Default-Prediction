import numpy as np
import pandas as pd
import streamlit as st
import pickle
import warnings
warnings.filterwarnings('ignore')


# loading the saved model

with open(r'D:\ML-DL PROJECTS\Credit Card Default Prediction\eda+modelling\trained_model_credit.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

limit_bal = 0
sex = 0
age = 0
bill_amt_sept = 0
bill_amt_aug = 0
bill_amt_jul = 0
bill_amt_jun = 0
bill_amt_may = 0
bill_amt_apr = 0
pay_amt_sept = 0
pay_amt_aug = 0
pay_amt_jul = 0
pay_amt_jun = 0
pay_amt_may = 0
pay_amt_apr = 0
education_Graduate_School = 0
education_High_School = 0
education_University = 0
marriage_Married = 0
marriage_Single = 0
pay_sept_1_ = 0
pay_sept_0 = 0
pay_sept_1 = 0
pay_sept_2 = 0
pay_sept_3 = 0
pay_sept_4 = 0
pay_sept_5 = 0
pay_sept_6 = 0
pay_sept_7 = 0
pay_sept_8 = 0
pay_aug_1_ = 0
pay_aug_0 = 0
pay_aug_1 = 0
pay_aug_2 = 0
pay_aug_3 = 0
pay_aug_4 = 0
pay_aug_5 = 0
pay_aug_6 = 0
pay_aug_7 = 0
pay_aug_8 = 0
pay_jul_1_ = 0
pay_jul_0 = 0
pay_jul_1 = 0
pay_jul_2 = 0
pay_jul_3 = 0
pay_jul_4 = 0
pay_jul_5 = 0
pay_jul_6 = 0
pay_jul_7 = 0
pay_jul_8 = 0
pay_jun_1_ = 0
pay_jun_0 = 0
pay_jun_1 = 0
pay_jun_2 = 0
pay_jun_3 = 0
pay_jun_4 = 0
pay_jun_5 = 0
pay_jun_6 = 0
pay_jun_7 = 0
pay_jun_8 = 0
pay_may_1_ = 0
pay_may_0 = 0
pay_may_1 = 0
pay_may_2 = 0
pay_may_3 = 0
pay_may_4 = 0
pay_may_5 = 0
pay_may_6 = 0
pay_may_7 = 0
pay_may_8 = 0
pay_apr_1_ = 0
pay_apr_0 = 0
pay_apr_1 = 0
pay_apr_2 = 0
pay_apr_3 = 0
pay_apr_4 = 0
pay_apr_5 = 0
pay_apr_6 = 0
pay_apr_7 = 0
pay_apr_8 = 0


def credit_card(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)

    if (prediction[0] == 0):
        return st.success('Customer will result in Default')
    else:
        return st.error('Customer will not result in Default')


def main():

    # giving a title
    st.title('Credit Card Default Prediction')

    # getting the input data from the user
    limit_bal = st.text_input('Amount of given credit in NT dollars')
    sex = st.radio('Select whether male or female', ('1', '0'))
    if (sex == '1'):
        st.info("Male")
    else:
        st.info("Female")
    age = st.text_input('Age in years')
    bill_amt_sept = st.text_input(
        'Amount of bill statement in September, 2005 (NT dollar)')
    bill_amt_aug = st.text_input(
        'Amount of bill statement in August, 2005 (NT dollar)')
    bill_amt_jul = st.text_input(
        'Amount of bill statement in July, 2005 (NT dollar)')
    bill_amt_jun = st.text_input(
        'Amount of bill statement in June, 2005 (NT dollar)')
    bill_amt_may = st.text_input(
        'Amount of bill statement in May, 2005 (NT dollar)')
    bill_amt_apr = st.text_input(
        'Amount of bill statement in April, 2005 (NT dollar)')
    pay_amt_sept = st.text_input('Repayment status in September, 2005')
    pay_amt_aug = st.text_input('Repayment status in August, 2005')
    pay_amt_jul = st.text_input('Repayment status in July, 2005')
    pay_amt_jun = st.text_input('Repayment status in June, 2005')
    pay_amt_may = st.text_input('Repayment status in May, 2005')
    pay_amt_apr = st.text_input('Repayment status in April, 2005')
    education_Graduate_School = st.radio(
        "Education", ("0 = Graduate", "1 = High School", "2 = University"))
    if (education_Graduate_School == "0 = Graduate"):
        education_Graduate_School = 1
        education_High_School = 0
        education_University = 0

    if (education_Graduate_School == "1 = High School"):
        education_Graduate_School = 0
        education_High_School = 1
        education_University = 0

    if (education_Graduate_School == "2 = Graduate"):
        education_Graduate_School = 0
        education_High_School = 0
        education_University = 1

    marriage_Married = st.radio(
        'Marriage Status', ("0 = Married", "1 = Un-Married"))
    if (marriage_Married == "0 = Married"):
        marriage_Married = 1
        marriage_Single = 0
    else:
        marriage_Married = 0
        marriage_Single = 1

    pay_sept_1_ = st.radio("Repayment Status September",
                                                        ("0 = paypal",
                                                        "1 = payment delay for one month",
                                                        "2 = payment delay for 2 months",
                                                        "3 = payment delay for 3 months",
                                                        "4 = payment delay for 4 months",
                                                        "5 = payment delay for 5 months", 
                                                        "6 = payment delay for 6 months",
                                                        "7 = payment delay for 7 months",
                                                        "8 = payment delay for 8 months"))
    if (pay_sept_1_ == "0 = paypal"):
        pay_sept_1_ = 1
        pay_sept_0 = 0
        pay_sept_2 = 0
        pay_sept_3 = 0
        pay_sept_4 = 0
        pay_sept_5 = 0
        pay_sept_6 = 0
        pay_sept_7 = 0
        pay_sept_8 = 0

    if (pay_sept_1_ == "1 = payment delay for one month"):
        pay_sept_1_ = 0
        pay_sept_0 = 1
        pay_sept_1 = 0
        pay_sept_2 = 0
        pay_sept_3 = 0
        pay_sept_4 = 0
        pay_sept_5 = 0
        pay_sept_6 = 0
        pay_sept_7 = 0
        pay_sept_8 = 0

    if (pay_sept_1_ == "2 = payment delay for 2 months"):
        pay_sept_1_ = 0
        pay_sept_0 = 0
        pay_sept_1 = 0
        pay_sept_2 = 1
        pay_sept_3 = 0
        pay_sept_4 = 0
        pay_sept_5 = 0
        pay_sept_6 = 0
        pay_sept_7 = 0
        pay_sept_8 = 0

    if (pay_sept_1_ == "3 = payment delay for 3 months"):
        pay_sept_1_ = 0
        pay_sept_0 = 0
        pay_sept_1 = 0
        pay_sept_2 = 0
        pay_sept_3 = 1
        pay_sept_4 = 0
        pay_sept_5 = 0
        pay_sept_6 = 0
        pay_sept_7 = 0
        pay_sept_8 = 0

    if (pay_sept_1_ == "4 = payment delay for 4 months"):
        pay_sept_1_ = 0
        pay_sept_0 = 0
        pay_sept_1 = 0
        pay_sept_2 = 0
        pay_sept_3 = 0
        pay_sept_4 = 1
        pay_sept_5 = 0
        pay_sept_6 = 0
        pay_sept_7 = 0
        pay_sept_8 = 0

    if (pay_sept_1_ == "5 = payment delay for 5 months"):
        pay_sept_1_ = 0
        pay_sept_0 = 0
        pay_sept_1 = 0
        pay_sept_2 = 0
        pay_sept_3 = 0
        pay_sept_4 = 0
        pay_sept_5 = 1
        pay_sept_6 = 0
        pay_sept_7 = 0
        pay_sept_8 = 0

    if (pay_sept_1_ == "6 = payment delay for 6 months"):
        pay_sept_1_ = 0
        pay_sept_0 = 0
        pay_sept_1 = 0
        pay_sept_2 = 0
        pay_sept_3 = 0
        pay_sept_4 = 0
        pay_sept_5 = 0
        pay_sept_6 = 1
        pay_sept_7 = 0
        pay_sept_8 = 0

    if (pay_sept_1_ == "7 = payment delay for 7 months"):
        pay_sept_1_ = 0
        pay_sept_0 = 0
        pay_sept_1 = 0
        pay_sept_2 = 0
        pay_sept_3 = 0
        pay_sept_4 = 0
        pay_sept_5 = 0
        pay_sept_6 = 0
        pay_sept_7 = 1
        pay_sept_8 = 0

    if (pay_sept_1_ == "8 = payment delay for 8 months"):
        pay_sept_1_ = 0
        pay_sept_0 = 0
        pay_sept_1 = 0
        pay_sept_2 = 0
        pay_sept_3 = 0
        pay_sept_4 = 0
        pay_sept_5 = 0
        pay_sept_6 = 0
        pay_sept_7 = 0
        pay_sept_8 = 1

    pay_aug_1_ = st.radio("Repayment Status August",
                          ("0 = paypal", "1 = payment delay for one month", "2 = payment delay for 2 months",
                           "3 = payment delay for 3 months", "4 = payment delay for 4 months",
                           "5 = payment delay for 5 months", "6 = payment delay for 6 months",
                           "7 = payment delay for 7 months", "8 = payment delay for 8 months"))
    if (pay_aug_1_ == "0 = paypal"):
        pay_aug_1_ = 1
        pay_aug_0 = 0
        pay_aug_1 = 0
        pay_aug_2 = 0
        pay_aug_3 = 0
        pay_aug_4 = 0
        pay_aug_5 = 0
        pay_aug_6 = 0
        pay_aug_7 = 0
        pay_aug_8 = 0

    if (pay_aug_1_ == "1 = payment delay for one months"):
        pay_aug_1_ = 0
        pay_aug_0 = 1
        pay_aug_1 = 0
        pay_aug_2 = 0
        pay_aug_3 = 0
        pay_aug_4 = 0
        pay_aug_5 = 0
        pay_aug_6 = 0
        pay_aug_7 = 0
        pay_aug_8 = 0

    if (pay_aug_1_ == "2 = payment delay for 2 months"):
        pay_aug_1_ = 0
        pay_aug_0 = 0
        pay_aug_1 = 0
        pay_aug_2 = 1
        pay_aug_3 = 0
        pay_aug_4 = 0
        pay_aug_5 = 0
        pay_aug_6 = 0
        pay_aug_7 = 0
        pay_aug_8 = 0

    if (pay_aug_1_ == "3 = payment delay for 3 months"):
        pay_aug_1_ = 0
        pay_aug_0 = 0
        pay_aug_1 = 0
        pay_aug_2 = 0
        pay_aug_3 = 1
        pay_aug_4 = 0
        pay_aug_5 = 0
        pay_aug_6 = 0
        pay_aug_7 = 0
        pay_aug_8 = 0

    if (pay_aug_1_ == "4 = payment delay for 4 months"):
        pay_aug_1_ = 0
        pay_aug_0 = 0
        pay_aug_1 = 0
        pay_aug_2 = 0
        pay_aug_3 = 0
        pay_aug_4 = 1
        pay_aug_5 = 0
        pay_aug_6 = 0
        pay_aug_7 = 0
        pay_aug_8 = 0

    if (pay_aug_1_ == "5 = payment delay for 5 months"):
        pay_aug_1_ = 0
        pay_aug_0 = 0
        pay_aug_1 = 0
        pay_aug_2 = 0
        pay_aug_3 = 0
        pay_aug_4 = 0
        pay_aug_5 = 1
        pay_aug_6 = 0
        pay_aug_7 = 0
        pay_aug_8 = 0

    if (pay_aug_1_ == "6 = payment delay for 6 months"):
        pay_aug_1_ = 0
        pay_aug_0 = 0
        pay_aug_1 = 0
        pay_aug_2 = 0
        pay_aug_3 = 0
        pay_aug_4 = 0
        pay_aug_5 = 0
        pay_aug_6 = 1
        pay_aug_7 = 0
        pay_aug_8 = 0

    if (pay_aug_1_ == "7 = payment delay for 7 months"):
        pay_aug_1_ = 0
        pay_aug_0 = 0
        pay_aug_1 = 0
        pay_aug_2 = 0
        pay_aug_3 = 0
        pay_aug_4 = 0
        pay_aug_5 = 0
        pay_aug_6 = 0
        pay_aug_7 = 1
        pay_aug_8 = 0

    if (pay_aug_1_ == "8 = payment delay for 8 months"):
        pay_aug_1_ = 0
        pay_aug_0 = 0
        pay_aug_1 = 0
        pay_aug_2 = 0
        pay_aug_3 = 0
        pay_aug_4 = 0
        pay_aug_5 = 0
        pay_aug_6 = 0
        pay_aug_7 = 0
        pay_aug_8 = 1

    pay_jul_1_ = st.radio("Repayment Status July",
                          ("0 = paypal", "1 = payment delay for one month", "2 = payment delay for 2 months",
                           "3 = payment delay for 3 months", "4 = payment delay for 4 months",
                           "5 = payment delay for 5 months", "6 = payment delay for 6 months",
                           "7 = payment delay for 7 months", "8 = payment delay for 8 months"))
    if (pay_jul_1_ == "0 = paypal"):
        pay_jul_1_ = 1
        pay_jul_0 = 0
        pay_jul_2 = 0
        pay_jul_3 = 0
        pay_jul_4 = 0
        pay_jul_5 = 0
        pay_jul_6 = 0
        pay_jul_7 = 0
        pay_jul_8 = 0

    if (pay_jul_1_ == "1 = payment delay for one month"):
        pay_jul_1_ = 0
        pay_jul_0 = 1
        pay_jul_2 = 0
        pay_jul_3 = 0
        pay_jul_4 = 0
        pay_jul_5 = 0
        pay_jul_6 = 0
        pay_jul_7 = 0
        pay_jul_8 = 0

    if (pay_jul_1_ == "2 = payment delay for 2 months"):
        pay_jul_1_ = 0
        pay_jul_0 = 0
        pay_jul_2 = 1
        pay_jul_3 = 0
        pay_jul_4 = 0
        pay_jul_5 = 0
        pay_jul_6 = 0
        pay_jul_7 = 0
        pay_jul_8 = 0

    if (pay_jul_1_ == "3 = payment delay for 3 months"):
        pay_jul_1_ = 0
        pay_jul_0 = 0
        pay_jul_2 = 0
        pay_jul_3 = 1
        pay_jul_4 = 0
        pay_jul_5 = 0
        pay_jul_6 = 0
        pay_jul_7 = 0
        pay_jul_8 = 0

    if (pay_jul_1_ == "4 = payment delay for 4 months"):
        pay_jul_1_ = 0
        pay_jul_0 = 0
        pay_jul_2 = 0
        pay_jul_3 = 0
        pay_jul_4 = 1
        pay_jul_5 = 0
        pay_jul_6 = 0
        pay_jul_7 = 0
        pay_jul_8 = 0

    if (pay_jul_1_ == "5 = payment delay for 5 months"):
        pay_jul_1_ = 0
        pay_jul_0 = 0
        pay_jul_2 = 0
        pay_jul_3 = 0
        pay_jul_4 = 0
        pay_jul_5 = 1
        pay_jul_6 = 0
        pay_jul_7 = 0
        pay_jul_8 = 0

    if (pay_jul_1_ == "6 = payment delay for 6 months"):
        pay_jul_1_ = 0
        pay_jul_0 = 0
        pay_jul_2 = 0
        pay_jul_3 = 0
        pay_jul_4 = 0
        pay_jul_5 = 0
        pay_jul_6 = 1
        pay_jul_7 = 0
        pay_jul_8 = 0

    if (pay_jul_1_ == "7 = payment delay for 7 months"):
        pay_jul_1_ = 0
        pay_jul_0 = 0
        pay_jul_2 = 0
        pay_jul_3 = 0
        pay_jul_4 = 0
        pay_jul_5 = 0
        pay_jul_6 = 0
        pay_jul_7 = 1
        pay_jul_8 = 0

    if (pay_jul_1_ == "8 = payment delay for 8 months"):
        pay_jul_1_ = 0
        pay_jul_0 = 0
        pay_jul_2 = 0
        pay_jul_3 = 0
        pay_jul_4 = 0
        pay_jul_5 = 0
        pay_jul_6 = 0
        pay_jul_7 = 0
        pay_jul_8 = 1

    pay_jun_1_ = st.radio("Repayment Status June",
                          ("0 = paypal", "1 = payment delay for one month", "2 = payment delay for 2 months",
                           "3 = payment delay for 3 months", "4 = payment delay for 4 months",
                           "5 = payment delay for 5 months", "6 = payment delay for 6 months",
                           "7 = payment delay for 7 months", "8 = payment delay for 8 months"))
    if (pay_jun_1_ == "0 = paypal"):
        pay_jun_1_ = 1
        pay_jun_0 = 0
        pay_jun_2 = 0
        pay_jun_3 = 0
        pay_jun_4 = 0
        pay_jun_5 = 0
        pay_jun_6 = 0
        pay_jun_7 = 0
        pay_jun_8 = 0

    if (pay_jun_1_ == "1 = payment delay for one month"):
        pay_jun_1_ = 0
        pay_jun_0 = 1
        pay_jun_2 = 0
        pay_jun_3 = 0
        pay_jun_4 = 0
        pay_jun_5 = 0
        pay_jun_6 = 0
        pay_jun_7 = 0
        pay_jun_8 = 0

    if (pay_jun_1_ == "2 = payment delay for 2 months"):
        pay_jun_1_ = 0
        pay_jun_0 = 0
        pay_jun_2 = 1
        pay_jun_3 = 0
        pay_jun_4 = 0
        pay_jun_5 = 0
        pay_jun_6 = 0
        pay_jun_7 = 0
        pay_jun_8 = 0

    if (pay_jun_1_ == "3 = payment delay for 3 months"):
        pay_jun_1_ = 0
        pay_jun_0 = 0
        pay_jun_2 = 0
        pay_jun_3 = 1
        pay_jun_4 = 0
        pay_jun_5 = 0
        pay_jun_6 = 0
        pay_jun_7 = 0
        pay_jun_8 = 0

    if (pay_jun_1_ == "4 = payment delay for 4 months"):
        pay_jun_1_ = 0
        pay_jun_0 = 0
        pay_jun_2 = 0
        pay_jun_3 = 0
        pay_jun_4 = 1
        pay_jun_5 = 0
        pay_jun_6 = 0
        pay_jun_7 = 0
        pay_jun_8 = 0

    if (pay_jun_1_ == "5 = payment delay for 5 months"):
        pay_jun_1_ = 0
        pay_jun_0 = 0
        pay_jun_2 = 0
        pay_jun_3 = 0
        pay_jun_4 = 0
        pay_jun_5 = 1
        pay_jun_6 = 0
        pay_jun_7 = 0
        pay_jun_8 = 0

    if (pay_jun_1_ == "6 = payment delay for 6 months"):
        pay_jun_1_ = 0
        pay_jun_0 = 0
        pay_jun_2 = 0
        pay_jun_3 = 0
        pay_jun_4 = 0
        pay_jun_5 = 0
        pay_jun_6 = 1
        pay_jun_7 = 0
        pay_jun_8 = 0

    if (pay_jun_1_ == "7 = payment delay for 7 months"):
        pay_jun_1_ = 0
        pay_jun_0 = 0
        pay_jun_2 = 0
        pay_jun_3 = 0
        pay_jun_4 = 0
        pay_jun_5 = 0
        pay_jun_6 = 0
        pay_jun_7 = 1
        pay_jun_8 = 0

    if (pay_jun_1_ == "8 = payment delay for 8 months"):
        pay_jun_1_ = 0
        pay_jun_0 = 0
        pay_jun_2 = 0
        pay_jun_3 = 0
        pay_jun_4 = 0
        pay_jun_5 = 0
        pay_jun_6 = 0
        pay_jun_7 = 0
        pay_jun_8 = 1

    pay_may_1_ = st.radio("Repayment Status May",
                          ("0 = paypal", "1 = payment delay for one month", "2 = payment delay for 2 months",
                           "3 = payment delay for 3 months", "4 = payment delay for 4 months",
                           "5 = payment delay for 5 months", "6 = payment delay for 6 months",
                           "7 = payment delay for 7 months", "8 = payment delay for 8 months"))
    if (pay_may_1_ == "0 = paypal"):
        pay_may_1_ = 1
        pay_may_0 = 0
        pay_may_2 = 0
        pay_may_3 = 0
        pay_may_4 = 0
        pay_may_5 = 0
        pay_may_6 = 0
        pay_may_7 = 0
        pay_may_8 = 0

    if (pay_may_1_ == "1 = payment delay for one month"):
        pay_may_1_ = 0
        pay_may_0 = 1
        pay_may_2 = 0
        pay_may_3 = 0
        pay_may_4 = 0
        pay_may_5 = 0
        pay_may_6 = 0
        pay_may_7 = 0
        pay_may_8 = 0

    if (pay_may_1_ == "2 = payment delay for 2 months"):
        pay_may_1_ = 0
        pay_may_0 = 0
        pay_may_2 = 1
        pay_may_3 = 0
        pay_may_4 = 0
        pay_may_5 = 0
        pay_may_6 = 0
        pay_may_7 = 0
        pay_may_8 = 0

    if (pay_may_1_ == "3 = payment delay for 3 months"):
        pay_may_1_ = 0
        pay_may_0 = 0
        pay_may_2 = 0
        pay_may_3 = 1
        pay_may_4 = 0
        pay_may_5 = 0
        pay_may_6 = 0
        pay_may_7 = 0
        pay_may_8 = 0

    if (pay_may_1_ == "4 = payment delay for 4 months"):
        pay_may_1_ = 0
        pay_may_0 = 0
        pay_may_2 = 0
        pay_may_3 = 0
        pay_may_4 = 1
        pay_may_5 = 0
        pay_may_6 = 0
        pay_may_7 = 0
        pay_may_8 = 0

    if (pay_may_1_ == "5 = payment delay for 5 months"):
        pay_may_1_ = 0
        pay_may_0 = 0
        pay_may_2 = 0
        pay_may_3 = 0
        pay_may_4 = 0
        pay_may_5 = 1
        pay_may_6 = 0
        pay_may_7 = 0
        pay_may_8 = 0

    if (pay_may_1_ == "6 = payment delay for 6 months"):
        pay_may_1_ = 0
        pay_may_0 = 0
        pay_may_2 = 0
        pay_may_3 = 0
        pay_may_4 = 0
        pay_may_5 = 0
        pay_may_6 = 1
        pay_may_7 = 0
        pay_may_8 = 0

    if (pay_may_1_ == "7 = payment delay for 7 months"):
        pay_may_1_ = 0
        pay_may_0 = 0
        pay_may_2 = 0
        pay_may_3 = 0
        pay_may_4 = 0
        pay_may_5 = 0
        pay_may_6 = 0
        pay_may_7 = 1
        pay_may_8 = 0

    if (pay_may_1_ == "8 = payment delay for 8 months"):
        pay_may_1_ = 0
        pay_may_0 = 0
        pay_may_2 = 0
        pay_may_3 = 0
        pay_may_4 = 0
        pay_may_5 = 0
        pay_may_6 = 0
        pay_may_7 = 0
        pay_may_8 = 1

    pay_apr_1_ = st.radio("Repayment Status April",
                          ("0 = paypal", "1 = payment delay for one month", "2 = payment delay for 2 months",
                           "3 = payment delay for 3 months", "4 = payment delay for 4 months",
                           "5 = payment delay for 5 months", "6 = payment delay for 6 months",
                           "7 = payment delay for 7 months", "8 = payment delay for 8 months"))
    if (pay_apr_1_ == "0 = paypal"):
        pay_apr_1_ = 1
        pay_apr_0 = 0
        pay_apr_2 = 0
        pay_apr_3 = 0
        pay_apr_4 = 0
        pay_apr_5 = 0
        pay_apr_6 = 0
        pay_apr_7 = 0
        pay_apr_8 = 0

    if (pay_apr_1_ == "1 = payment delay for one month"):
        pay_apr_1_ = 0
        pay_apr_0 = 1
        pay_apr_2 = 0
        pay_apr_3 = 0
        pay_apr_4 = 0
        pay_apr_5 = 0
        pay_apr_6 = 0
        pay_apr_7 = 0
        pay_apr_8 = 0

    if (pay_apr_1_ == "2 = payment delay for 2 months"):
        pay_apr_1_ = 0
        pay_apr_0 = 0
        pay_apr_2 = 1
        pay_apr_3 = 0
        pay_apr_4 = 0
        pay_apr_5 = 0
        pay_apr_6 = 0
        pay_apr_7 = 0
        pay_apr_8 = 0

    if (pay_apr_1_ == "3 = payment delay for 3 months"):
        pay_apr_1_ = 0
        pay_apr_0 = 0
        pay_apr_2 = 0
        pay_apr_3 = 1
        pay_apr_4 = 0
        pay_apr_5 = 0
        pay_apr_6 = 0
        pay_apr_7 = 0
        pay_apr_8 = 0

    if (pay_apr_1_ == "4 = payment delay for 4 months"):
        pay_apr_1_ = 0
        pay_apr_0 = 0
        pay_apr_2 = 0
        pay_apr_3 = 0
        pay_apr_4 = 1
        pay_apr_5 = 0
        pay_apr_6 = 0
        pay_apr_7 = 0
        pay_apr_8 = 0

    if (pay_apr_1_ == "5 = payment delay for 5 months"):
        pay_apr_1_ = 0
        pay_apr_0 = 0
        pay_apr_2 = 0
        pay_apr_3 = 0
        pay_apr_4 = 0
        pay_apr_5 = 1
        pay_apr_6 = 0
        pay_apr_7 = 0
        pay_apr_8 = 0

    if (pay_apr_1_ == "6 = payment delay for 6 months"):
        pay_apr_1_ = 0
        pay_apr_0 = 0
        pay_apr_2 = 0
        pay_apr_3 = 0
        pay_apr_4 = 0
        pay_apr_5 = 0
        pay_apr_6 = 1
        pay_apr_7 = 0
        pay_apr_8 = 0

    if (pay_apr_1_ == "7 = payment delay for 7 months"):
        pay_apr_1_ = 0
        pay_apr_0 = 0
        pay_apr_2 = 0
        pay_apr_3 = 0
        pay_apr_4 = 0
        pay_apr_5 = 0
        pay_apr_6 = 0
        pay_apr_7 = 1
        pay_apr_8 = 0

    if (pay_apr_1_ == "8 = payment delay for 8 months"):
        pay_apr_1_ = 0
        pay_apr_0 = 0
        pay_apr_2 = 0
        pay_apr_3 = 0
        pay_apr_4 = 0
        pay_apr_5 = 0
        pay_apr_6 = 0
        pay_apr_7 = 0
        pay_apr_8 = 1

    if st.button('Credit Card will default or not'):
        result = credit_card(
            [limit_bal, sex, age, bill_amt_sept, bill_amt_aug, bill_amt_jul, bill_amt_jun, bill_amt_may, bill_amt_apr, pay_amt_sept, pay_amt_aug,
             pay_amt_jul, pay_amt_jun, pay_amt_may, pay_amt_apr, education_Graduate_School, education_High_School, education_University,
             marriage_Married, marriage_Single, pay_sept_1_, pay_sept_0, pay_sept_1, pay_sept_2, pay_sept_3, pay_sept_4, pay_sept_5, pay_sept_6,
             pay_sept_7, pay_sept_8, pay_aug_1_, pay_aug_0, pay_aug_1, pay_aug_2, pay_aug_3, pay_aug_4, pay_aug_5, pay_aug_6, pay_aug_7,
             pay_aug_8, pay_jul_1_, pay_jul_0, pay_jul_1, pay_jul_2, pay_jul_3, pay_jul_4, pay_jul_5, pay_jul_6, pay_jul_7, pay_jul_8,
             pay_jun_1_, pay_jun_0, pay_jun_1, pay_jun_2, pay_jun_3, pay_jun_4, pay_jun_5, pay_jun_6, pay_jun_7, pay_jun_8, pay_may_1_,
             pay_may_0, pay_may_1, pay_may_2, pay_may_3, pay_may_4, pay_may_5, pay_may_6, pay_may_7, pay_may_8, pay_apr_1_, pay_apr_0,
             pay_apr_1, pay_apr_2, pay_apr_3, pay_apr_4, pay_apr_5, pay_apr_6, pay_apr_7, pay_apr_8])


if __name__ == '__main__':
    main()
