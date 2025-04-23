import os

import streamlit as st

from calculator.math_ops import add
from settings import Settings


def main():
    st.title("Number Addition App")

    st.write("This simple app adds two numbers together.")

    env_file = os.getenv("ENV_FILE_PATH", "conf/.env.dev")
    settings = Settings(_env_file=env_file, _env_file_encoding="utf-8")
    st.markdown(f"### Settings:\n* {settings.db_host=}\n* {settings.openai_api_key=}\n"
                f"* {settings.openai_api_key.get_secret_value()=}")

    # Get user inputs
    num1 = st.number_input("Enter the first number:", value=0.0)
    num2 = st.number_input("Enter the second number:", value=0.0)

    # Calculate the result
    result = add(num1, num2)

    # Display the result
    st.write(f"### Result: {result}")

    # Add some explanation
    with st.expander("How it works"):
        st.write("""
        This app is a simple demonstration of Streamlit capabilities.
        It takes two numerical inputs and returns their sum.
        """)


if __name__ == "__main__":
    main()
