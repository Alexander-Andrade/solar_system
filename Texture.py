from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

# import scipy
# import scipy.ndimage
from PIL import Image


# class Texture2D:
#
#     def __init__(self, image_name):
#         self.image = scipy.ndimage.imread(image_name)
#         self.image = scipy.ndimage.rotate(np.fliplr(self.image), 180, reshape=False)
#         self.width, self.height, self.bytes_per_pix = self.image.shape
#         self.image = np.reshape(self.image, (self.width*self.height, self.bytes_per_pix), order='C')
#         self.img_format = self.__get_gl_img_format(image_name)
#         self.texture = glGenTextures(1)
#         glBindTexture(GL_TEXTURE_2D, self.texture)
#         glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
#
#         glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST)
#         glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
#
#         glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
#         glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
#
#         gluBuild2DMipmaps(GL_TEXTURE_2D, self.img_format, self.width, self.height, self.img_format, GL_UNSIGNED_BYTE, self.image)
#
#     def __get_gl_img_format(self, image_name):
#         if image_name.lower().endswith('jpg') and self.bytes_per_pix == 3:
#             return GL_RGB
#         elif image_name.lower().endswith('png') and self.bytes_per_pix == 4:
#             return GL_RGBA
#         else: return GL_RGB
#
#     def bind_texture(self):
#         glBindTexture(GL_TEXTURE_2D, self.texture)
#
#     def get_width(self):
#         return self.width
#
#     def get_height(self):
#         return self.height


class Texture2D:

    def __init__(self, image_name):
        self.type = GL_TEXTURE_2D
        self.image = Image.open(image_name).transpose(Image.FLIP_LEFT_RIGHT).rotate(180)
        self.img_data = np.array(list(self.image.getdata()), np.uint8)

        self.texture = glGenTextures(1)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)

        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

        self.im_format = self.__get_gl_img_format(image_name)
        gluBuild2DMipmaps(GL_TEXTURE_2D, self.im_format, self.width(), self.height(), self.im_format, GL_UNSIGNED_BYTE, self.img_data)

    def __get_gl_img_format(self, image_name):
        bytes_per_pixel = len(self.img_data[0])
        if image_name.lower().endswith('jpg'):
            return GL_RGB
        elif image_name.lower().endswith('png') and bytes_per_pixel == 4:
            return GL_RGBA
        else:
            return GL_RGB


    def bind_texture(self):
        glBindTexture(self.type, self.texture)

    def width(self):
        return self.image.size[0]

    def height(self):
        return self.image.size[1]
