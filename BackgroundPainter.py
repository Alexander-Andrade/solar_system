from Painter import *
from Texture import Texture2D


class BackgroundPainter(Painter):

    def __init__(self, img_name):
        self.texture = Texture2D(img_name)

    def draw(self):
        glEnable(GL_TEXTURE_2D)
        self.texture.bind_texture()
        glBegin(GL_QUADS)
        # new face
        glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0, 1.0);
        glTexCoord2f(1.0, 0.0); glVertex3f(1.0, -1.0, 1.0);
        glTexCoord2f(1.0, 1.0); glVertex3f(1.0, 1.0, 1.0);
        glTexCoord2f(0.0, 1.0); glVertex3f(-1.0, 1.0, 1.0);
        # new face
        glTexCoord2f(0.0, 0.0);	glVertex3f(1.0, 1.0, 1.0);
        glTexCoord2f(1.0, 0.0);	glVertex3f(1.0, 1.0, -1.0);
        glTexCoord2f(1.0, 1.0);	glVertex3f(1.0, -1.0, -1.0);
        glTexCoord2f(0.0, 1.0);	glVertex3f(1.0, -1.0, 1.0);
        # new face
        glTexCoord2f(0.0, 0.0);	glVertex3f(1.0, 1.0, -1.0);
        glTexCoord2f(1.0, 0.0);	glVertex3f(-1.0, 1.0, -1.0);
        glTexCoord2f(1.0, 1.0);	glVertex3f(-1.0, -1.0, -1.0);
        glTexCoord2f(0.0, 1.0);	glVertex3f(1.0, -1.0, -1.0);
        # new face
        glTexCoord2f(0.0, 0.0);	glVertex3f(-1.0, -1.0, -1.0);
        glTexCoord2f(1.0, 0.0);	glVertex3f(-1.0, -1.0, 1.0);
        glTexCoord2f(1.0, 1.0);	glVertex3f(-1.0, 1.0, 1.0);
        glTexCoord2f(0.0, 1.0);	glVertex3f(-1.0, 1.0, -1.0);
        # new face
        glTexCoord2f(0.0, 0.0);	glVertex3f(-1.0, 1.0, -1.0);
        glTexCoord2f(1.0, 0.0);	glVertex3f(1.0, 1.0, -1.0);
        glTexCoord2f(1.0, 1.0);	glVertex3f(1.0, 1.0, 1.0);
        glTexCoord2f(0.0, 1.0);	glVertex3f(-1.0, 1.0, 1.0);
        # new face
        glTexCoord2f(0.0, 0.0);	glVertex3f(-1.0, -1.0, -1.0);
        glTexCoord2f(1.0, 0.0);	glVertex3f(1.0, -1.0, -1.0);
        glTexCoord2f(1.0, 1.0);	glVertex3f(1.0, -1.0, 1.0);
        glTexCoord2f(0.0, 1.0);	glVertex3f(-1.0, -1.0, 1.0);
        glEnd()
        glDisable(GL_TEXTURE_2D)

