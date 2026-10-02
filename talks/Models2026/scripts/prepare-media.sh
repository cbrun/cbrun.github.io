#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p assets/media

# Source recordings are already edited demonstrations; preserve their speed.
clip() {
  ffmpeg -hide_banner -loglevel error -y -ss "$3" -i "../videos/$1.mp4" \
    -t "$4" -an -vf scale=1920:-2 -c:v libx264 -preset fast -crf 20 \
    -threads 2 -pix_fmt yuv420p -movflags +faststart "assets/media/$2.mp4"
}

clip '2 - Understanding a Model' trace 27 27
clip '3-4 - Analysis - Consistency - Automation of the model' failure 54 29
clip '3-4 - Analysis - Consistency - Automation of the model' decompression 84 32
clip '3-4 - Analysis - Consistency - Automation of the model' consistency 117 29
clip '6 - Importing Data' aeb 0 91.567
clip 'demo-syson-capella-extension' syson 80 38.767

# Opening question, then the final choice of engineering activity.
ffmpeg -hide_banner -loglevel error -y \
  -t 26 -i '../videos/1 - Arcadia-Capella Discovery.mp4' \
  -ss 164 -t 27 -i '../videos/1 - Arcadia-Capella Discovery.mp4' \
  -filter_complex '[0:v]setpts=PTS-STARTPTS,scale=1920:-2[a];[1:v]setpts=PTS-STARTPTS,scale=1920:-2[b];[a][b]concat=n=2:v=1:a=0[v]' \
  -map '[v]' -an -c:v libx264 -preset fast -crf 20 -threads 2 \
  -pix_fmt yuv420p -movflags +faststart assets/media/discovery.mp4

for name in trace failure decompression consistency discovery aeb syson; do
  ffmpeg -hide_banner -loglevel error -y -i "assets/media/$name.mp4" \
    -frames:v 1 -q:v 2 "assets/media/$name.jpg"
done
