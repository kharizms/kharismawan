# 1. Tes kesetaraan dan ketidaksamaan dengan string
food = "bakso"
print("Is food == 'bakso'? I predict True.")
print(food == "bakso")

print("Is food != 'sate'? I predict True.")
print(food != "sate")


# 2. Tes menggunakan metode lower()
name = "Python"
print("\nIs name.lower() == 'python'? I predict True.")
print(name.lower() == "python")

print("Is name.lower() == 'java'? I predict False.")
print(name.lower() == "java")


# 3. Tes numerik (angka)
age = 20
print(f"\nTes Numerik (age = {age}):")
print(f"Is age == 20? {age == 20} (True)")
print(f"Is age != 25? {age != 25} (True)")
print(f"Is age > 18? {age > 18} (True)")
print(f"Is age < 15? {age < 15} (False)")
print(f"Is age >= 21? {age >= 21} (False)")
print(f"Is age <= 18? {age <= 18} (False)")


# 4. Tes menggunakan keyword 'and' dan 'or'
has_id = True
is_adult = True
has_permission = False

print("\nTes Operator Logika (and & or):")
print(f"Is has_id and is_adult? {has_id and is_adult} (True)")
print(f"Is has_id and has_permission? {has_id and has_permission} (False)")
print(f"Is has_permission or is_adult? {has_permission or is_adult} (True)")
print(f"Is has_permission or (age < 18)? {has_permission or (age < 18)} (False)")


# 5. Tes keberadaan item dalam list (in & not in)
languages = ["python", "c", "c++"]
print("\nTes Keberadaan List (in & not in):")
print(f"Is 'python' in languages? {'python' in languages} (True)")
print(f"Is 'java' in languages? {'java' in languages} (False)")
print(f"Is 'java' not in languages? {'java' not in languages} (True)")
print(f"Is 'python' not in languages? {'python' not in languages} (False)")