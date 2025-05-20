import streamlit as st
import requests
import json
from pprint import pformat


def main():
    st.title("HTTP Headers Inspector")
    st.write("This app shows HTTP request headers, focusing on X-Forwarded-For")

    # Add an explanation
    st.markdown("""
    ## About X-Forwarded-For
    The `X-Forwarded-For` header identifies the originating IP address of a client connecting through proxies or load balancers.

    Format: `X-Forwarded-For: client_ip, proxy1_ip, proxy2_ip, ...`
    """)

    # Display current request headers
    st.header("Your Current Request Headers")

    # Get headers from the streamlit request
    headers = st.experimental_get_query_params()

    # Try to get the Streamlit session information which may contain header data
    st.subheader("Streamlit Session Info")
    session_info = st.session_state.to_dict()
    st.code(pformat(session_info), language="python")

    # Alternative approach: Make a request to a header echo service
    st.header("Headers Echo Service")
    if st.button("Fetch Headers from httpbin.org"):
        try:
            response = requests.get("https://httpbin.org/headers")
            if response.status_code == 200:
                headers_data = response.json()

                # Check if X-Forwarded-For exists
                x_forwarded = headers_data.get('headers', {}).get('X-Forwarded-For')

                if x_forwarded:
                    st.success(f"X-Forwarded-For header found: {x_forwarded}")
                else:
                    st.info("No X-Forwarded-For header detected")

                # Display all headers
                st.json(headers_data)
            else:
                st.error(f"Failed to get headers: {response.status_code}")
        except Exception as e:
            st.error(f"Error fetching headers: {e}")

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
