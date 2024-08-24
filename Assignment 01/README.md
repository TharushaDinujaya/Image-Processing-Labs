# Point Operations

Image processing point operations involve modifying individual pixels in an image based on their intensity values. These operations are applied to each pixel independently of its neighbors. In this Lab following point operations are considered.

## 1. Brightness Adjustment

Description: Increases or decreases the brightness of an image by adding or subtracting a constant value to each pixel's intensity.
Formula: 𝐼′(𝑥,𝑦) = 𝐼(𝑥,𝑦) + 𝐶I

## 2. Contrast Adjustment

Description: Modifies the contrast of an image by scaling the pixel values. This can make the image appear more vivid or more muted.
Formula: 𝐼′(𝑥,𝑦) = 𝛼⋅𝐼(𝑥,𝑦) + 𝛽I

## 3. Negative Image

Description: Inverts the pixel values of an image, converting light areas to dark and vice versa.
Formula: 𝐼′(𝑥,𝑦) = 255 − 𝐼(𝑥,𝑦)

## 4. Color Manipulation

Description: Adjusts the color properties of an image, such as brightness, contrast, and hue, on a per-channel basis (e.g., RGB channels).

## 5. Reduce to 4Bpp

Reduces the color depth of an image to 4 bits per pixel, limiting it to 16 colors. This involves mapping the image’s original colors to a palette of 16 colors.

## 6. Mirror Image

Flips an image horizontally (left-to-right) or vertically (top-to-bottom) to create a mirror reflection.
