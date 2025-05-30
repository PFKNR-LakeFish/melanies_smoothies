import streamlit as st
from snowflake.snowpark import Session

st.title("Snowflake Connection Test")

try:
    # Load connection parameters from secrets
    connection_parameters = st.secrets["snowflake"]

    # Create a Snowpark session
    session = Session.builder.configs(connection_parameters).create()

    # Run a simple query
    df = session.sql("SELECT CURRENT_USER(), CURRENT_ROLE(), CURRENT_DATABASE(), CURRENT_SCHEMA()").to_pandas()

    st.success("✅ Successfully connected to Snowflake!")
    st.dataframe(df)

except Exception as e:
    st.error("❌ Failed to connect to Snowflake.")
    st.exception(e)
