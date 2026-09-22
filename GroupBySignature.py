def group_by_signature(words: list) -> list:
    groups = {}
    order = []
 
    for word in words:
        if word == "":
            continue
        signature = "".join(sorted(word.lower()))
        if signature not in groups:
            groups[signature] = []
            order.append(signature)
        groups[signature].append(word)
 
    return [groups[sig] for sig in order]
 
 
 
if __name__ == "__main__":
    # Example 1
    words = ["abc", "bca", "cab", "bac", "xyz", "yxz", "zxy", "dog"]
    print(group_by_signature(words))
    # Output: [["abc", "bca", "cab", "bac"], ["xyz", "yxz", "zxy"], ["dog"]]

    # Example 2
    words = ["apple", "pale", "leap", "plea", "papel", "hello"]
    print(group_by_signature(words))
    # Output: [["apple", "papel"], ["pale", "leap", "plea"], ["hello"]]
