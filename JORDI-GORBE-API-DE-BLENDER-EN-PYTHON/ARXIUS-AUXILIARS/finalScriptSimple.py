import bpy
import io
import time

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

#S'obre el fitxer csv on les dades son enmagatzemades i es fa un readlines on el contingut del text queda guardat a la variable linies

fitxer = io.open('csvmickey.csv', 'r')
linies = fitxer.readlines()
for index in range(len(linies)):
    linies[index] = linies[index].replace('\n', '')
fitxer.close()

# Es crea una funció que generi el dibuix a sobre del qual volem que s'imprimeixin els noms personalitzats dels socis, en aquest cas un clauer amb la silueta de Mickey Mouse.
def dibuix(escrit):
    # Es genera el primer parallelepipede que serà la base del clauer i se l'anomena "pla".
    bpy.ops.mesh.primitive_cube_add(radius=1, location=(0, 0, 0))
    bpy.ops.transform.resize(value=(3, 3, 3), constraint_axis=(True, False, False))
    bpy.ops.transform.resize(value=(3, 3, 3), constraint_axis=(False, True, False))
    cub1 = bpy.context.object

    # Es generan els altres dos parallelepipedes  que formaran les "orelles" de la figura i es colocan als  costats del primer cilindre.
    bpy.ops.mesh.primitive_cube_add(radius=1, location=(3, 3, 0))
    bpy.ops.transform.resize(value=(1.5, 1.5, 1.5), constraint_axis=(True, False, False))
    bpy.ops.transform.resize(value=(1.5, 1.5, 1.5), constraint_axis=(False, True, False))

    bpy.ops.mesh.primitive_cube_add(radius=1, location=(3, -3, 0))
    bpy.ops.transform.resize(value=(1.5, 1.5, 1.5), constraint_axis=(True, False, False))
    bpy.ops.transform.resize(value=(1.5, 1.5, 1.5), constraint_axis=(False, True, False))

    # Es genera un quart parallelepipede que serà el forat per on posar les claus al clauer
    bpy.ops.mesh.primitive_cube_add(radius=1, location=(2, 0, 0))
    bpy.ops.transform.resize(value=(.3, .3, .3), constraint_axis=(True, False, False))
    bpy.ops.transform.resize(value=(.3, .3, .3), constraint_axis=(False, True, False))
    cub4 = bpy.context.object

    # Mitjanzant el següent procès s'elimina la superficie del "pla2" que hi ha dins del "pla"
    # Create a boolean modifier named 'my_bool_mod' for the cube.
    mod_bool = cub1.modifiers.new('my_bool_mod', 'BOOLEAN')
    # Set the mode of the modifier to DIFFERENCE.
    mod_bool.operation = 'DIFFERENCE'
    # Set the object to be used by the modifier.
    mod_bool.object = cub4
    # The modifier_apply function only works on the active object.
    # Set the cube as the active object.
    bpy.context.scene.objects.active = cub1
    # Apply the modifier.
    res = bpy.ops.object.modifier_apply(modifier='my_bool_mod')
    # Delete the cylinder.
    cub4.select = True
    bpy.ops.object.delete()

    # Crear el text, extruir-lo, centrar-ho, moure-ho i rotar-lo.
    bpy.ops.object.text_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(
    True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
    False, False, False, False))
    bpy.context.object.data.extrude = 1
    bpy.context.object.data.align_x = 'CENTER'
    bpy.ops.transform.translate(value=(0, 0, 0.5), constraint_axis=(False, False, True))
    bpy.ops.transform.rotate(value=4.71239, axis=(0, 0, 1), constraint_axis=(True, True, False))

    # Delete default "Text"
    bpy.ops.object.editmode_toggle()
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')

    # Set new word
    chars = escrit
    for char in chars:
        bpy.ops.font.text_insert(text=char)
    bpy.ops.object.editmode_toggle()

    # Transformar el text en mesh
    bpy.ops.object.convert(target='MESH')
    text1 = bpy.context.object

    # Mitjanzant el següent procès s'elimina la superficie del "pla2" que hi ha dins del "pla"
    # Create a boolean modifier named 'my_bool_mod' for the cube.
    mod_bool = cub1.modifiers.new('my_bool_mod', 'BOOLEAN')
    # Set the mode of the modifier to DIFFERENCE.
    mod_bool.operation = 'DIFFERENCE'
    # Set the object to be used by the modifier.
    mod_bool.object = text1
    # The modifier_apply function only works on the active object.
    # Set the cube as the active object.
    bpy.context.scene.objects.active = cub1
    # Apply the modifier.
    res = bpy.ops.object.modifier_apply(modifier='my_bool_mod')
    # Delete the cylinder.
    text1.select = True
    bpy.ops.object.delete()

    #Es crea un document .stl amb cada nom que aparegui al .csv i la figura corresponent
    nom='.//'+escrit+'.stl'
    bpy.ops.export_mesh.stl(filepath=nom)
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

# agafa les dades que del archiu csv que s'han guardat a la variable linies i crea una figura amb cada nom dins de la variable linies.
for name in linies:
    dibuix(name)




