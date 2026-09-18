print("======================================")
print("     PHISHING AWARENESS SIMULATOR")
print("======================================")

print("\nExample Email:")
print("--------------------------------------")
print("Subject: Urgent - Your Account Needs Verification")
print("From: security@example-security-check.com")
print("")
print("Your account has been selected for verification.")
print("Please review your account immediately.")
print("--------------------------------------")

score = 0

print("\nIdentify the warning signs.")

answer = input("\n1. Does the message create urgency? (yes/no): ")

if answer.lower() == "yes":
    score += 1

answer = input("2. Is the sender address suspicious? (yes/no): ")

if answer.lower() == "yes":
    score += 1

answer = input("3. Should you verify a link before clicking it? (yes/no): ")

if answer.lower() == "yes":
    score += 1

print("\n======================================")
print("             RESULT")
print("======================================")

print("Your score:", score, "/ 3")

if score == 3:
    print("Excellent! You identified the major warning signs.")
elif score == 2:
    print("Good! You identified most warning signs.")
else:
    print("Review common phishing warning signs.")

print("\nRemember:")
print("- Check the sender address.")
print("- Be careful with urgent messages.")
print("- Verify links before opening them.")
print("- Never share passwords through suspicious messages.")