from collections import Counter


def analyze_text(text):
    words = text.lower().split()

    cleaned_words = []

    for word in words:
        cleaned = word.strip(".,!?;:\"'()[]{}")
        if cleaned:
            cleaned_words.append(cleaned)

    if not cleaned_words:
        return None

    frequencies = Counter(cleaned_words)

    return {
        "words": len(cleaned_words),
        "unique_words": len(set(cleaned_words)),
        "characters": len(text),
        "longest_word": max(cleaned_words, key=len),
        "most_common": frequencies.most_common(5),
        "reading_time": max(1, round(len(cleaned_words) / 200))
    }


def display_results(results):
    print("\n--- Text Analysis ---")
    print(f"Words: {results['words']}")
    print(f"Unique words: {results['unique_words']}")
    print(f"Characters: {results['characters']}")
    print(f"Longest word: {results['longest_word']}")
    print(f"Estimated reading time: {results['reading_time']} minute(s)")

    print("\nMost common words:")

    for word, count in results["most_common"]:
        print(f"  {word}: {count}")


def main():
    print("TextLens")
    print("Enter a paragraph to analyze.")
    print("Press Enter twice when you're finished.\n")

    lines = []

    while True:
        line = input()

        if line == "":
            break

        lines.append(line)

    text = " ".join(lines)
    results = analyze_text(text)

    if results is None:
        print("\nNo text was entered.")
        return

    display_results(results)


if __name__ == "__main__":
    main()