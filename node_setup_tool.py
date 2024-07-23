# simple example of how to create a shelf tool for basic garment geo setup
# I reuse this setup a lot for each garment I import so this shelf tool make this initial setup easier
# (for similar tools just paste this code into a new shelf tool and modify node name as required for individual setup)

# get obj context and create geo
obj = hou.node('/obj')
geo_node = obj.createNode('geo', 'geo_garment')

# create nodes for a basic setup
file_node = geo_node.createNode('file')
uvlayout_node = geo_node.createNode('uvlayout::3.0', 'uv')
uvtransform_node = geo_node.createNode('uvtransform::2.0')
transform_node = geo_node.createNode('xform')
rest_node = geo_node.createNode('rest')
remesh_node = geo_node.createNode('remesh::2.0')
transform2_node = geo_node.createNode('xform')
group_node = geo_node.createNode('groupcreate')

objectmerge_node = geo_node.createNode('object_merge')
walknull_node = geo_node.createNode('null', 'walk')

# connect input and layout
uvlayout_node.setInput(0, file_node, 0)
uvtransform_node.setInput(0, uvlayout_node, 0)
transform_node.setInput(0, uvtransform_node, 0)
rest_node.setInput(0, transform_node, 0)
remesh_node.setInput(0, rest_node, 0)
transform2_node.setInput(0, remesh_node, 0)
group_node.setInput(0, transform2_node, 0)

walknull_node.setInput(0, objectmerge_node, 0)

geo_node.layoutChildren()

#set flags and parameters
group_node.setDisplayFlag(True)
file_node.setRenderFlag(False)

remesh_node.parm('targetsize').set(0.0067)
