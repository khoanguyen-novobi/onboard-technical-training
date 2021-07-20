"""
This is exercise of string
"""


def exercise_string_file(
    input_path="python-exercises/assignment/string/text.txt",
    output_path="python-exercises/assignment/string/output.txt",
):

    # Read the input file
    file_read = open(input_path, "r")
    d = dict()
    for line in file_read:
        line = line.strip()
        words = line.split(" ")

        # Count word frequency
        for word in words:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1

    # Read the output file
    file_write = open(output_path, "w")

    # Write all word which has frequency larger than 1
    file_write.write(",".join([k for k, v in d.items() if v > 1]))

    # Print out the count of appearence for each word.
    for key, value in d.items():
        print(key, value)

    # Print the times that the word appear, or print out a message saying it does not exist if no
    find_word = input("Input your word: ")
    print(d[find_word]) if find_word in d else print("it does not exist")

    # Print the first 100 characters of the string.
    one_big_str = "".join([k for k in d.keys()])
    print(one_big_str[:100])
