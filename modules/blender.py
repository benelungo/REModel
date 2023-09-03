import os
import bpy
import mathutils
import math
import matplotlib.colors as plot_colors
from PySide6.QtWidgets import QMessageBox


def load_blend_file(path: str):
    """
    Load blend file by path

    WARNING: Before using any method you must call "load_blend_file"
    """
    try:
        bpy.ops.wm.open_mainfile(filepath=path)
    except Exception:
        QMessageBox.critical(None, "Error", "Wrong blend file")
        raise Exception("Wrong file")


def get_collections():
    """
    Read all collections on scene and return it

    :return: all collections of blend scene
    :rtype: bpy.data.bpy_prop_collection
    """
    return bpy.data.collections


def disable_interpolation():
    """Disable shadows of all objects"""
    if bpy.context.scene.render.engine == 'CYCLES':
        bpy.context.scene.cycles.taa_render_samples = 1
    else:
        bpy.context.scene.eevee.taa_render_samples = 1


def disable_antialiasing():  # TODO this is not working, find good method
    if bpy.context.scene.render.engine == 'CYCLES':
        bpy.context.scene.cycles.use_motion_blur = False
        bpy.context.scene.cycles.sss_samples = 1
        bpy.context.scene.cycles.use_bloom = False
        try:
            bpy.context.scene.cycles.samples = 1
        except Exception as e:
            print(e)
    else:
        bpy.context.scene.eevee.use_motion_blur = False
        bpy.context.scene.eevee.sss_samples = 1
        bpy.context.scene.eevee.use_bloom = False
        try:
            bpy.context.scene.eevee.samples = 1
        except Exception as e:
            print(e)


def disable_specular():
    """Disable specular of all objects"""
    for collection in get_collections():
        for obj in collection.objects:
            if type(obj) == bpy.types.Object and obj.active_material is not None:
                obj.active_material.specular_intensity = 0

    for obj in bpy.context.scene.objects:
        if obj.type == 'MESH':
            for slot in obj.material_slots:
                if slot.material is not None:
                    material = slot.material
                    material.specular_intensity = 0.0  # TODO і тут


def disable_shadows():
    """Disable shadows of all objects"""
    if bpy.context.scene.render.engine == 'CYCLES':
        bpy.context.scene.cycles.use_shadows = False
    else:
        bpy.context.scene.eevee.use_shadows = False

    for obj in bpy.context.scene.objects:
        for slot in obj.material_slots:
            if slot.material is not None:
                slot.material.shadow_method = 'NONE'


def disable_light():
    """Disable all light sources"""
    for obj in bpy.context.scene.objects:
        if obj.type == 'LIGHT':
            obj.data.color = (1.0, 1.0, 1.0)  # TODO і тут

    for obj in bpy.context.scene.objects:
        if obj.type == "LIGHT":
            obj.hide_render = True


def enable_emission():
    """Enable objects emission and apply old color"""
    for material in bpy.data.materials:
        material.use_nodes = True
        # Remove any existing nodes
        for node in material.node_tree.nodes:
            material.node_tree.nodes.remove(node)

        # Add an emission node and link it to the output
        emission_node = material.node_tree.nodes.new(type='ShaderNodeEmission')
        output_node = material.node_tree.nodes.new(type='ShaderNodeOutputMaterial')
        material.node_tree.links.new(emission_node.outputs[0], output_node.inputs[0])

        # Set the emission color and strength
        emission_node.inputs[0].default_value = material.diffuse_color
        emission_node.inputs[1].default_value = 1.0


def rotate_UD(degrees):
    """Rotate camera around world center Up/Down"""
    camera = bpy.context.scene.camera
    radians = math.radians(degrees)
    x = camera.location.x * math.cos(radians) - camera.location.z * math.sin(radians)
    y = camera.location.y
    z = camera.location.x * math.sin(radians) + camera.location.z * math.cos(radians)
    new_location = mathutils.Vector((x, y, z))
    camera.location = new_location
    camera.rotation_euler.x -= radians


def rotate_LR(degrees):
    """Rotate camera around world center Left/Right"""
    camera = bpy.context.scene.camera
    radians = math.radians(degrees)
    x = camera.location.x * math.cos(radians) - camera.location.y * math.sin(radians)
    y = camera.location.x * math.sin(radians) + camera.location.y * math.cos(radians)
    z = camera.location.z
    new_location = mathutils.Vector((x, y, z))
    camera.location = new_location
    camera.rotation_euler.z += radians


def change_resolution(width, height):
    """Change render resolution"""
    bpy.context.scene.render.resolution_x = width
    bpy.context.scene.render.resolution_y = height


def change_background(colors):
    """Change world background"""
    bpy.context.scene.world.use_nodes = True
    tree = bpy.context.scene.world.node_tree
    for node in tree.nodes:
        if node.type in ("TEX_ENVIRONMENT", "BACKGROUND", "ShaderNodeBackground", "Background", "ShaderNodeTexEnvironment"):
            tree.nodes.remove(node)

    # Створюємо новий вузол Background
    background_node = tree.nodes.new("ShaderNodeBackground")
    background_node.location = (0, 0)
    background_node.inputs[0].default_value = plot_colors.to_rgba(colors["Scene Background"])

    # Підключаємо вихідний вузол Background до вихідного вузла World Output
    world_output = tree.nodes.get("World Output")
    if world_output is not None:
        tree.links.new(background_node.outputs[0], world_output.inputs[0])

    bpy.context.scene.view_settings.view_transform = 'Standard'


