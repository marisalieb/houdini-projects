# creating window
import hou
import os
import PySide2 as ps  # ps is just an abbreviation


def assign_textures(path, material):
    files = os.listdir(path)  # this will go to where we specified the path below and list every object/file in there
    for image in files:
        if 'diff_1k.jpg' in image:
            material.parm('basecolor_useTexture').set(True)
            material.parm('basecolor_texture').set(path + '/' + image)
        if '_ao_1k.jpg' in image:
            material.parm('occlusion_useTexture').set(True)
            material.parm('occlusion_texture').set(path + '/' + image)
        if 'rough_1k.exr' in image:
            material.parm('rough_useTexture').set(True)
            material.parm('rough_texture').set(path + '/' + image)
        # add more for metal, glossiness, reflection, etc.
        if 'nor_gl_1k.exr' in image:
            material.parm('baseBumpAndNormal_enable').set(True)
            material.parm('baseNormal_texture').set(path + '/' + image)
            material.parm('baseNormal_scale').set(-.01)
        if 'disp_1k.png' in image:
            material.parm('dispTex_enable').set(True)
            material.parm('dispTex_texture').set(path + '/' + image)
            material.parm('dispTex_scale').set(.05)


def getHoudiniMainWindow():
    # get the houdini main window
    return hou.qt.mainWindow()


class CreateWindow(ps.QtWidgets.QDialog):
    def __init__(self, parent=getHoudiniMainWindow()):

    # initialise the create window
    super(CreateWindow, self).__init__(parent)

    # window settings
    self.setWindowTitle('Assign Textures Window')
    self.setMinimumSize(300, 80)
    self.setWindow(self.windowFlags() ^ ps.QtCore.Qt.WindowContextHelpButtonHint)

    # Window element creation
    self.createWidgets()
    self.createLayouts()
    self.createConnections()

    # first  method that's custom to the class here
    def createWidgets(self):

    # create pyside window widgets

    # widgets to get folder path
    self.texturePathLineEdit = ps.QtWidgets.QLineEdit()
    self.texturePathButton = hou.qt.FileChooserButton()
    self.textureButton = ps.QtWidgets.QPushButton('Assign Textures')
