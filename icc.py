from PIL import Image
import os


def extract_icc_profile(image_path):
    """
    Extracts the ICC profile from an image file.

    Args:
        image_path (str): Path to the image file.
        save (bool): If True, saves the ICC profile to a file named <md5>.icc.

    Returns:
        bytes: The ICC profile data, or None if not found.
    """
    with Image.open(image_path) as img:
        icc_profile = img.info.get("icc_profile")
    return icc_profile


def attach_icc_profile(source_image_path, target_image_path, output_path):
    """
    Extracts ICC profile from a source image and attaches it to a target image,
    then saves the result.

    Args:
        source_image_path (str): Path to the image file from which to extract the ICC profile.
        target_image_path (str): Path to the image file to which the ICC profile will be attached.
        output_path (str): Path to save the output image file with the attached ICC profile.
    """
    icc_profile = extract_icc_profile(source_image_path)
    if icc_profile:
        with Image.open(target_image_path) as img:
            img.save(output_path, icc_profile=icc_profile)
    else:
        print(
            f"No ICC profile found in {source_image_path}. Saving target image without ICC profile."
        )
        with Image.open(target_image_path) as img:
            img.save(output_path)


if __name__ == "__main__":
    # Example usage: Extract ICC from a source image and attach to a target image
    source_img_path = (
        "ori_hdr_image/hdr_frog.png"  # Source image with desired ICC profile
    )
    target_img_path = "output_image.png"  # Image to attach the ICC profile to
    output_img_path = (
        "output_image_with_icc.png"  # Output image with attached ICC profile
    )
    attach_icc_profile(source_img_path, target_img_path, output_img_path)
