from pathlib import Path
import random
import shutil

SOURCE = Path("data")
DEST = Path("data_ei")

CLASSES = [
    "healthy",
    "early_blight",
    "late_blight",
]

TEST_RATIO = 0.20
SEED = 42

random.seed(SEED)


def prepare_dataset():
    for class_name in CLASSES:
        source_dir = SOURCE / class_name
        train_dir = DEST / "train" / class_name
        test_dir = DEST / "test" / class_name

        train_dir.mkdir(parents=True, exist_ok=True)
        test_dir.mkdir(parents=True, exist_ok=True)

        files = [
            f for f in source_dir.iterdir()
            if f.is_file()
        ]

        random.shuffle(files)

        test_count = round(len(files) * TEST_RATIO)

        test_files = files[:test_count]
        train_files = files[test_count:]

        for file in train_files:
            shutil.copy2(file, train_dir / file.name)

        for file in test_files:
            shutil.copy2(file, test_dir / file.name)

        print(
            f"{class_name}: "
            f"train={len(train_files)}, "
            f"test={len(test_files)}, "
            f"total={len(files)}"
        )


if __name__ == "__main__":
    prepare_dataset()
    print("\nDataset preparation complete.")