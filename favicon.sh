# Favicon PNGs
magick favicon_cb_dark.svg -background none -alpha on -resize 32x32   PNG32:favicon-32.png
magick favicon_cb_dark.svg -background none -alpha on -resize 64x64   PNG32:favicon-64.png
magick favicon_cb_dark.svg -background none -alpha on -resize 96x96   PNG32:favicon-96.png
magick favicon_cb_dark.svg -background none -alpha on -resize 192x192 PNG32:favicon-192.png
magick favicon_cb_dark.svg -background none -alpha on -resize 512x512 PNG32:favicon-512.png

# Apple touch icon
magick favicon_cb_dark.svg -background none -alpha on -resize 180x180 PNG32:apple-touch-icon.png

# ICO with multiple sizes (transparency preserved)
magick favicon_cb_dark.svg -background none -alpha on -define icon:auto-resize=16,32,48 favicon.ico
