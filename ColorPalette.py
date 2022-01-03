from PIL import Image
import numpy as np
import pandas as pd


class ColorPalette:

    def __init__(self, filepath):
        self.path = filepath
        self.image = Image.open(self.path)
        self.hex_codes = self.convert_to_array()

    def convert_to_array(self):
        if self.image.mode == "RGBA":
            self.image = self.image.convert("RGB")
        self.image.thumbnail((12, 12))
        numpy_rgb = np.asarray(self.image)
        m, n, r = numpy_rgb.shape
        out_array = np.column_stack((np.repeat(np.arange(m), n), numpy_rgb.reshape(m * n, -1)))
        df = pd.DataFrame(out_array)
        count_values = df.groupby([1, 2, 3]).size().reset_index(name="count").reset_index()
        count_values = count_values.sort_values(by=["count"], axis=0, ascending=False).head(10)
        hex_codes = []
        for row in range(count_values.shape[0]):
            rgb = count_values.iloc[row].to_list()[1:4]
            hex_codes.append(self.rgb_to_hexcode(int(rgb[0]), int(rgb[1]), int(rgb[2])))
        return hex_codes

    def rgb_to_hexcode(self, r, g, b):
        return ('#{:X}{:X}{:X}').format(r,g,b)
