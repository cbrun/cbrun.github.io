# PNG classiques pour favicon et PWA
convert -background none favicon_cb_dark.svg -resize 32x32 favicon-32.png
convert -background none favicon_cb_dark.svg -resize 192x192 favicon-192.png
convert -background none favicon_cb_dark.svg -resize 512x512 favicon-512.png

# Apple touch icon
convert -background none favicon_cb_dark.svg -resize 180x180 apple-touch-icon.png

convert -background none favicon_cb_dark.svg -define icon:auto-resize=16,32,48 favicon.ico


convert -background none favicon_cb_dark.svg -resize 64x64 favicon-64.png
convert -background none favicon_cb_dark.svg -resize 96x96 favicon-96.png

