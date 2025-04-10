import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide',page_title='StartUp Analysis')

df = pd.read_csv('startup_cleaned.csv')

def load_overall_analysis():
    st.title('Overall Analysis')

    #total invested amount
    total = round(df['amount'].sum())
    max_funding = df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]
    avg_funding = df.groupby('startup')['amount'].sum().mean()
    nums_startups = df['startup'].nunique()

    col1,col2,col3,col4 =st.columns(4)

    with col1:
        st.metric('Total', str(total) + 'Cr')
    with col2:
        st.metric('Max', str(max_funding) + 'Cr')
    with col3:
        st.metric('Avg',str(round(avg_funding))+ 'Cr')
    with col4:
        st.metric('Funded StartUps',nums_startups)

def load_investors_details(investor):
    st.title(investor)
    #load 5 investments of investors
    last5_df = df[df['investors'].str.contains(investor)].head()[['date','startup','vertical','city','round','amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)

    #biggest Investments
    col1,col2 = st.columns(2)
    with col1:
        big_series = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        st.subheader('Biggest Investment')

        fig, ax = plt.subplots()
        ax.bar(big_series.index,big_series.values)

        st.pyplot(fig)
    with col2:
        vertical_series = df[df['investors'].str.contains(investor, na=False)] \
            .groupby('vertical')['amount'].sum()

        st.subheader('Sectors Invested in:')

        # Bigger size (width, height)
        fig1, ax1 = plt.subplots(figsize=(8, 6))  # Increase as needed
        ax1.pie(vertical_series, labels=vertical_series.index, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')  # Keep it a perfect circle

        st.pyplot(fig1)
    col1, col2 = st.columns(2)
    with col1:
        vertical_series = df[df['investors'].str.contains(investor, na=False)] \
            .groupby('city')['amount'].sum()

        st.subheader('City:')

        # Bigger size (width, height)
        fig1, ax1 = plt.subplots(figsize=(8, 6))  # Increase as needed
        ax1.pie(vertical_series, labels=vertical_series.index, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')  # Keep it a perfect circle

        st.pyplot(fig1)
    with col2:
        # Ensure 'date' column is in datetime format
        df['date'] = pd.to_datetime(df['date'], errors='coerce')

        # Extract year after conversion
        df['year'] = df['date'].dt.year

        # Filter and group by year
        year_series = df[df['investors'].str.contains(investor, na=False)].groupby('year')['amount'].sum()

        st.subheader('YOY Investment:')
        fig2, ax2 = plt.subplots(figsize=(8, 6))
        ax2.plot(year_series.index, year_series.values, marker='o', linestyle='-')

        # Removed ax2.axis('equal') — it's not suitable for line plots
        ax2.set_xlabel('Year')
        ax2.set_ylabel('Total Investment (₹)')
        ax2.set_title('Year-over-Year Investment by IDG Ventures')
        ax2.grid(True)

        st.pyplot(fig2)


df['investors']=df['investors'].fillna('undisclosed')
st.sidebar.title('StartUp Funding Analysis')
option = st.sidebar.selectbox('Select one:',['Overall Analysis','StartUp','Investor'])

if option =='Overall Analysis':

    btn0 = st.sidebar.button('Show Overall Analysis')
    if btn0:
        load_overall_analysis()

elif option =='StartUp':
    st.sidebar.selectbox('Select StartUp:',sorted(df['startup'].unique().tolist()))
    btn1=st.sidebar.button('Find StartUp Details')
    st.title('StartUp Analysis')
else:
    selected_investor = st.sidebar.selectbox('Select Investor',sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investors Details')
    if btn2:
        load_investors_details(selected_investor)




