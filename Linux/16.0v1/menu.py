import nuke

def create_deepc_menu():
    menus = {
            "Draw": {"icon":"ToolbarDraw.png",
                    "nodes": ["DeepCConstant", "DeepCID", "DeepCPMatte", "DeepCPNoise"]},
            "Channel": {"icon":"ToolbarChannel.png",
                        "nodes": ["DeepCAddChannels", "DeepCRemoveChannels", "DeepCShuffle"]},
            "Color": {"icon":"ToolbarColor.png",
                      "nodes": ["DeepCAdd", "DeepCClamp", "DeepCColorLookup", "DeepCGamma", "DeepCGrade", "DeepCHueShift", "DeepCInvert", "DeepCMatrix", "DeepCMultiply", "DeepCPosterize", "DeepCSaturation"]},
            "3D": {"icon":"ToolbarChannel.png",
                    "nodes": ["DeepCWorld"]},
            "Merge": {"icon":"ToolbarMerge.png",
                      "nodes": ["DeepCKeymix"]},
            "Util": {"icon":"ToolbarToolsets.png",
                    "nodes": ["DeepCAdjustBBox", "DeepCCopyBBox"]},
    }

    toolbar = nuke.menu("Nodes")
    DeepCMenu = toolbar.addMenu("DeepC", icon="DeepC.png")


    for menu, entry in menus.items():
        new = DeepCMenu.addMenu(menu, icon=entry["icon"])

        for node in entry.get("nodes"):
            new.addCommand(node, "nuke.createNode('{}')".format(node), icon="{}.png".format(node))

create_deepc_menu()
