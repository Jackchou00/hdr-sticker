import colour
from PIL import Image
import numpy as np


def convert_to_rec2020_pq(input_image_path, output_image_path, peak_luminance=1600):
    """
    Reads an image, converts its color space to Rec.2020 PQ, and saves the output.

    Args:
        input_image_path (str): Path to the input image file.
        output_image_path (str): Path to save the output image file.
        peak_luminance (int, optional): Peak luminance in nits for PQ conversion. Defaults to 1600.
    """
    with Image.open(input_image_path) as img:
        arr = np.asarray(img)

    # Extract alpha channel if present
    alpha = None
    if arr.shape[-1] == 4:
        alpha = arr[..., 3]
        arr = arr[..., :3]  # Ignore alpha channel for color conversion

    arr = arr / 255.0  # Normalize to [0, 1] range
    arr = colour.eotf(arr, "sRGB")  # Apply sRGB EOTF
    arr = colour.RGB_to_RGB(
        arr, input_colourspace="sRGB", output_colourspace="ITU-R BT.2020"
    )  # Convert sRGB to Rec.2020 color space
    arr = colour.eotf_inverse(
        arr * peak_luminance, "ITU-R BT.2100 PQ"
    )  # Apply PQ EOTF inverse, scaling by peak luminance in nits

    arr = arr * 255.0  # Scale back to [0, 255] range
    arr = arr.astype(np.uint8)  # Convert to uint8 type

    # Add alpha channel back if it was present
    if alpha is not None:
        arr = np.dstack((arr, alpha))
        output_image = Image.fromarray(arr, mode="RGBA")
    else:
        output_image = Image.fromarray(arr, mode="RGB")

    output_image.save(output_image_path, format="PNG")


if __name__ == "__main__":
    # Example usage
    input_img = "example.png"  # Example input image
    output_img = "output_image.png"  # Output image after color conversion
    convert_to_rec2020_pq(input_img, output_img, peak_luminance=1600)
