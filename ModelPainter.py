from Painter import *
from Model import gl_face_mode
import pyassimp as assimp
import numpy as np
import copy
from Texture import Texture2D

class ModelPainter(Painter):

    def __init__(self, model):
        self.model = model
        self.scene_list = None
        self.__compile()

    def clone(self, model):
        model_painter = copy.copy(self)
        model_painter.model = model
        return model_painter

    def __compile(self):
        self.scene_list = glGenLists(1)
        glNewList(self.scene_list, GL_COMPILE)
        self.recursive_render(self.model.scene.rootnode)
        glEndList()

    def apply_material(self, mtl):
            # diffuse = np.array(mtl.properties.get('diffuse', [0.8, 0.8, 0.8, 1.0]))
            # specular = np.array(mtl.properties.get('specular', [0., 0., 0., 1.0]))
            # ambient = np.array(mtl.properties.get('ambient', [0.2, 0.2, 0.2, 1.0]))
            # emissive = np.array(mtl.properties.get('emissive'))
            # shininess = min(mtl.properties.get("shininess", 1.0), 128)
            # wireframe = mtl.properties.get("wireframe", 0)
            # twosided = mtl.properties.get("twosided", 1)
            #
            # glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, diffuse)
            # glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, specular)
            # glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, ambient)
            # glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, emissive)
            # glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, shininess)
            # glPolygonMode(GL_FRONT_AND_BACK, GL_LINE if wireframe else GL_FILL)
            # glDisable(GL_CULL_FACE) if twosided else glEnable(GL_CULL_FACE)
            # tex_name = mtl.properties.get(("file", 1))
            # if tex_name:
            #     name_parts = self.model.model_name.rpartition('/')
            #     tex_name = name_parts[0] + name_parts[1] + tex_name
            #     mtl.texture = Texture2D(tex_name)
        pass


    def recursive_render(self, node):
        print(node)
        glDisable(GL_TEXTURE_2D)
        glPushMatrix()
        glMultMatrixf(node.transformation.transpose())
        scene = self.model.scene
        # draw all meshes assigned to this node
        for mesh in node.meshes:
            ## apply material
            # if len(scene.materials):
                #self.apply_material(mesh.material)
                # if hasattr(mesh.material, "texture"):
                #     mesh.material.texture.bind_texture()
            glEnable(GL_LIGHTING) if len(mesh.normals) else glDisable(GL_LIGHTING)

            for face in mesh.faces:
                face_mode = gl_face_mode(face)
                glBegin(face_mode)
                for ind in face:
                    if len(mesh.colors):
                        glColor4fv(mesh.colors[ind])
                    if len(mesh.normals):
                        glNormal3fv(mesh.normals[ind])
                    # if hasattr(mesh.material, "texture"):
                    #     glTexCoord3fv(mesh.texturecoords[ind])
                    glVertex3fv(mesh.vertices[ind])
                glEnd()
        # draw all children
        for child in node.children:
            self.recursive_render(child)
        glPopMatrix()

    def draw(self):
        glPushMatrix()
        center = self.model.center
        scale = self.model.scale
        glTranslatef(center[0], center[1], center[2])
        glScalef(scale[0], scale[1], scale[2])
        if self.model.rot:
            rot_axes = self.model.rot.axes
            glRotatef(self.model.rot.angle, rot_axes[0], rot_axes[1], rot_axes[2])
        glCallList(self.scene_list)
        glPopMatrix()

