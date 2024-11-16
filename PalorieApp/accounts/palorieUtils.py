import requests
from .config import FOODVISOR_API_KEY

# Make foodvisor API request to generate nutritional information from image path
def generate_from_image(path_to_image):
    url = "https://vision.foodvisor.io/api/1.0/en/analysis/"
    headers = {
        "Authorization": f"Api-Key {FOODVISOR_API_KEY}",

        }
    with open(f"{path_to_image}", "rb") as image:
        response = requests.post(url, headers=headers, files={"image": image})
        response.raise_for_status()
    
    if response.status_code == 200:
        response_data = response.json()
        
        # Extract only the relevant information (display_name and g_per_serving)
        extracted_data = []
        for item in response_data.get('items', []):
            food_info = item.get('food', [{}])[0].get('food_info', {})
            
            # Collect display_name and g_per_serving, using default values if the key is missing
            food = {
                "display_name": food_info.get("display_name", "Unknown"),
                "g_per_serving": food_info.get("g_per_serving", "N/A")
            }
            
            extracted_data.append(food)
        
        # Now `extracted_data` contains only the information you want
        print(extracted_data)
        return extracted_data

    else:
        print(f"Error: {response.status_code}")
