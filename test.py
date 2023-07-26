import streamlit as st

def test_secrets():
    print(st.secrets["SUPABASE_URL"])
    print(st.secrets["SUPABASE_KEY"])
    print(st.secrets["OPENAI_API_KEY"])

if __name__ == "__main__":
    test_secrets()
