#!/bin/bash

cd ~
wget https://blzdistsc2-a.akamaihd.net/Linux/SC2.4.10.zip
unzip -P iagreetotheeula SC2.4.10.zip -d ~/

export SC2PATH="$HOME/StarCraftII"

git clone https://github.com/oxwhirl/smac.git
cp -r smac/smac/env/starcraft2/maps/SMAC_Maps $SC2PATH/Maps/