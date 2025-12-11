import sys
sys.path.append("src")

from Artwork_record_manager import ArtworkRecordManager

def main():
    print("=== Basic Usage Example ===")

    record = ArtworkRecordManager(
        "Starry Night",
        "Van Gogh, Vincent",
        1889,
        "Painting"
    )

    print(record)
    print(record.to_dict())
    print("Artwork age:", record.get_age(), "years")

if __name__ == "__main__":
    main()
