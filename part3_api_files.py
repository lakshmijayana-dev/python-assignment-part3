# Writing to file
with open("python_notes.txt", "w", encoding="utf-8") as f:
    f.write("Topic 1: Variables store data. Python is dynamically typed.\n")
    f.write("Topic 2: Lists are ordered and mutable.\n")
    f.write("Topic 3: Dictionaries store key-value pairs.\n")
    f.write("Topic 4: Loops automate repetitive tasks.\n")
    f.write("Topic 5: Exception handling prevents crashes.\n")

print("File written successfully")

with open("python_notes.txt", "a", encoding="utf-8") as f:
    f.write("Topic 6: Functions help reuse code.\n")
    f.write("Topic 7: APIs allow communication between systems.\n")

print("Lines appended")

print("\nReading file:")

with open("python_notes.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    print(f"{i+1}. {line.strip()}")


print("\nTotal lines:", len(lines))

keyword = input("\nEnter keyword to search: ").lower()

found = False

for line in lines:
    if keyword in line.lower():
        print(line.strip())
        found = True

if not found:
    print("No match found")

import requests

print("\n--- Fetch Products ---")

res = requests.get("https://dummyjson.com/products?limit=20")
data = res.json()

products = data["products"]

# Print table
print("ID | Title | Category | Price | Rating")
print("-"*50)

for p in products:
    print(p["id"], "|", p["title"], "|", p["category"], "|", p["price"], "|", p["rating"])

print("\n--- Filtered & Sorted ---")

filtered = [p for p in products if p["rating"] >= 4.5]

# Sort by price descending
filtered.sort(key=lambda x: x["price"], reverse=True)

for p in filtered:
    print(p["title"], "-", p["price"], "-", p["rating"]) 

print("\n--- Laptops Category ---")

res = requests.get("https://dummyjson.com/products/category/laptops")
data = res.json()

for p in data["products"]:
    print(p["title"], "-", p["price"]) 

print("\n--- POST Request ---")

new_product = {
    "title": "My Custom Product",
    "price": 999,
    "category": "electronics",
    "description": "A product I created via API"
}

res = requests.post("https://dummyjson.com/products/add", json=new_product)

print(res.json())

def safe_divide(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

    except TypeError:
        return "Error: Invalid input types"


# Testing
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("ten", 2))

def read_file_safe(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()
            return content

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")

    finally:
        print("File operation attempt complete.")


# Testing
print(read_file_safe("python_notes.txt"))   # should work
print(read_file_safe("ghost_file.txt"))     # should fail

import requests

try:
    res = requests.get("https://dummyjson.com/products", timeout=5)
    print("API call successful")

except requests.exceptions.ConnectionError:
    print("Connection failed. Please check your internet.")

except requests.exceptions.Timeout:
    print("Request timed out. Try again later.")

except Exception as e:
    print("Error:", e)

while True:
    user_input = input("Enter product ID (1–100) or 'quit': ")

    if user_input.lower() == "quit":
        break

    if not user_input.isdigit():
        print("Invalid input. Enter number only.")
        continue

    product_id = int(user_input)

    if product_id < 1 or product_id > 100:
        print("Enter ID between 1–100")
        continue

    # API call
    res = requests.get(f"https://dummyjson.com/products/{product_id}")

    if res.status_code == 404:
        print("Product not found")
    else:
        data = res.json()
        print(data["title"], "-", data["price"])    