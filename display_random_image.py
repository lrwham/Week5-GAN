def display_random_image(dir):
    import random
    import os
    from PIL import Image
    import matplotlib.pyplot as plt

    files = os.listdir(dir)
    file = random.choice(files)
    img = Image.open(os.path.join(dir, file))
    plt.imshow(img)
    plt.show()