import os
import shutil
from sklearn.model_selection import train_test_split

def split_data(input_folder, output_folder, test_size=0.2, random_state=42):
    all_images = []
    all_labels = []

    for class_name in os.listdir(input_folder):
        class_path = os.path.join(input_folder, class_name)
        for file_name in os.listdir(class_path):
            file_path = os.path.join(class_path, file_name)
            all_images.append(file_path)
            all_labels.append(class_name)

    train_images, temp_images, train_labels, temp_labels = train_test_split(
        all_images, all_labels, test_size=test_size, random_state=random_state, stratify=all_labels
    )

    val_images, test_images, val_labels, test_labels = train_test_split(
        temp_images, temp_labels, test_size=0.5, random_state=random_state, stratify=temp_labels
    )

    train_folder = os.path.join(output_folder, 'train')
    val_folder = os.path.join(output_folder, 'validation')
    test_folder = os.path.join(output_folder, 'test')

    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(val_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)

    copy_files(train_images, train_labels, train_folder)
    copy_files(val_images, val_labels, val_folder)
    copy_files(test_images, test_labels, test_folder)

def copy_files(image_paths, labels, output_folder):
    for image_path, label in zip(image_paths, labels):
        image_name = os.path.basename(image_path)
        output_label_folder = os.path.join(output_folder, label)
        os.makedirs(output_label_folder, exist_ok=True)

        shutil.copy(image_path, os.path.join(output_label_folder, image_name))


if __name__ == "__main__":
    # Specify input and output folders
    input_folder = './data_raw'
    output_folder = './data'

    # Split data and create train, validation, and test sets
    split_data(input_folder, output_folder)
