
#%% Specify DATA_DIR and SAMPLE_DIR

from pathlib import Path

# Locate repository root folder
PROJECT_ROOT = Path(__file__).resolve().parent

# Dataset directory
DATA_DIR = PROJECT_ROOT / "data"

# Individual data file location
SAMPLE_DIR = DATA_DIR / "2016_MagDown"

# %% Test cell

print(f"Project root exists: {PROJECT_ROOT.exists()}")
print(f"Dataset directory exists: {SAMPLE_DIR.exists()}")

root_files = list(SAMPLE_DIR.glob("*.root"))

print(f"ROOT files found: {len(root_files)}")

for file in root_files:
    print(file.name)

# Booleans should return True
# Expect 2 ROOT files found, and list them