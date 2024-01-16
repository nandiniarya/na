# app.py

import streamlit as st
import pandas as pd
import plotly.express as px


def main():
    st.title("My Dashboard")

    # Your content goes here

if __name__ == "__main__":
    main()



# Page title
st.title("Sales Dashboard")

# Load your dataset
try : 
    data_url="ecom.csv"
    df = pd.read_csv(data_url)

    # Display the DataFrame
    st.subheader("Data Preview:")
    st.dataframe(df)

    # Slicers (Dropdowns)
    selected_countries = st.multiselect('Select Countries:', df['country'].unique())
    selected_genders = st.multiselect('Select Genders:', df['gender'].unique())

    # Filter the DataFrame based on slicer selections
    filtered_df = df[
        (df['country'].isin(selected_countries)) &
        (df['gender'].isin(selected_genders))
    ]

    # 1. Bar chart of total sales per country
    st.subheader("1. Total Sales by Country Bar Chart")
    fig_bar = px.bar(filtered_df, x='country', y='sales', title='Total Sales by Country',
                     color='sales', color_continuous_scale='Viridis')
    fig_bar.update_layout(showlegend=False)  # Hide legend for cleaner appearance
    st.plotly_chart(fig_bar)

    # 2. Pie chart of payment methods distribution
    st.subheader("2. Payment Methods Distribution Pie Chart")
    fig_pie = px.pie(filtered_df, names='pay_method', title='Payment Methods Distribution',
                     color_discrete_sequence=px.colors.qualitative.Set3)
    st.plotly_chart(fig_pie)

    # 3. Line chart of sales trends over time
    st.subheader("3. Sales Trends Over Time Line Chart")
    fig_line = px.line(filtered_df, x='accessed_date', y='sales', title='Sales Trends Over Time',
                       line_shape='linear', render_mode='svg', line_dash_sequence=['solid'],
                       labels={'accessed_date': 'Accessed Date', 'sales': 'Sales'},
                       color_discrete_sequence=['#1f77b4'])
    st.plotly_chart(fig_line)

    # 4. Box plot of sales by gender
    st.subheader("4. Box Plot of Sales by Gender")
    fig_box = px.box(filtered_df, x='gender', y='sales', title='Sales Distribution by Gender',
                     color='gender', color_discrete_sequence=['#ff7f0e'])
    st.plotly_chart(fig_box)

    # 5. Different Area chart of total sales across network protocols over time
    st.subheader("5. Area Chart of Sales Across Network Protocols Over Time")
    fig_area_network = px.area(filtered_df, x='accessed_date', y='sales', color='network_protocol',
                               title='Sales Across Network Protocols Over Time (Area Chart)',
                               color_discrete_sequence=px.colors.qualitative.Set2)
    st.plotly_chart(fig_area_network)

except pd.errors.EmptyDataError:
    st.error("Error: Empty dataset.")
except Exception as e:
    st.error(f"Error: {e}")
