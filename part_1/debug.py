import os
import numpy as np

# Print current working directory
print("Current Working Directory:", os.getcwd())

# Check if the file exists in the expected path
file_path = '/Users/lylenghort/Documents/Hs_md7_matplotlib/Hs_matplotlib/part_1/points.csv'

if os.path.exists(file_path):
    print(f"✅ File found: {file_path}")

    # Check if the file is readable
    try:
        with open(file_path, 'r') as f:
            print("✅ File opened successfully. First 5 lines:")
            for _ in range(5):
                print(f.readline().strip())
    except Exception as e:
        print(f"❌ Error reading the file: {e}")

    # Try loading with NumPy
    try:
        points = np.loadtxt(file_path, delimiter=',')
        print("✅ NumPy loaded the file successfully!")
        print("First 5 rows:", points[:5])
    except Exception as e:
        print(f"❌ NumPy error: {e}")

else:
    print(f"❌ File NOT found: {file_path}")
    print("Check if the file exists and is accessible.")

# Alternative: Try using a relative path
relative_path = "points.csv"
if os.path.exists(relative_path):
    print(f"✅ Found the file using relative path: {relative_path}")
else:
    print(f"❌ File NOT found using relative path: {relative_path}")
