# Text Organizer

A lightweight Linux desktop utility for transforming text.

## Features
- Construct text from comma-separated input
- Strip leading/trailing whitespace per line
- Split text into one-item-per-line output
- Native Linux GUI
- No internet required
- Open source

## Application Screenshot 
![Image of Application](./assets/app-screenshot.png)

## Install

### Option 1: AppImage (recommeded)
Download the AppImage from the [Releases page](https://github.com/Stennis1/text-organizer/releases).

```bash
chmod +x Text_Organizer-x86_64.AppImage
./Text_Organizer-x86_64.AppImage
```

### Option 2: One-liner install

```bash
curl -fsSL https://raw.githubusercontent.com/Stennis1/text-organizer/main/install.sh | bash
text-organizer
```

## NOTE
- AppImages may not run on Ubuntu 25.04 due to FUSE limitations

- Works correctly on Ubuntu 20.04 / 22.04 and most Linux distros