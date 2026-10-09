from src.pinterest.auth import PinterestAuth


auth = PinterestAuth()

url = auth.get_authorization_url()

print("Pinterest authorization URL:")
print(url)