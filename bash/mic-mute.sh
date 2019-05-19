#!/usr/bin/env bash

# A script that toggles the microphone.

# NOTE: `0` may not refer to your actual mic if it's a webcam.
# ID of your microphone.
MIC_ID=0;

MIC_ON_MSG="Turning mic on..."
MIC_OFF_MSG="Turning mic off..."

# A file that stores whether or not the microphone should be on.
MIC_ON_FILE=/tmp/MIC_TOGGLE_SCRIPT.txt;

# Set it to 'on' by default.
if [[ ! -e ${MIC_ON_FILE} ]]; then
  echo 1 > ${MIC_ON_FILE};
fi

# If our mic should be on,
if grep -q "1" "${MIC_ON_FILE}"; then

  echo ${MIC_ON_MSG}
  notify-send "$0" "${MIC_ON_MSG}"

  # Turn it on,
  amixer -c ${MIC_ID} sset Mic cap;

  # Record that our mic should be off.
  echo "0" > ${MIC_ON_FILE}
  exit;
fi

# If our mic should be off,
if grep -q "0" "${MIC_ON_FILE}"; then

  echo "${MIC_OFF_MSG}"
  notify-send "$0" "${MIC_OFF_MSG}"

  # Turn it off,
  amixer -c ${MIC_ID} sset Mic nocap;

  # Record that our mic should be on.
  echo "1" > ${MIC_ON_FILE}
  exit;
fi

# If we've got this far, something's wrong!
echo "Something went wrong!"
notify-send "$0" "Something went wrong!"
rm ${MIC_ON_FILE}
