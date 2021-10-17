def method(new_string):
    upper_case=new_string.upper()
    print(upper_case)

    Lower_case = new_string.lower()
    print(Lower_case)


    split1 = new_string.split("_")
    print(split1)

    split2 = new_string.split(" ")
    print(split2)


    print("indexing", new_string[::1])

method( input("Enter a string: "))
