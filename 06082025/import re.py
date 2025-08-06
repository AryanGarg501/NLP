import re

# 1. Find URL
def extract_url(text):
    return re.findall(r'https?://[^\s]+', text)

# 2. Get email id
def extract_email(text):
    return re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)

# 3. Find hashtags
def extract_hashtags(text):
    return re.findall(r'#\w+', text)

# 4. Find mentions
def extract_mentions(text):
    return re.findall(r'@\w+', text)

# 5. Find numbers
def extract_numbers(text):
    return re.findall(r'\d+', text)

# 6. Find punctuations
def extract_punctuations(text):
    return re.findall(r'[^\w\s]', text)

# 7. Validate PAN number
def validate_pan(text):
    return bool(re.fullmatch(r'[A-Z]{5}[0-9]{4}[A-Z]', text))

# 8. Remove repetitive characters
def remove_repetitions(text):
    return re.sub(r'(.)\1+', r'\1', text)

# 9. Find Indian mobile numbers (starting with 9, 8 or 7 and 10 digits)
def extract_indian_mobile_numbers(text):
    return re.findall(r'\b[789]\d{9}\b', text)

# 10. Extract words starting with capital letter
def extract_capitalized_words(text):
    return re.findall(r'\b[A-Z][a-z]*\b', text)


# --------------------- Test Examples ---------------------

print("1. URL:", extract_url("I love spending time at https://www.xy123z.com/"))
print("2. Email:", extract_email("My email id is xyz111@gmail.com"))
print("3. Hashtags:", extract_hashtags("#Sushant is trending now in the world."))
print("4. Mentions:", extract_mentions("@Ajit, please help me"))
print("5. Numbers:", extract_numbers("8853147 sq. km of area washed away in floods"))
print("6. Punctuations:", extract_punctuations("Corona virus killed #24506 people. #Corona is un(tolerable)"))
print("7. PAN Valid (ABCED3193P):", validate_pan("ABCED3193P"))
print("   PAN Invalid (lEcGD012eg):", validate_pan("lEcGD012eg"))
print("8. Repetition Removed:", remove_repetitions("heyyy this is a verrrry loong texttt"))
print("9. Indian Mobile:", extract_indian_mobile_numbers("9990001796 is a phone number of PMO office"))
print("10. Capital Words:", extract_capitalized_words("Ajit Doval is the best National Security Advisor so far."))
