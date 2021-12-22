#!/bin/sh
# Usage: Inside the gryff/experiments/nsdi20 folder, run ./initialize_experiment_configs.sh

# Purpose: This script modifies the following variables in the JSON config files in gryff/experiments/nsdi20:
  # "base_local_exp_directory" --> path to a directory on your local machine in which you want the experiment results stored
  # "base_remote_bin_directory_nfs" --> path to a directory on the experiment machines in which the client/server binaries will be stored. For example, this could be a subdirectory in your home directory
  # "emulab_user" --> username for CloudLab account
  # "experiment_name" --> name of experimented instantiated from profile
  # "project_name" --> name of Cloudlab project associated with Cloudlab account
  # "src_directory"--> path to the directory on your local machine that contains the git repository
  # "default_remote_shell" --> the type of shell that you have configured for your account on CloudLab. In theory "bash" should work as a value, but I haven't recently tested these scripts with "bash". It may be safer to try "tcsh" initially.
  # "server_host_format_str" --> the domain suffix should match the cluster in which you've instantiated the experiment. The experiments in the paper were run on the Emulab cluster, but if you want to run on, e.g., CloudLab Utah, you can change the suffix to "utah.cloudlab.us"
  # "client_host_format_str" --> same as above

# --------------------------- change settings here ----------------------------------
# Edit these variables, and the rest will be configured automatically.
EMULAB_USER="zhouaea"
EXPERIMENT_NAME="gryff"
PROJECT_NAME="HyflowTM"
DEFAULT_REMOTE_SHELL="tcsh"
HOST_FORMAT_STR_SUFFIX="emulab.net" # Used to configure SERVER_HOST_FORMAT_STR and CLIENT_HOST_FORMAT_STR.
# -----------------------------------------------------------------------------------

# Automatically configure other variables except base_local_exp_directory.
SRC_DIRECTORY=/users/"${EMULAB_USER}/epaxos" # Gryff folder should be in this location.
BASE_REMOTE_BIN_DIRECTORY_NFS="${SRC_DIRECTORY}" # Client/server binaries are stored in <user>/epaxos.
SERVER_HOST_FORMAT_STR="%s.%s.%s.${HOST_FORMAT_STR_SUFFIX}"
CLIENT_HOST_FORMAT_STR="client-%d-%d.%s.%s.${HOST_FORMAT_STR_SUFFIX}"

# Modify each config file (and configure experiment result folder location).
for FILENAME in *.json
do
  # Configure base_local_exp_directory for each json file.
  EXPERIMENT_CONFIG_NAME=`echo $FILENAME | cut -d'.' -f 1` # Extract the .json from the filename
  BASE_LOCAL_EXP_DIRECTORY="${SRC_DIRECTORY}/results/$EXPERIMENT_CONFIG_NAME" # base_local_exp_directory results are stored in gryff/results/<experiment>

  # Note 1: The replaced lines don't have tabs like the original lines, but whitespace doesn't matter in json.
  # Note 2: If this script is being run on MacOS, change each occurence of "sed" to "gsed".
  sed -i "/\"base_local_exp_directory\":/c \"base_local_exp_directory\": \"${BASE_LOCAL_EXP_DIRECTORY}\"," ./$FILENAME
  sed -i "/\"base_remote_bin_directory_nfs\":/c \"base_remote_bin_directory_nfs\": \"${BASE_REMOTE_BIN_DIRECTORY_NFS}\"," ./$FILENAME
  sed -i "/\"emulab_user\":/c \"emulab_user\": \"${EMULAB_USER}\"," ./$FILENAME
  sed -i "/\"experiment_name\":/c \"experiment_name\": \"${EXPERIMENT_NAME}\"," ./$FILENAME
  sed -i "/\"project_name\":/c \"project_name\": \"${PROJECT_NAME}\"," ./$FILENAME
  sed -i "/\"src_directory\":/c \"src_directory\": \"${SRC_DIRECTORY}\"," ./$FILENAME
  sed -i "/\"default_remote_shell\":/c \"default_remote_shell\": \"${DEFAULT_REMOTE_SHELL}\"," ./$FILENAME
  sed -i "/\"server_host_format_str\":/c \"server_host_format_str\": \"${SERVER_HOST_FORMAT_STR}\"," ./$FILENAME
  sed -i "/\"client_host_format_str\":/c \"client_host_format_str\": \"${CLIENT_HOST_FORMAT_STR}\"," ./$FILENAME

  echo "$FILENAME configured"
done