import streamlit as st
import requests
import json
from pprint import pformat


def main():
    # Add an explanation
    st.markdown("""
    ## About X-Forwarded-For
    The `X-Forwarded-For` header identifies the originating IP address of a client connecting through proxies or load balancers.

    Format: `X-Forwarded-For: client_ip, proxy1_ip, proxy2_ip, ...`
    """)

    # Display current request headers
    st.header("Your Request Headers")

    # Get headers from the streamlit request
    headers = st.query_params

    # Manual header input for testing
    st.header("Test with Custom Headers")
    custom_header = st.text_input("Enter X-Forwarded-For value (e.g., '203.0.113.195, 70.41.3.18, 150.172.238.178')")

    if custom_header:
        st.code(f"X-Forwarded-For: {custom_header}")

        # Parse the header
        ips = [ip.strip() for ip in custom_header.split(",")]
        st.write("Client IP (first in chain):", ips[0])
        if len(ips) > 1:
            st.write("Proxy chain:", ", ".join(ips[1:]))


if __name__ == "__main__":
    main()
