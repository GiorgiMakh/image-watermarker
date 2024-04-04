from PIL import Image, ImageDraw, ImageFont
import os
import configparser

# Configuring settings
config = configparser.ConfigParser()
config.read('settings.ini')

watermark_text = config.get('DEFAULT','watermark')
color = config.get('COLOR', 'color')

inputDir = "./input/"
outputDir = "./output/"
filenames = os.listdir(inputDir)

def add_watermark(input_image_path, watermark_text, watermark_position=(0, 0)):

  # Open the input image
  image = Image.open(inputDir+input_image_path)

  # Create a drawing object
  draw = ImageDraw.Draw(image)

  # Get text size using a default font (e.g., Arial)
  font_size = int(config.get('DEFAULT','font_size'))
  font = ImageFont.truetype(config.get('DEFAULT','font'), font_size)

  # Approximate text width
  text_width = len(watermark_text) * font_size

  # Approximate text height (depends on font size)
  text_height = font_size  # Adjust based on your desired font size

  # Adjust watermark position based on image size and opacity
  if watermark_position == (0, 0):
    # Place watermark in the bottom right corner
    watermark_position = (image.width - text_width - 5, image.height - text_height  - 10)

  # Draw the watermark text using default font and size
  draw.text(watermark_position, watermark_text, fill=color, font=font)

  # Save the watermarked image
  outputPath = outputDir+input_image_path
  image.save(outputPath)
  print('Watermarked image: '+outputPath)

if __name__ == "__main__":
  for image in filenames:
    add_watermark(image, watermark_text)