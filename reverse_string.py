def reverse_string(string: str) -> str:
    if string == "":
        print("the first part")
        return ""
    else:
        lst = list(string.strip())
        # print(lst)
        print("the second part")
        lst.reverse()
        arr = []

        for a in lst:
            arr.append(a)

        string = ""

        for b in arr:
            string += b
        # print(string)
        return string

if __name__ == "__main__":
    reverse_string("")
