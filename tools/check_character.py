"""Acceptance test for a delivered character file.

blender -b yakine.blend --python tools/check_character.py -- Yakine
blender -b zahra.blend  --python tools/check_character.py -- Zahra 1.22   (secondary character + its height)
Exit code 0 = OK, 1 = errors found (listed in the console).
"""
import sys

import bpy
from mathutils import Vector

_args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
NAME = _args[0] if _args else "Yakine"
HERO = NAME in ("Yakine", "Nour")
# scale = height of the character relative to Nour (adults: see agents/cast_library.py "height")
SCALE = float(_args[1]) if len(_args) > 1 else {"Yakine": 0.97, "Nour": 1.00}.get(NAME, 1.0)
HEIGHT = 1.75 * SCALE          # top of head incl. hair (buns excluded)

BONES = ["root", "hips", "spine", "chest", "neck", "head", "eye_L", "eye_R", "jaw"]
for s in ("L", "R"):
    BONES += [f"shoulder_{s}", f"upperarm_{s}", f"forearm_{s}", f"hand_{s}",
              f"thigh_{s}", f"shin_{s}", f"foot_{s}", f"toe_{s}", f"thumb_01_{s}", f"index_01_{s}"]
SHAPES = ["smile", "frown", "brow_up", "brow_down", "brow_worried", "eyes_wide", "squint",
          "blink_L", "blink_R", "cheeks_puff", "pout"] + [f"vis_{c}" for c in "ABCDEFGH"]
MESHES = ["body", "face", "eye_L", "eye_R", "hair"]

errors, warnings = [], []
if NAME not in bpy.data.collections:
    errors.append(f"collection '{NAME}' missing")

rig = bpy.data.objects.get(f"{NAME}_rig")
if rig is None or rig.type != "ARMATURE":
    errors.append(f"armature '{NAME}_rig' missing")
else:
    for b in BONES:
        if b not in rig.data.bones:
            errors.append(f"bone '{b}' missing")
    if any(abs(v) > 1e-3 for v in rig.location) or any(abs(v) > 1e-3 for v in rig.rotation_euler):
        errors.append("armature must be at the origin with rotation 0")
    if any(abs(v - 1) > 1e-3 for v in rig.scale):
        errors.append("armature scale must be applied (1, 1, 1)")
    for pb in rig.pose.bones:
        if pb.constraints:
            warnings.append(f"bone '{pb.name}' has constraints (scripts animate rotations directly)")
    if rig.animation_data and rig.animation_data.drivers:
        warnings.append("armature has drivers")

for m in MESHES:
    ob = bpy.data.objects.get(f"{NAME}_{m}")
    if ob is None:
        (errors if m in ("body", "face") else warnings).append(f"mesh '{NAME}_{m}' missing")
    elif rig is not None and ob.find_armature() != rig:
        errors.append(f"mesh '{ob.name}' is not deformed by '{NAME}_rig'")

face = bpy.data.objects.get(f"{NAME}_face")
if face is not None:
    keys = face.data.shape_keys.key_blocks if face.data.shape_keys else {}
    for k in SHAPES:
        if k not in keys:
            errors.append(f"shape key '{k}' missing on {face.name}")

meshes = [o for o in bpy.data.objects if o.type == "MESH" and o.name.startswith(NAME)]
if meshes:
    zs, tris = [], 0
    for o in meshes:
        zs += [(o.matrix_world @ Vector(c)).z for c in o.bound_box]
        tris += sum(len(p.vertices) - 2 for p in o.data.polygons)
    h = max(zs) - min(zs)
    if abs(h - HEIGHT) > 0.15 and HERO:
        errors.append(f"height {h:.2f}, expected ≈ {HEIGHT:.2f} (±0.15)")
    if abs(min(zs)) > 0.03:
        errors.append(f"feet must touch z = 0 (lowest point at {min(zs):.3f})")
    if tris > 90000:
        warnings.append(f"{tris} triangles (budget 30k-60k)")
    if rig is not None and "head" in rig.data.bones:
        hz = (rig.matrix_world @ rig.data.bones["head"].head_local).z
        if abs(hz - 1.02 * SCALE) > 0.06 * SCALE:
            (errors if HERO else warnings).append(
                f"head bone (neck base) at {hz:.2f}, expected {1.02 * SCALE:.2f} ±5% (child proportions)")
    eye = bpy.data.objects.get(f"{NAME}_eye_L")
    if eye is not None:
        eye_y = sum((eye.matrix_world @ Vector(c)).y for c in eye.bound_box) / 8
        if eye_y > 0.0:
            errors.append("character must face -Y (eyes are on the +Y side)")
    print(f"[check] height {h:.3f} - {tris} triangles")

for img in bpy.data.images:
    if img.source == "FILE" and not img.packed_file:
        errors.append(f"image '{img.name}' is not packed")
for mat in bpy.data.materials:
    if mat.use_nodes:
        for n in mat.node_tree.nodes:
            if not n.bl_idname.startswith(("ShaderNode", "NodeFrame", "NodeReroute", "NodeGroup")):
                warnings.append(f"material '{mat.name}' uses node '{n.bl_idname}'")
for o in bpy.data.objects:
    for mod in o.modifiers:
        if mod.type == "PARTICLE_SYSTEM" and mod.particle_system.settings.type == "HAIR":
            errors.append(f"'{o.name}' uses particle hair (use geometry hair)")

for w in warnings:
    print("[check] WARNING:", w)
for e in errors:
    print("[check] ERROR:", e)
print(f"[check] {NAME}: {'OK' if not errors else str(len(errors)) + ' error(s)'}")
sys.exit(1 if errors else 0)
