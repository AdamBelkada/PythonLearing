from demo import process_data
# from demo import main

print("from caller script...")
print(__name__)

# main()
# process_data("stuff")
# print("newstuff:" + str(newstuff))
# print ("caller is done")


def main():
    print("SSSSSSSSSSSSSSS")
    data = "directly running demo"
    print(data)
    modified_data = process_data(data)
    print(modified_data)

if __name__ == "__main__":
    print("TTTTTTTTTTTTTTTTTTTTTTT")
    main()