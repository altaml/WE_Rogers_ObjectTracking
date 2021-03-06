import logging
import argparse
from pathlib import Path
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
import sys
sys.path.append('../')
from data.config import DATA_PATH
from data_utils import frame2video_convertor


if __name__ == '__main__':
    logger.info(f'combining the frames to video and save the results')
    a = argparse.ArgumentParser()
    a.add_argument('--pathIn', help='path to the image folder')
    a.add_argument('--pathOut', help='folder for saving the output video')
    a.add_argument('--fps', help='frame per second', type=int, default=10)
    args = a.parse_args()
    args.pathIn = Path(DATA_PATH / 'Object Detection Results')
    args.pathOut = Path(DATA_PATH / 'Reconstructed Videos')
    logger.info(f'fps is: {args.fps}')
    for folder in args.pathIn.iterdir():
        if folder.is_dir():
            logger.info(f'{folder}')
            frame2video_convertor(folder, args.pathOut, args.fps)

