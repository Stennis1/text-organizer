#!/usr/bin/env bash
set -e

APP_NAME="text-organizer"
VERSION="v1.0.0"
REPO="Stennis1/text-organizer"

INSTALL_DIR="$HOME/.local/bin"
APPIMAGE_NAME="Text_Organizer-x86_64.AppImage"

URL="https://github.com/$REPO/releases/download/$VERSION/$APPIMAGE_NAME"

echo "Installing $APP_NAME..."

mkdir -p "$INSTALL_DIR"

curl -L "$URL" -o "$INSTALL_DIR/$APP_NAME"
chmod +x "$INSTALL_DIR/$APP_NAME"

echo ""
echo "Text Organizer installed successfully!"
echo "Run with:"
echo "  $APP_NAME"