def normalize_colors():
    # Get the reference to the scene
    scene = bpy.context.scene

    # Disable color management
    try:
        scene.view_settings.view_transform = 'Raw'
        scene.view_settings.look = 'None'
    except:
        print("Redo")

    if bpy.context.scene.render.engine == 'CYCLES':  # TODO тут зміна кольору
        bpy.context.scene.cycles.gi_diffuse_bounces = 0
    else:
        bpy.context.scene.eevee.gi_diffuse_bounces = 0


def set_hdr_background(path):
    bpy.context.scene.world.use_nodes = True
    tree = bpy.context.scene.world.node_tree

    # Delete previous nodes
    for node in tree.nodes:
        tree.nodes.remove(node)

    # Add nodes for the HDR background
    bg_image = tree.nodes.new(type='ShaderNodeBackground')
    tex_image = tree.nodes.new(type='ShaderNodeTexEnvironment')
    tex_image.image = bpy.data.images.load(path)
    tex_coord = tree.nodes.new(type='ShaderNodeTexCoord')
    mapping = tree.nodes.new(type='ShaderNodeMapping')
    mapping.vector_type = 'TEXTURE'
    # mapping.inputs[2].default_value = (3.14159, 0, 0)  # Turn 180 degrees
    tex_coord.location = (-400, 400)
    mapping.location = (-200, 400)

    # Connecting nodes
    tree.links.new(tex_coord.outputs[0], mapping.inputs[0])
    tree.links.new(mapping.outputs[0], tex_image.inputs[0])
    tree.links.new(tex_image.outputs[0], bg_image.inputs[0])

    # Add the output node "World Output"
    world_output = tree.nodes.get("World Output")
    if world_output is None:
        world_output = tree.nodes.new(type='ShaderNodeOutputWorld')
    tree.links.new(bg_image.outputs[0], world_output.inputs[0])


def transformX(value):
    bpy.context.scene.camera.location.x += value


def transformY(value):
    bpy.context.scene.camera.location.y += value


def transformZ(value):
    bpy.context.scene.camera.location.z += value


def apply_custom_materials(colors: dict) -> None:
    """Change collections colors"""
    change_materials(colors)
    change_background(colors)
    enable_emission()
    disable_light()
    disable_shadows()
    disable_specular()
    disable_antialiasing()
    disable_interpolation()
    normalize_colors()


def change_materials(colors):
    """Changing all materials in collections on custom with appropriated colors"""
    for collection in bpy.data.collections:
        material = bpy.data.materials.new(name=collection.name)
        try:
            material.diffuse_color = plot_colors.to_rgba(colors[collection.name])
        except Exception as e:
            QMessageBox.critical(None, "Error", str(e))
            raise Exception(e)
        for obj in collection.objects:
            if isinstance(obj, bpy.types.Object) \
                    and obj.type != 'LIGHT' \
                    and obj.type != 'CAMERA' \
                    and obj.type != 'ARMATURE':
                for slot in obj.material_slots:
                    slot.material = material
                obj.data.materials.append(material)


def apply_options(required_options, options_dict, options_value):
    """Apply all selected options to the scene objects"""
    for option in required_options:
        if option["type"] == 'regular':
            options_dict[option['name']]["func"]()
        else:
            if options_value[option["name"]] is not None:
                options_dict[option['name']]["func"](options_value[option["name"]])


def render(_output_dir: str, _output_filename: str) -> None:
    """Render one image to output directory"""
    bpy.context.scene.render.image_settings.compression = 0
    bpy.context.scene.render.image_settings.quality = 100
    bpy.context.scene.render.image_settings.file_format = 'PNG'
    bpy.context.scene.render.image_settings.color_mode = 'RGB'
    bpy.context.scene.render.image_settings.color_depth = '16'

    if bpy.context.scene.render.engine == 'CYCLES':
        bpy.context.scene.cycles.device = 'GPU'
        bpy.context.preferences.addons['cycles'].preferences.compute_device_type = 'CUDA'

    bpy.context.scene.render.filepath = os.path.join(_output_dir, _output_filename)

    bpy.ops.render.render(write_still=True)


def generate_image(classes_text_list: dict,
                   options_text_list: list,
                   save_full_path: str,
                   blend_file_path: str,
                   options_dict: dict,
                   options_value: dict,
                   path_to_values,
                   path_to_targets,
                   filename) -> None:

    # return any changes
    load_blend_file(blend_file_path)

    # change scene by options
    apply_options(options_text_list, options_dict, options_value)

    # render value image
    filepath = os.path.join(path_to_values, filename)
    render(save_full_path, filepath)

    # prepare scene to render like target
    apply_custom_materials(classes_text_list)

    # render target image
    filepath = os.path.join(path_to_targets, filename)
    render(save_full_path, filepath)
