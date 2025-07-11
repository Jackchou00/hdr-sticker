from color_conversion import convert_to_rec2020_pq
from icc import attach_icc_profile


def main():
    """
    Main function to orchestrate image processing:
    1. Converts an input image to Rec.2020 PQ color space.
    2. Attaches an ICC profile from a source image to the converted image.
    """
    # Define input and output paths
    input_image_path = "example.png"  # Original image
    converted_image_path = "output_image.png"  # Image after color space conversion
    icc_source_image_path = (
        "ori_hdr_image/hdr_frog.png"  # Image with desired ICC profile
    )
    final_output_image_path = (
        "output_image_with_icc.png"  # Final image with ICC profile
    )

    print(f"Converting {input_image_path} to Rec.2020 PQ...")
    convert_to_rec2020_pq(input_image_path, converted_image_path)
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
