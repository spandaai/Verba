# Prerequisites Installation Guide

This guide details how to install and configure the required dependencies for unstructured file imports: Tesseract OCR, Poppler, and LibreOffice across different operating systems.

## Table of Contents
- [Windows Installation](#windows-installation)
- [macOS Installation](#macos-installation)
- [Linux Installation](#linux-installation)
- [Verifying Installations](#verifying-installations)
- [Troubleshooting](#troubleshooting)

## Windows Installation

### 1. Tesseract OCR
**Method 1 - Installer (Recommended):**
1. **Download Tesseract:**
   * Go to: https://github.com/UB-Mannheim/tesseract/wiki
   * Download latest installer (64-bit recommended)
   * Current latest: "tesseract-ocr-w64-setup-5.3.1.20230401.exe"

2. **Install:**
   * Run the installer
   * Keep default options
   * Note installation path (default: `C:\Program Files\Tesseract-OCR`)

3. **Add to PATH:**
   * Right-click 'This PC' → Properties
   * Click 'Advanced system settings'
   * Click 'Environment Variables'
   * Under 'System Variables', find 'Path'
   * Click 'Edit' → 'New'
   * Add `C:\Program Files\Tesseract-OCR`
   * Click 'OK' on all windows

### 2. Poppler
**Method 1 - Manual (Recommended):**
1. **Download:**
   * Go to: https://github.com/oschwartz10612/poppler-windows/releases/
   * Download latest release zip

2. **Install:**
   * Create folder: `C:\Program Files\poppler`
   * Extract zip into this folder

3. **Add to PATH:**
   * Open System Properties (as above)
   * Add `C:\Program Files\poppler\bin`

### 3. LibreOffice
1. **Download:**
   * Go to: https://www.libreoffice.org/download/download/
   * Download Windows x64 installer (.msi)

2. **Install:**
   * Run the .msi file
   * Choose "Typical" installation
   * Check "Register as default application"

3. **Add to PATH:**
   * Add `C:\Program Files\LibreOffice\program`

## macOS Installation

### Using Homebrew (Recommended)
1. **Install Homebrew** (if not installed):
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. **Install All Dependencies:**
```bash
# Install Tesseract
brew install tesseract

# Install Poppler
brew install poppler

# Install LibreOffice
brew install --cask libreoffice
```

3. **Add to PATH** (add to ~/.zshrc or ~/.bash_profile):
```bash
# For Tesseract
export PATH="/usr/local/bin:$PATH"

# For LibreOffice
export PATH="/Applications/LibreOffice.app/Contents/MacOS:$PATH"
```

4. **Reload Profile:**
```bash
source ~/.zshrc  # or ~/.bash_profile
```

## Linux Installation (Ubuntu/Debian)

### 1. Tesseract
```bash
# Install Tesseract and English language pack
sudo apt-get update
sudo apt-get install tesseract-ocr
sudo apt-get install tesseract-ocr-eng
```

### 2. Poppler
```bash
# Install Poppler utils
sudo apt-get update
sudo apt-get install poppler-utils
```

### 3. LibreOffice
```bash
# Install LibreOffice
sudo apt-get update
sudo apt-get install libreoffice
```

For other Linux distributions, use the appropriate package manager:
- Fedora/RHEL: Use `dnf` instead of `apt-get`
- Arch Linux: Use `pacman`
- openSUSE: Use `zypper`

## Verifying Installations

Open terminal/command prompt and verify each installation:

**Windows:**
```cmd
tesseract --version
pdfinfo -v
soffice --version
```

**macOS/Linux:**
```bash
tesseract --version
pdfinfo -v
soffice --version
```

## Troubleshooting

### Windows Issues

1. **Command Not Found:**
   * Verify PATH entries
   * Restart command prompt
   * Restart computer

2. **DLL Errors:**
   * Install Visual C++ Redistributable:
     * Download both x86 and x64: [Visual C++ Downloads](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist)

### macOS Issues

1. **Command Not Found:**
```bash
# Verify Homebrew installation
brew doctor

# Verify PATH
echo $PATH

# Reinstall if needed
brew reinstall tesseract
brew reinstall poppler
brew reinstall --cask libreoffice
```

2. **Permission Issues:**
```bash
# Fix permissions
sudo chown -R $(whoami) $(brew --prefix)/*
```

### Linux Issues

1. **Package Conflicts:**
```bash
# Fix broken installations
sudo apt --fix-broken install

# Clean and update
sudo apt-get clean
sudo apt-get update
```

2. **Missing Dependencies:**
```bash
# Install common dependencies
sudo apt-get install build-essential
```

### Still Having Issues?

1. Check installation logs:
   * Windows: Event Viewer
   * macOS: Console app
   * Linux: `/var/log/` directory

2. For help:
   * Open an [issue](../issues/new)
   * Include your:
     * Operating System and version
     * Installation method used
     * Complete error message
     * Output of version check commands

---

For additional assistance, please refer to our [Issues](../issues) page or open a new issue.
