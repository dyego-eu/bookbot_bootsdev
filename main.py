from collections import Counter, OrderedDict


REPORT_TEMPLATE = """
--- Begin report of {book_name} ---
{report_contents}
--- End report ---
"""

WORD_COUNT_TEMPLATE = "{word_count} were found in the document"
CHARACTER_COUNT_TEMPLATE = "The '{char}' character was found {count} times"

def main():
    book_name = "books/frankenstein.txt"
    with open(book_name) as file:
        book = file.read()

    word_count = count_words(book)
    character_count = count_characters(book)
    report = assemble_report(book_name, character_count, word_count)

    print(report)


def assemble_report(book: str, character_count: dict[str, int], word_count: int):
    word_count_report = WORD_COUNT_TEMPLATE.format(word_count=word_count)
    character_report = "\n".join(
        [
            CHARACTER_COUNT_TEMPLATE.format(char=char, count=count)
            for char, count in character_count.items()
        ]
    )
    report_contents = "\n\n".join([word_count_report, character_report])
    return REPORT_TEMPLATE.format(book_name=book, report_contents=report_contents)


def count_words(book: str) -> int:
    lines = book.split("\n")
    words_in_line = [
        line.split( ) for line in lines
    ]
    return sum([len(line) for line in words_in_line])


def count_characters(book: str) -> dict[str, int]:
    char_counts = dict(Counter(book.lower()))
    char_counts["\\n"] = char_counts["\n"]
    del char_counts["\n"]
    return {
        key: value
        for key, value in sorted(
            char_counts.items(),
            key=lambda item: item[1],
            reverse=True,
        )
        if key.isalpha()
    }


if __name__ == "__main__":
    main()


