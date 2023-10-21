import requests

def get_public_ip():
    try:
        response = requests.get("https://api64.ipify.org?format=json")
        if response.status_code == 200:
            data = response.json()
            return data["ip"]
        else:
            return "Failed to retrieve IP"
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    public_ip = get_public_ip()
    print(f"Your public IP address is: {public_ip}")
