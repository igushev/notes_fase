import os

from fase_lib.tools import deploy_util
from fase_lib.tools import version_util


FASE_LIB_DIR_VAR_NAME = 'FASE_LIB_DIR'
FASE_VERSION_FILENAME_VAR_NAME = 'FASE_VERSION_FILENAME'
HOME_DIR_VAR_NAME = 'NOTES_FASE_DIR'
VERSION_FILENAME_VAR_NAME = 'NOTES_FASE_VERSION_FILENAME'
DEPLOY_DIR_VAR_NAME = 'NOTES_FASE_SERVER_DEPLOY_DIR'
DEPLOY_FILENAME_TEMPLATE = 'NotesFaseServer_Notes_%s_Fase_%s'

def main(argv):
  fase_lib_dir = os.environ[FASE_LIB_DIR_VAR_NAME]
  home_dir = os.environ[HOME_DIR_VAR_NAME]
  deploy_dir = os.environ[DEPLOY_DIR_VAR_NAME]
  assert deploy_dir, '%s must be set!' % DEPLOY_DIR_VAR_NAME

  version_filename = os.environ[VERSION_FILENAME_VAR_NAME]
  version = version_util.ReadAndUpdateVersion(version_filename)
  fase_version_filename = os.environ[FASE_VERSION_FILENAME_VAR_NAME]
  fase_version = version_util.ReadAndUpdateVersion(fase_version_filename)

  deploy_filename = DEPLOY_FILENAME_TEMPLATE % (version.replace('.', '_'), fase_version.replace('.', '_'))
  copy_list = [(fase_lib_dir, os.path.basename(fase_lib_dir))]
  deploy_util.Deploy(home_dir, copy_list, deploy_dir, deploy_filename)


if __name__ == '__main__':
  main(os.sys.argv)
