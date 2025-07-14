[简体中文](README_zhCN.md) | English

# HDR Image Conversion with ICC Profile Embedding

This project demonstrates how to convert images to the Rec.2020 PQ color space and embed ICC profiles for HDR display.

## Project Structure

The main files in the project are organized as follows:

-   [`main.py`](main.py): The main entry point of the application. It coordinates the color space conversion and ICC profile embedding process.
-   [`color_conversion.py`](color_conversion.py): Converts image color space to Rec.2020 PQ.
-   [`icc.py`](icc.py): Handles the extraction and embedding of ICC profiles in image files.

## Sample Images

- ori_hdr_image/hdr_frog.png
- ori_hdr_image/hdr_mashiro.png

Two HDR stickers collected from QQ group chats, each with different embedded ICC profiles. Used for ICC extraction, selected via `icc_source_image_path` in main.py.

- example.png

A standard sticker assumed to be in sRGB color space. This will be converted to Rec.2020 PQ space and embedded with an ICC profile.

## Setup

To set up and run this project, follow these steps:

1.  **Clone the repository:**
    ```bash  
    git clone https://github.com/Jackchou00/hdr-sticker
    cd hdr-sticker 
    ```  

2.  **Set up virtual environment:**
    ```bash
    uv sync
    ```

## Usage

To process an image, run the `main.py` script:

```bash
uv run main.py
```

Settings can be customized in `config.toml`:

```toml
[paths]
input_image          = "example.png"                 # input image file name
converted_image      = "output_image.png"            # intermediate converted image
icc_source_image     = "ori_hdr_image/hdr_frog.png"  # ICC profile source image
final_output_image   = "output_image_with_icc.png"   # final saved image

[color_conversion]
peak_luminance = 1600   # Peak luminance in nits
```

Adjust these parameters to change which images are processed or tune the HDR peak luminance.

Default input image: `example.png`  
Default output: `output_image_with_icc.png`

**Important Notes for QQ:**
- Regular "images" cannot trigger HDR brightness through ICC profiles in QQ
- To enable HDR, send as an "animated sticker" by:  
  `1. Send the image → 2. Long press → 3. Select "Add as sticker"`

**Platform Compatibility:**
- iOS (OLED devices): Can trigger HDR brightness
- macOS & Windows: Uses ICC tone mapping (processed stickers display normally)
- Android: May not display correctly