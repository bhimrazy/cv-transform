import argparse
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def flip_image(img: np.ndarray, axis=0) -> np.ndarray:
    """Flips image

    axis: 0 -> vertical flip
    axis: 1 -> horizontal flip
    """
    # your code goes here
    if axis:
        # horizontal flip | axis 1
        return img[:, ::-1]

    # vertical flip | axis 0
    return img[::-1, :]


def main(args):
    # Retrieve the argument values
    img_path = args.image_path
    flip_axis = args.flip
    out_path = args.output_path

    # Assert that the provided arguments are not empty
    assert img_path, "Image path argument is required."
    assert flip_axis != None, "Flip axis argument is required."
    assert out_path, "Output path argument is required."

    # Load the image
    print("Loading Image from:", img_path)
    image = Image.open(img_path)

    # image array
    img_arr = np.asarray(image)

    # apply flip
    print("Applying flipping transformation...")
    flipped_img = flip_image(img=img_arr, axis=flip_axis)

    # Create a figure with two subplots
    fig, (ax1, ax2,ax3, ax4) = plt.subplots(1, 4, figsize=(12, 4))

    # Set the title of the figure
    fig.suptitle("Image Transformations Grid")

    # Set the title and display the original image in the first subplot
    ax1.set_title("Original Image")
    ax1.imshow(img_arr)
    ax1.axis("off")  # Turn off the axes
    ax1.grid(False)  # Hide grid lines

    # Set the title and display the flipped image in the second subplot
    ax2.set_title("Flipped Image")
    ax2.imshow(flipped_img)
    ax2.axis("off")  # Turn off the axes
    ax2.grid(False)  # Hide grid lines

    rand_flip_img = lambda x: flip_image(x,np.random.randint(0,2)) 

    # Set the title and display the rand flipped image in the third subplot
    ax3.set_title("R. Flipped Image")
    ax3.imshow(rand_flip_img(img_arr))
    ax3.axis("off")  # Turn off the axes
    ax3.grid(False)  # Hide grid lines

    # Set the title and display the flipped image in the fourth subplot
    ax4.set_title("R. Flipped Image")
    ax4.imshow(rand_flip_img(img_arr))
    ax4.axis("off")  # Turn off the axes
    ax4.grid(False)  # Hide grid lines

    # Adjust the layout of the subplots
    plt.tight_layout()

    # Save the figure to the specified output path
    plt.savefig(out_path)

    # Display a confirmation message
    print(f"Image grid saved at: {out_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Image Transformation Script")

    parser.add_argument("-i", "--image_path", type=str, help="Path to the image")
    parser.add_argument("-f", "--flip", type=int, help="Flip Image. 0 for vertical and 1 Horizontal")
    parser.add_argument("-o", '--output_path', type=str, help='Path to save the rotated image')

    args = parser.parse_args()
    main(args)
