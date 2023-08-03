#!/bin/bash

repos=(
  "/home/ubuntu/muiva_app"
)

echo ""
echo "Getting latest for" ${#repos[@]} "repositories using git pull"

for repo in "${repos[@]}"
do
  echo ""
  echo "****** Getting latest for" ${repo} "******"
  cd "${repo}"
  git reset --hard
  git pull
  echo "******************************************"
  echo ""
  echo "Restarting systemclt"
  echo ""
done
  sudo systemctl stop muiva.service
  sudo systemctl start muiva.service
  sudo systemctl status muiva.service