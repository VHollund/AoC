from Helpers.GetInput import get_input_split_lines

def sanitize(data):
    nd=[]
    for x in data:
        removeNL=x.replace("\n", "")
        nd.append(removeNL)
    return nd


if __name__ == "__main__":
    data = get_input_split_lines(2021, "04")
    data = sanitize(data)
