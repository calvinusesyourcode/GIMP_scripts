from gimpfu import *
import re

def create_image_and_text_layer():
    # Read text from file
    with open("C:/Users/calvi/AppData/Roaming/GIMP/2.10/plug-ins/text.txt", "r") as file:
        text = file.read()

    # Split text into array
    text_array = text.split("\n#\n")

    for array_index, text in enumerate(text_array):
        # Create a new image of size 480x360
        image = gimp.Image(480, 360, RGB)

        # Create a new text layer
        text_layer = pdb.gimp_text_layer_new(image, text, "Minecraftia", 21, PIXELS)

        # Add text layer to image
        image.add_layer(text_layer, 0)

        # Set text color to white
        black = gimpcolor.RGB(0.0, 0.0, 0.0, 1.0)
        white = gimpcolor.RGB(1.0, 1.0, 1.0, 1.0)
        pdb.gimp_text_layer_set_color(text_layer, black)

        # Set font justify to center
        pdb.gimp_text_layer_set_justification(text_layer, TEXT_JUSTIFY_CENTER)

        # Duplicate the text layer
        text_layer_white = pdb.gimp_layer_copy(text_layer, TRUE)


        # Add shadow layer to image
        image.add_layer(text_layer_white, 0)

        # Apply Gaussian blur to the copied layer
        radius = 5
        pdb.plug_in_gauss_rle(image, text_layer, radius, 1, 1)

        # Set duplicate layer font color to black
        pdb.gimp_text_layer_set_color(text_layer_white, white)

        # Align text layers to the center of image
        pdb.gimp_layer_set_offsets(text_layer, (480 - pdb.gimp_drawable_width(text_layer)) // 2, 
        (360 - pdb.gimp_drawable_height(text_layer)) // 2)
        pdb.gimp_layer_set_offsets(text_layer_white, (480 - pdb.gimp_drawable_width(text_layer_white)) // 2, 
        (360 - pdb.gimp_drawable_height(text_layer_white)) // 2)

        # Move the shadow layer 5 pixels to the right and 5 pixels down
        pdb.gimp_layer_translate(text_layer_white, -2, -2)
        
        # # Convert the text layer to a regular layer
        # text_layer_copy = pdb.gimp_layer_new_from_drawable(text_layer, image)

        # # Add the new layer to the image
        # image.add_layer(text_layer_copy, 0)


        # Merge down
        merged_layer = image.merge_visible_layers(CLIP_TO_IMAGE)

        # Remove non-alphanumeric characters from text for filename
        clean_text = re.sub(r'\W+', '_', text)

        # Export the image
        filename = "C:/Users/calvi/Desktop/{}.png".format(clean_text)
        pdb.file_png_save(image, merged_layer, filename, filename, 0, 9, 1, 1, 1, 1, 1)


register(
    "python_fu_create_image_and_text_layer",
    "Create image and text layer",
    "Create a 480x360 transparent image, create a text layer, set text to item of array, set font to Minecraftia, set font size to 21, set font color to white, duplicate layer, set duplicate layer font color to black, move that layer behind, move it 5 pixels to the right and 5 pixels down",
    "OpenAI",
    "OpenAI",
    "2023",
    "<Toolbox>/Xtns/Languages/Python-Fu/Test/_Create image and text layer...",
    "",
    [],
    [],
    create_image_and_text_layer
)

main()
