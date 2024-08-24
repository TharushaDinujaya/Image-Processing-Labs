# Point Operations

Image processing point operations involve modifying individual pixels in an image based on their intensity values. These operations are applied to each pixel independently of its neighbors. In this Lab following point operations are considered.

## 1. Brightness Adjustment

Description: Increases or decreases the brightness of an image by adding or subtracting a constant value to each pixel's intensity.

Formula: 𝐼′(𝑥,𝑦) = 𝐼(𝑥,𝑦) + 𝐶I

| Unprocessed Image                                                                                            | Gray Scaled Image                                                                                                       | Brightness Increased Image                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Colored](https://github.com/TharushaDinujaya/Image-Processing-Labs/blob/main/Assignment%2001/SrcImage.jpg) | ![Grayscale](<https://github.com/TharushaDinujaya/Image-Processing-Labs/blob/main/Assignment%2001/OPImage_(1%2C1).png>) | ![Grayscale brightness increased](<https://github.com/TharushaDinujaya/Image-Processing-Labs/blob/main/Assignment%2001/OPImage_(1%2C3).png>) |

## 2. Contrast Adjustment

Description: Modifies the contrast of an image by scaling the pixel values. This can make the image appear more vivid or more muted.

Formula: 𝐼′(𝑥,𝑦) = 𝛼⋅𝐼(𝑥,𝑦) + 𝛽I

| Unprocessed Image                                                                                            | Gray Scaled Image                                                                                                       | Contrast Increased Image                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| ![Colored](https://github.com/TharushaDinujaya/Image-Processing-Labs/blob/main/Assignment%2001/SrcImage.jpg) | ![Grayscale](<https://github.com/TharushaDinujaya/Image-Processing-Labs/blob/main/Assignment%2001/OPImage_(1%2C1).png>) | ![Grayscale contrast increased](<https://github.com/TharushaDinujaya/Image-Processing-Labs/blob/main/Assignment%2001/OPImage_(2%2C1).png>) |

## 3. Negative Image

Description: Inverts the pixel values of an image, converting light areas to dark and vice versa.

Formula: 𝐼′(𝑥,𝑦) = 255 − 𝐼(𝑥,𝑦)

| Unprocessed Image                                                                                            | Gray Scaled Image                                                                                                       | Negative Image                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| ![Colored](https://github.com/TharushaDinujaya/Image-Processing-Labs/blob/main/Assignment%2001/SrcImage.jpg) | ![Grayscale](<https://github.com/TharushaDinujaya/Image-Processing-Labs/blob/main/Assignment%2001/OPImage_(1%2C1).png>) | ![Grayscale Negative](<https://github.com/TharushaDinujaya/Image-Processing-Labs/blob/main/Assignment%2001/OPImage_(1%2C2).png>) |

## 4. Color Manipulation

Description: Adjusts the color properties of an image, such as brightness, contrast, and hue, on a per-channel basis (e.g., RGB channels).

## 5. Reduce to 4Bpp

Reduces the color depth of an image to 4 bits per pixel, limiting it to 16 colors. This involves mapping the image’s original colors to a palette of 16 colors.

| Unprocessed Image                                                                                            | Gray Scaled Image                                                                                                       | Reduced to 4Bpp Image                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Colored](https://github.com/TharushaDinujaya/Image-Processing-Labs/blob/main/Assignment%2001/SrcImage.jpg) | ![Grayscale](<https://github.com/TharushaDinujaya/Image-Processing-Labs/blob/main/Assignment%2001/OPImage_(1%2C1).png>) | ![Grayscale image reduced to 4Bpp](<https://github.com/TharushaDinujaya/Image-Processing-Labs/blob/main/Assignment%2001/OPImage_(2%2C2).png>) |

## 6. Mirror Image

Flips an image horizontally (left-to-right) or vertically (top-to-bottom) to create a mirror reflection.

| Unprocessed Image                                                                                            | Gray Scaled Image                                                                                                       | Mirror Image                                                                                                               |
| ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| ![Colored](https://github.com/TharushaDinujaya/Image-Processing-Labs/blob/main/Assignment%2001/SrcImage.jpg) | ![Grayscale](<https://github.com/TharushaDinujaya/Image-Processing-Labs/blob/main/Assignment%2001/OPImage_(1%2C1).png>) | ![Mirror Image](<https://github.com/TharushaDinujaya/Image-Processing-Labs/blob/main/Assignment%2001/OPImage_(2%2C3).png>) |
