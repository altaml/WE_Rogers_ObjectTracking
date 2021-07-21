import cv2
import os
import logging
from pathlib import Path
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


def videos2frames_frame_number(inputdir: Path, outputdir: Path, frame_number: int):
    """
    convert video to frames based on the requested number of frames.
    """
    assert inputdir.is_dir(), f"{str(inputdir)} does not exist!"
    if not outputdir.is_dir():
        outputdir.mkdir(parents=True, exist_ok=False)

    files = list(x for x in inputdir.iterdir() if x.is_file() and x.suffix == '.mp4')
    logger.info(f'list of video files are: {files}')
    for i in range(len(files)):
        current_output = outputdir / Path(Path(files[i]).name).stem
        logger.info(f'ouputput folder for frames is: {current_output}')
        try:
            os.mkdir(current_output)
        except OSError:
            pass
        logger.info(f'saving the frames for {files[i]}')
        vidcap = cv2.VideoCapture(str(files[i]))
        fps = vidcap.get(cv2.CAP_PROP_FPS)
        fcnt = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
        logger.info(f'framerate:, {fps}')
        logger.info(f'frame count:, {fcnt}')
        logger.info(f'video duration:, {fcnt/fps}')
        count = 0
        save_count = 0
        while True:
            success, image = vidcap.read()
            if not success:
                break
            if count % frame_number == 0:
                cv2.imwrite(str(current_output / 'frame{:d}.jpg'.format(count)), image)
                save_count += 1
                logger.info(f'frame {count} is saved!')
            count += 1


def frame2video_convertor(pathIn: Path, pathOut: Path, fps: int):
    """
    combining all the frames to reconstruct the video.
    """
    frame_array = []
    files = list(x for x in pathIn.iterdir() if x.is_file() and x.suffix == '.jpg')
    logger.info(f'list of files are: {files}')
    files.sort()
    frame_array = []

    assert pathIn.is_dir(), f"{str(pathIn)} does not exist!"
    if not pathOut.is_dir():
        pathOut.mkdir(parents=True, exist_ok=False)
    final_video_name = pathOut / Path('rec_' + pathIn.name + '.mp4')
    logger.info(f'final video file name is:, {final_video_name}')
    for i in range(len(files)):
        filename = files[i]
        # read the frame
        img = cv2.imread(str(filename))
        height, width, layers = img.shape
        size = (width, height)
        # inserting the frames into an image array
        frame_array.append(img)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(str(final_video_name), fourcc, fps, size)

    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    out.release()
