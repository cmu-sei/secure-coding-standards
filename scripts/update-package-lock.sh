#!/usr/bin/env bash

original1="https:\/\/artifacts.sei.cmu.edu:443\/artifactory\/api\/npm\/npm-remote\/"
replacement1="https:\/\/registry.npmjs.org\/"
original2="https:\/\/artifacts.sei.cmu.edu:443\/artifactory\/api\/npm\/sei-design-system-remote\/"
replacement2="https:\/\/npm.pkg.github.com\/"
filename="package-lock.json"

if [ ! -f "$filename" ]; then
  echo "File $filename not found!"
  exit 1
fi

if [[ "$OSTYPE" == "darwin"* ]]; then
  sed -i.bak "s/$original1/$replacement1/g" "$filename" && rm -f "${filename}.bak"
  sed -i.bak "s/$original2/$replacement2/g" "$filename" && rm -f "${filename}.bak"
else
  sed -i "s/$original1/$replacement1/g" "$filename"
  sed -i "s/$original2/$replacement2/g" "$filename"
fi

if [ $? -eq 0 ]; then
  echo "Successfully updated $filename"
else
  echo "Failed to update $filename"
  exit 1
fi