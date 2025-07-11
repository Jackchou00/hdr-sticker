[简体中文](README_zhCN.md) | English

# HDR Image Conversion with ICC Profile Embedding  

This project demonstrates how to convert images to the Rec.2020 PQ color space and embed ICC profiles for HDR display.  

## Project Structure  

The main files in the project are organized as follows:  

-   [`main.py`](main.py): The main entry point of the application. It coordinates the color space conversion and ICC profile embedding process.  
-   [`color_conversion.py`](color_conversion.py): Converts image color space to Rec.2020 PQ.  
-   [`icc.py`](icc.py): Handles the extraction and embedding of ICC profiles in image files.  

## Setup  

To set up and run this project, follow these steps:  

1.  **Clone the repository:**  
    ```bash  
    git clone [repository_url]  
    cd image-convert  
    ```  

2.  **Set up the virtual environment:**  
    ```bash  
    uv sync  
    ```  

## Usage  

To process an image, run the `main.py` script:  

```bash  
uv run main.py  
```