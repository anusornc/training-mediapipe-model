import argparse
import glob
import logging
import os
from utils import MediapipeManager


def main(input_folder):
    logging.info("Walking through the input folder.")
    file_list = [files for files in glob.glob(os.path.abspath(input_folder) + "**/*.mp4",
                                              recursive=True)]

    if len(file_list) == 0:
        raise FileNotFoundError

    mediapipe = MediapipeManager("data/")
    try:
        for file_path in file_list:
            mediapipe.run_mediapipe(file_path)
        logging.info("Execution has been completed.")
    except ProcessLookupError:
        print(ProcessLookupError)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run mediapipe framework.")
    parser.add_argument("-i", "--input_data_path",
                        help="Folder containing files with .mp4 \
                              extension to be converted by mediapipe",
                        required=True)
    arguments = parser.parse_args()
    input_data_path = arguments.input_data_path
    main(input_data_path)