Changelog
=========

[Upcoming]
----------

### Fixed

- Suppress `DeprecationWarning`s from `importlib.resources` on Python 3.9+
- Add missing LICENSE file and PyPI classifiers


[0.4.1] - 2021-06-21
--------------------

### Fixed

- Added missing post-processing call for structs


[0.4.0] - 2021-06-21
--------------------

### Changed

- Mapping interface to `Hdf5Matfile` doesn't load a variable from disk; instead
  it returns a Loader that can be indexed

### Added

- Add support for indexing/partial loading
- Progress towards full test coverage


[0.3.1] - 2021-05-06
--------------------

### Changed

- Only translate OSErrors with 'file signature not found' to 'cannot open as
  HDF5'. Could be other OSErrors raised by h5py.


[0.3.0] - 2021-05-06
--------------------

### Fixed

- Transpose arrays (MATLAB is column-major, woops)
- Don't throw AttributeError when deleting partially-initialized objects

### Changed

- Change how squeezing works for scalars: use indexing instead of `.item()`.
- Make some h5py file not found/file not valid errors more helpful.
  FileNotFoundError is thrown instead of OSError when file not found. Files that
  exist, but are invalid HDF5 have a better error message.
- Throw MatlabDecodeError instead of re-raising KeyError when item has no
  'MATLAB_class' attribute (and therefore can't be decoded).

### Added

- Add mapping interface to Hdf5Matfile (dict-like indexing, `.keys()`,
  `.values()`, etc.)
- Squeezing can be controlled after init with the 'squeeze' attribute.
- Add (incomplete) unit tests.
