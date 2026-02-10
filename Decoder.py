import base64

def decode_base64(data):
    try:
        # Convert the string to bytes
        byte_data = data.encode('utf-8')
        
        # Decode the base64 bytes
        decoded_bytes = base64.b64decode(byte_data)
        
        # Convert bytes back to a readable string
        return decoded_bytes.decode('utf-8')
    except Exception as e:
        return f"Error: Invalid Base64 input or non-text content. ({e})"

# --- Quick Test ---
if __name__ == "__main__":
    # Example: "SGVsbG8gV29ybGQh" is "Hello World!"
    user_input = input("Enter the Base64 string to decode: ")
    
    result = decode_base64(user_input)
    print("\nDecoded Result:")
    print("-" * 20)
    print(result)
    print("-" * 20)
