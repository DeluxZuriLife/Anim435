import os 
import maya.standalone
maya.standalone.initialize(name="python")
import maya.cmds as cmds

def main(): 
     asset = os.environ.get("ASSET")
     if not asset: 
        cmds.error("please set an Environment variable ASSET. Use Git Bash and export ASSET=WhatImNamingMyASSET")
        return 
grp = asset 
if not cmds.objExists(grp) 
     grp = cmds.group(em=True, name=asset)
     transforms = []
     for t in cmds.ls(type="transform") or []: 
        shapes = cmds.listRelatives(t, s=True, ni=True) or []
        if any(cmds.nodeType(s) == "mesh" for s in shapes): 
            transforms.append(t)

for t in transforms:
    if t != grp and (cmds.listRelatives(t, p=True) or [None])[0] != grp: 
        try:
            cmds.parent(t, grp)
        except RuntimeError: 
            pass
attr = "assetName"
for t in transforms: 
    plug = f"{t}.{attr}"
if not cmds.objExists(plug):
     cmds.addAttr(t, ln=attr, dt="string")
     cmds.setAttr(plug,asset, type="string")

out_dir = os.getcwd()
out_path = os.path.join(out_dir, f"{asset}.mb")
cmds.file(save=True, type=file_type)
print(f"Saved: {out_path}")

file_type = "mayaBinary" if out_path.lower().endswith(".mb") else "mayaAscii"
cmds.file(save=True, type=file_type) 
print(f"Saved: {out_path}") 

if _name_ == "_main_": 
    try: 
        main()
    finally: 
        maya.standalone.uninitialize() 