# Package initializer for shop_package
# This file marks shop_package as a Python package directory.

# Importing key functions here so they can be imported directly from package if needed:
# e.g., from shop_package import calculate_total, apply_discount

from .discount import apply_discount, flat_discount
from .billing import calculate_total, apply_tax

print("Initializing shop_package...")  # learning note: prints when package is first imported!
