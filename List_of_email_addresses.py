# List of email addresses (some duplicates)

email_addresses = ["userl@example.com", "user2@example.com", "user3@example.com", "user1@example.com", "user4@example.com", "user2@example.com"]

# Use a set to remove duplicates
unique_emails = set (email_addresses)

#Convert the set back to a sorted list if needed 
unique_emails_list = sorted (unique_emails)
print (unique_emails_list)

# Output the unique email addresses

print("Unique email addresses:")
for email in unique_emails_list:
    print(email)