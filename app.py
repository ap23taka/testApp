import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import streamlit_authenticator as stauth

##### Basic Auth
def basicauth_
# configs
names = ["user"]
usernames = ["username"]
# passwords = ["***"] # delete after hashing
# hashed_passwords = stauth.hasher(passwords).generate()
hashed_passwords = ['$2b$12$3N0xSkirQPcndDPSmQfKZOc2EEJByhJbv.mxm9cUWQDATsO4.fuNa']
authenticator = stauth.authenticate(names,usernames,hashed_passwords,'some_cookie_name','some_signature_key',cookie_expiry_days=0)

# Get User Input via APP interface
name, authentication_status = authenticator.login('Login','main')

##### APP
def main():
    st.title("Data to Pairplot APP")

    ## Data
    st.subheader("Data Selection")
    uploaded_file = st.file_uploader(
        label="Upload an excel file"
    )
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        # st.write(type(uploaded_file))
        st.subheader("Uploaded Data")
        st.write(df)
        st.write(f"Columns : {df.columns.values}")

        ### side bar
        option = st.sidebar.multiselect(
            label = 'Select columns for correlation plot.',
            options=df.columns.values.tolist(),
            default=df.columns.values[:4]
        )

        # plot
        st.subheader('Pairplot (Matrix of Correlation plot)')
        st.write("Select columns at side bar.")
        st.write('Current selections :', option)

        fig = sns.pairplot(data=df, vars=option, diag_kind="kde")
        st.pyplot(fig)

if authentication_status:
    # st.write('Welcome *%s*' % (name))
    main()
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')

