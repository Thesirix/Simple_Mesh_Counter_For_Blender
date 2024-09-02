import bpy

total_polygons = 0

for obj in bpy.context.scene.objects:
    if obj.type == 'MESH':
        poly_count = len(obj.data.polygons)
        total_polygons += poly_count
        print(f"Object: {obj.name}, Polygons: {poly_count}")

print(f"Total number of polygons in the project: {total_polygons}")
