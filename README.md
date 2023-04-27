# SDK gear to extract slide metadata

This gear uses OpenSlide to extract file metadata from a pathology slide file and inject it as file-level metadata on Flywheel.

## Usage

Run at the session-level (either in batch or on a single session).

### Inputs

File to process 

### Configuration

* __debug__ (boolean, default False): Include debug statements in output.

### Limitations

Current limitations of the gear are as follows:

* 