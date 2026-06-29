from converter import image_to_ascii

image_path = input("Enter image path: ")

try:
    image_to_ascii(image_path)
    print("\n✅ ASCII art saved to output.txt")
except Exception as e:
    print("❌ Error:", e)
