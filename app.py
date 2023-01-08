import streamlit as st
import pandas as pd

# Function to load data from an XLSX file
@st.cache
def load_xlsx(file):
    return pd.read_excel(file)

# Function to save data to a CSV file
def save_csv(df, filename):
    df.to_csv(filename, index=False)

# Main function
def main():
    st.title("XLSX to CSV Converter")

    # Load data from XLSX file
    file = st.file_uploader("Upload XLSX file", type="xlsx")
    if file is not None:
        df = load_xlsx(file)

    # Save data to CSV file
    if "df" in locals():
        if st.button("Convert to CSV"):
            filename = st.text_input("Enter filename")
            if filename:
                save_csv(df, filename)
                st.success("Data saved to CSV file")

if __name__ == "__main__":
    main()
