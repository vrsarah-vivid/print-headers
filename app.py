import streamlit as st

def main():
    # Add an explanation
    st.markdown("""
    ## About X-Forwarded-For
    The `X-Forwarded-For` header identifies the originating IP address of a client connecting through proxies or load balancers.
    """)

    st.write("## Headers")
    st.write(st.context.headers)

if __name__ == "__main__":
    main()
