"""
    Datasets will be generated using the The LJ Speech Dataset format, generating a transcript.csv for each character.
        
        ID: this is the name of the corresponding .wav file
        Transcription: words spoken by the reader (UTF-8)
        Normalized Transcription: transcription with numbers, ordinals, and monetary units expanded into full words (UTF-8).

"""

import sys
import argparse
import re
import csv
import os
import cv2

def sanitize_subtitles(subtitles:list) -> list:
    """
        Removes multilines from subtitles if the names don't appear in the subtitles.
        Changes numbers to written numbers.

        Parameters
        ----------
        subtitles : list
            A list of the subtitles

        Returns
        -------
        list
            A list of the subtitles who has been sanitized
    """
    subtitles_sanitized = []

    #ToDo - Go through the subtitles and find multilines to remove them
    #ToDo - While doing the last loop, change every numbers to written numbers

    return subtitles_sanitized


def add_names_to_subtitles(subtitles:list, transcript:list) -> list:
    """
        Add names found in the transcript to the subtitles lines.

        Parameters
        ----------
        subtitles : list
            A list of the subtitles
        transcript : list
            A list of the transcript lines

        Returns
        -------
        list
            A list of the subtitles with the names of the characters appended to them
    """
    new_subtitles = []
    
    #ToDo - Go through the transcript and match subtitles lines
    #ToDo - Add the name at the beginning of the subtitles lines

    return new_subtitles

def video_to_lfspeech(subtitles:list, video:str, transcript:list, odir:str):
    """
        Creates one CSV transcipt file per character found in the subtitles
        and generates the corresponding WAV files.

        Parameters
        ----------
        subtitles : list
            A list of the subtitles
        video : str
            The path to the video file
        transcript : list
            A list of the transcript lines
        odir : str
            Path to the output directory for the generated transcripts datasets
    """
    # Makes the subtitles readable according to the LFSpeech dataset
    subtitles = sanitize_subtitles(subtitles)
    # If a transcript is found, add the names of the characters to the subtitles
    if transcript:
        subtitles = add_names_to_subtitles(subtitles, transcript)
    #Load the video in opencv
    cap = cv2.VideoCapture(video)
    #ToDo - Go through the subtitles and video to get clips
    #ToDo - Save which clip belong to which subtitle in a map
    #ToDo - Save the clips to the output directory
    #ToDo - Close the video and save the CSV from the map

if __name__ == '__main__':   
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('-s', '--subtitles', help='Path to the subtitles file.', type=str, required=True)
    argument_parser.add_argument('-v', '--video', help='Path to the video file.', type=str, required=True)
    argument_parser.add_argument('-o', '--output_directory', help='Path to the output audio files.', type=str, default='./')
    argument_parser.add_argument('-t', '--transcript', help='Path to the transcript of the video. \
                                                            If the subtitles do not contain the names of the \
                                                            characters in the format of "Character-" or "Character:" \
                                                            the program will look for names in the transcript.', type=str, default=None)
    args = argument_parser.parse_args()

    sub = args.subtitles
    vid = args.video
    tscript = args.transcript
    
    if tscript is not None:
        if not os.path.exists(os.path.abspath(tscript)):
            print('Could not load the path to the video. Exiting...')
            sys.exit(3)
        else:
            with open(os.path.abspath(tscript), 'r', encoding='utf-8') as f:
                tscript = f.read()
    if not os.path.exists(os.path.abspath(vid)):
        print('Could not load the path to the video. Exiting...')
        sys.exit(1)

    if not os.path.exists(os.path.abspath(sub)):
        print('Could not load the path to the subtitles. Exiting...')
        sys.exit(2)
    else:
        with open(os.path.abspath(sub), 'r', encoding='utf-8') as f:
            sub = f.read()

    video_to_lfspeech(sub, vid, tscript, args.output_directory)
    