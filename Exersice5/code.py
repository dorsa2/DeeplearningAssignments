import numpy as np
from PIL import Image
import zipfile

# Step 1: Generate a sample RGB image (100x100) with random colors
np.random.seed(42)
rgb_image = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)

# Save the original RGB image
Image.fromarray(rgb_image).save("rgb_image.png")

# Step 2: Convert RGB to Grayscale without using image processing libraries
def rgb_to_grayscale(rgb_img):
    r = rgb_img[:,:,0].astype(float)
    g = rgb_img[:,:,1].astype(float)
    b = rgb_img[:,:,2].astype(float)
    gray = 0.299*r + 0.587*g + 0.114*b
    return gray.astype(np.uint8)

grayscale_image = rgb_to_grayscale(rgb_image)

# Save grayscale image
Image.fromarray(grayscale_image).save("grayscale_image.png")

# Step 3: Simulate AI-based conversion back to RGB by stacking grayscale into 3 channels
reconstructed_rgb = np.stack([grayscale_image]*3, axis=-1).astype(np.uint8)

# Save reconstructed RGB image
Image.fromarray(reconstructed_rgb).save("reconstructed_rgb.png")

# Step 4: Calculate Binary Cross Entropy (BCE) Loss between original and reconstructed RGB images
def bce_loss(original, reconstructed):
    epsilon = 1e-7  # to avoid log(0)
    original_norm = original / 255.0
    reconstructed_norm = reconstructed / 255.0
    loss = - (original_norm * np.log(reconstructed_norm + epsilon) + (1 - original_norm) * np.log(1 - reconstructed_norm + epsilon))
    return np.mean(loss)

loss_value = bce_loss(rgb_image, reconstructed_rgb)

print(f"BCE Loss between original and reconstructed RGB: {loss_value:.4f}")

# Step 5: Save images and zip them together
with zipfile.ZipFile("image_conversion_results.zip", 'w') as zipf:
    zipf.write("rgb_image.png")
    zipf.write("grayscale_image.png")
    zipf.write("reconstructed_rgb.png")

print("Images saved and zipped into 'image_conversion_results.zip'")
