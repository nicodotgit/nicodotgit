import re
from datetime import datetime
from zoneinfo import ZoneInfo

# 1. Configuration
# Birthdate: January 18, 2005, 13:40 Chile time
birth_date = datetime(2005, 1, 18, 13, 40, tzinfo=ZoneInfo("America/Santiago"))
readme_path = "README.md"

# 2. Calculate Age
# We use the average Gregorian year (365.2425 days) for better precision over time
current_date = datetime.now(ZoneInfo("America/Santiago"))
difference = current_date - birth_date
years = difference.total_seconds() / (365.2425 * 24 * 3600)

# Format to 4 decimal places
formatted_age = f"{years:.4f}"

# 3. Update README.md
with open(readme_path, "r", encoding="utf-8") as file:
    content = file.read()

# Regex to find the existing badge URL. 
# Matches: src="https://img.shields.io/badge/Age-[NUMBER]-blue
pattern = r"(src=\"https://img\.shields\.io/badge/Age-)([\d\.]+)(-blue)"

# Replace with new age
new_content = re.sub(pattern, f"\\g<1>{formatted_age}\\g<3>", content)

if content != new_content:
    with open(readme_path, "w", encoding="utf-8") as file:
        file.write(new_content)
    print(f"Updated age to {formatted_age}")
else:
    print("Age is already up to date.")
