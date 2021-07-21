import logging
import argparse
from pathlib import Path
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
import sys
sys.path.append('../')
sys.argv=['']; del sys
from data.config import DATA_PATH
from data_utils import videos2frames_frame_number


if __name__ == '__main__':
    logger.info(f"breaking the video to frames and save the results")
    a = argparse.ArgumentParser()
    a.add_argument('--pathIn', help='path to video folder')
    a.add_argument('--pathOut', help='path to the output folder')
    a.add_argument('--fnumber', help='frame gap number for saving')
    args = a.parse_args()
    args.pathIn = Path(DATA_PATH / 'Original Videos')
    args.pathOut = Path(DATA_PATH / 'Original Frames')
    args.fnumber = 2000
    videos2frames_frame_number(args.pathIn, args.pathOut, args.fnumber)


