#automatically apply textures to a material based off of a folder

import hou
import os #acces to operating system

# you need an argument for a path and a material since i defined a path
def apply_textures(path, material):
    files = os.listdir(path) #this will go to where we specified the path below and list every object/file in there
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
        #add more for metal, glossiness, reflection, etc.
        if 'nor_gl_1k.exr' in image:
            material.parm('baseBumpAndNormal_enable').set(True)
            material.parm('baseNormal_texture').set(path + '/' + image)
            material.parm('baseNormal_scale').set(-.01)
        if 'disp_1k.png' in image:
            material.parm('dispTex_enable').set(True)
            material.parm('dispTex_texture').set(path + '/' + image)
            material.parm('dispTex_scale').set(.05)



material = hou.selectedNodes()[0] #you need a list, so even if just one object is selected you get a list and select the first item in the list with [0]
path = 'D:/Git/tutorial_materials/textures' # insert in () the pathway to a material file on your pc, IMPORTANT here: make sure the slashes / are this way round
apply_textures(path, material) # need this line to call the function, everything previous is just the blueprint but you still need to call the function

#end stage 2
