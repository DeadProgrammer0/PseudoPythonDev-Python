# Else and Finally in Try Except.

f1 = open("dict.txt")

try:
    f = open("dict3.txt")
except Exception as e:
    print(f"Error! {e}.")
else:
    print("File was Opened Successfully.")
finally:
    f1.close()
    try:
        f.close()
    except Exception as e:
        print("Failed to Close f.")
    print("Files Closed.")