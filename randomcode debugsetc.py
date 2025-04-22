'''#debug the rating:
# Debug logging for intermediate values
specres_adjusted = (self.specres - 75) / 20
baseres_adjusted = (self.baseres - 45) / 30
combined_res = (specres_adjusted + baseres_adjusted) / 50 * 2
specproc_component = specproc_count / 3
baseproc_component = (basecount + specproc_count) / 13

# Log intermediate values
print(f"specres_adjusted: {specres_adjusted}")
print(f"baseres_adjusted: {baseres_adjusted}")
print(f"combined_res: {combined_res}")
print(" ")
print(f"specproc_count: {specproc_count}")
print(f"basecount: {basecount}")
print(f"specproc_component: {specproc_component}")
print(f"baseproc_component: {baseproc_component}")


# Calculate the rating
self.rating = int(((combined_res + specproc_component + baseproc_component) / 4) * 100)

# Log final rating before capping
print(f"Calculated rating before capping: {self.rating}")

# Cap the rating at 100
self.rating = min(self.rating, 100)'''

import random
import string

def generate_random_string():
    """Generates a random string of letters and numbers with the specified length."""
    length=25
    characters = string.ascii_letters + string.digits  # Combine letters and digits
    return ''.join(random.choices(characters, k=length))

# Example usage
for _ in range(10):
    random_string = generate_random_string()
    print(random_string)