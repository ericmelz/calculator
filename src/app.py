import streamlit as st

def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

def main():
    st.title("Number Addition App")
    
    st.write("This simple app adds two numbers together.")
    
    # Get user inputs
    num1 = st.number_input("Enter the first number:", value=0.0)
    num2 = st.number_input("Enter the second number:", value=0.0)
    
    # Calculate the result
    result = add_numbers(num1, num2)
    
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
