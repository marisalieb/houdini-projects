# this is the code from my export fractures hda

def exportAllParts(parent):
    # get all child nodes in hda
    frac_node = parent.node('fracture')
    unique_node = frac_node.node('find_unique_values')
    export_node = parent.node('export')
    rop_node = parent.node('ropnet1').node('filmboxfbx')

    # clear subnet before next export
    children = export_node.children()
    for child in children:
        child.destroy()

    # get detail attribute
    geo = unique_node.geometry()
    attribute = geo.findGlobalAttrib('names')
    names = geo.stringListAttribValue(attribute)

    # set up new nodes with correct geo
    for name in names:
        new_geo = export_node.createNode('geo', name)
        merge_node = new_geo.createNode('object_merge')
        blast_node = new_geo.createNode('blast')

        # hook up nodes in new geo and move display flag, turn off render
        blast_node.setInput(0, merge_node, 0)
        blast_node.setDisplayFlag(True)
        merge_node.setRenderFlag(False)

        merge_node.parm('objpath1').set('../../../fracture/')

        blast_node.parm('group').set('@name=' + name)
        blast_node.parm('negate').set(True)

    rop_node.parm('execute').pressButton()