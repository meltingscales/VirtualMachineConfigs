#!/usr/bin/env bash

if [ ! -f /minecraft/start.sh ]; then
  mv /minecraft-unzipped/BM_Exosphere_2.0.2_server /minecraft
fi

echo "eula=true" > /minecraft/BM_Exosphere_2.0.2_server/eula.txt

bash /minecraft/BM_Exosphere_2.0.2_server/start.sh
