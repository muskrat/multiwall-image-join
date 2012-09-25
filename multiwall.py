#! /usr/bin/env python2

"""
Multimonitor wallpaper generation script

(c) I K Stead, 25-09-2012
"""
import Image    # Python imaging library
import argparse # Command line options

def open_images(path_list):
    """Open images at paths and return list of Image.image objects"""
    return [Image.open(path) for path in path_list]

def join_images(img_list):
    """Join images horizontally into a new image"""
    sizes = [img.size for img in img_list] # (x, y) tuples
    
    # Functions, just because I felt like doing this in functional style
    add = lambda a, b: a + b 
    elems = lambda i, l: [ x[i] for x in l ] # Get i'th element in each tuple

    # Calculate size of new image by adding up x values and taking the
    # maximum y value.
    newsize = (reduce(add, elems(0, sizes)), 
                    max(elems(1, sizes)))

    # Create the new image and insert images from batch
    new = Image.new('RGB', newsize)
    topleft = 0
    for img in img_list:
        new.paste(img, (topleft, 0))
        topleft += img.size[0]
    return new

def save_image(img, path):
    """Save image object to specified path"""
    img.save(path)
    return

def main():
    # Set up command line interace
    desc = "Join an arbitrary list of images horizontally"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('image_paths', action='store', nargs='+')
    parser.add_argument('-out', action='store')
    args = parser.parse_args()

    batch = open_images(args.image_paths)
    new = join_images(batch)
    save_image(new, args.out)
    return

if __name__ == '__main__':
    main()
