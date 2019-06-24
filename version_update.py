import os

from fase_lib.tools import version_util


VERSION_FILENAME_VAR_NAME = 'NOTES_FASE_VERSION_FILENAME'


def main(argv):
  assert len(argv) <= 2
  update_position = int(argv[1]) if len(argv) == 2 else None
  version_filename = os.environ[VERSION_FILENAME_VAR_NAME]
  version_util.ReadAndUpdateVersion(version_filename, update_position)


if __name__ == '__main__':
  main(os.sys.argv)
