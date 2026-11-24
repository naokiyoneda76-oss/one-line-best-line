from pathlib import Path

OUTPUT_PATH = "/output/entry.txt"
LINE = "I pay $40 a month to walk past my gym like a hamster with a restraining order."


def main():
    output_path = Path(OUTPUT_PATH)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as output_file:
        output_file.write(LINE)


if __name__ == "__main__":
    main()
