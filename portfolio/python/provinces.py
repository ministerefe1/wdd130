def main():
    text_list = read_list("provinces.txt")
    # Remove element from the last of a list
    # text_list = text_list[:-1]

    # Remove element from the first of a list
    text_list = text_list[1:]
    # Replace 'AB' with Alberta in a list
    for i in range(len(text_list)):
        if text_list[i] == "AB":
            text_list[i] = "Alberta"

    alberta_count = text_list.count("Alberta")

    print(f"the number of element that are Alberta in list: {alberta_count}")

    print(text_list)


def read_list(filename):
    text_list = []

    with open(filename, "rt") as text_file:
        for line in text_file:
            clean_list = line.strip()

            text_list.append(clean_list)

    return text_list


if __name__ == "__main__":
    main()


# def read_list(filename):
#     text_list = []

#     with open(filename, "rt") as text_file:
#         for line in text_file:
#             clean_line = line.strip()
#             text_list.append(clean_line)

#     return text_list


# def main():
#     text_list = read_list("provinces.txt")  # Make sure to provide the correct file name

#     print(text_list)


# if __name__ == "__main":
#     main()
