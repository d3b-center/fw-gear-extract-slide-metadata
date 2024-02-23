"""Main module."""
import logging
import os
from pathlib import Path
import openslide
from fw_gear_extract_slide_metadata.staintype import staintype

from fw_core_client import CoreClient
from flywheel_gear_toolkit import GearToolkitContext
import flywheel

from .run_level import get_analysis_run_level_and_hierarchy

log = logging.getLogger(__name__)

fw_context = flywheel.GearContext()
fw = fw_context.client

def process(input_path):
    """Process `file_path` and returns a `flywheel.FileEntry` and its corresponding meta.

    Args:
        input_path (Path-like): Path to input-file.

    Returns:
        dict: Dictionary of file attributes to update.
        dict: Dictionary containing the file meta.
    """
    obj = openslide.OpenSlide(input_path)
    file_name = Path(input_path).stem
    harmonized_stain_type = staintype(file_name)
    file_dictionary = {}
    # add dimensions
    file_dictionary['Dimensions.Width'] = obj.dimensions[0]
    file_dictionary['Dimensions.Height'] = obj.dimensions[1]
    # adding stain info
    file_dictionary['stain_type'] = file_name
    # add properties
    for item in obj.properties:
        tag_name = '.'.join(item.split('.')[1:]) # remove the leading word
        if tag_name != 'comment':
            log.info(f'ADDING - {tag_name} : {obj.properties[item]}')
            file_dictionary[tag_name] = obj.properties[item]
    fe = {"modality": 'SM - Slide Microscopy', "info": file_dictionary}
    return fe

def run(file_path):
    """Processes file at file_path.

    Args:
        file_type (str): String defining file type.
        file_path (AnyPath): A Path-like to file input.
        project (flywheel.Project): The flywheel project the file is originating
            (Default: None).

    Returns:
        dict: Dictionary of file attributes to update.
        dict: Dictionary containing the file meta.

    """
    fe = process(
        file_path
    )
    return fe
