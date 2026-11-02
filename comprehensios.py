def get_words(filename):
    with open(filename) as f:
        return f.read().split()

def save_counts(counts):
    with open ("counts.CSV", "w") as f:
        f.write("word,count\n")
        for word, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
            f.write(f"{word},{count}\n")
def main():
    counts = {}
    words = get_words("address.txt")
    lowercase_words = [word.lower() for word in words]

    for word in lowercase_words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    save_counts(counts)
main()