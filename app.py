import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

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


if __name__ == '__main__':
    main()
