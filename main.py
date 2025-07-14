import tomllib
from color_conversion import convert_to_rec2020_pq
from icc import attach_icc_profile


def main():
    """
    Main function to orchestrate image processing:
    1. Converts an input image to Rec.2020 PQ color space.
    2. Attaches an ICC profile from a source image to the converted image.
    """
    # Load configuration from TOML file
    with open("config.toml", "rb") as f:
        config = tomllib.load(f)
    
    # Extract paths and parameters from config
    paths = config["paths"]
    input_image_path = paths["input_image"]
    converted_image_path = paths["converted_image"]
    icc_source_image_path = paths["icc_source_image"]
    final_output_image_path = paths["final_output_image"]
    
    peak_luminance = config["color_conversion"]["peak_luminance"]

    print(f"Converting {input_image_path} to Rec.2020 PQ...")
    convert_to_rec2020_pq(input_image_path, converted_image_path, peak_luminance)
    print(f"Image converted and saved to {converted_image_path}")

    print(
        f"Attaching ICC profile from {icc_source_image_path} to {converted_image_path}..."
    )
    attach_icc_profile(
        icc_source_image_path, converted_image_path, final_output_image_path
    )
    print(f"Final image with ICC profile saved to {final_output_image_path}")


if __name__ == "__main__":
    main()
