# Removing spaces from beginning and at the end

name = "        Harshad         "
final_name = name.strip()
print("The final input is", final_name)

# Removing left space and right space
lspace = name.lstrip()
print("The left space removed", lspace)

rspace = name.rstrip()
print("the right space removed", rspace)

