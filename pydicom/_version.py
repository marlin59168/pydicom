"""Pure python package for DICOM medical file reading and writing."""
import re


__version__ = '2.1.0.dev0'
__version_info__ = tuple(
    re.match(r'(\d+\.\d+\.\d+).*', __version__).group(1).split('.'))


# DICOM Standard version used for:
#   _dicom_dict, _uid_dict and _storage_sopclass_uids
__dicom_version__ = '2020d'
