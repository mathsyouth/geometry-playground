import pyvista as pv

# Load the OBJ file
mesh = pv.read("../data/yarn.obj")

# Create a tube filter to give the line some thickness
tube = mesh.tube(radius=0.1)

# Load a local Matcap texture
matcap_texture_path = "../../pmp-data/matcap/toon.jpg"
matcap_texture = pv.read_texture(matcap_texture_path)

# Create a plotter object
plotter = pv.Plotter(window_size=[800, 600])

# Compute normals for each vertex
normals = tube.point_normals

# Normalize normals to the range [0, 1]
normals = (normals + 1) / 2.0

# Extract RGB colors from the Matcap texture
colors = matcap_texture.to_array()
texture_height, texture_width, _ = colors.shape

# Map normals to Matcap texture coordinates
u = (normals[:, 0] * (texture_width - 1)).astype(int)
v = (normals[:, 1] * (texture_height - 1)).astype(int)

# Retrieve colors based on mapped coordinates
mapped_colors = colors[u, v]

# Ensure the shape is correct: n_points by 3
if mapped_colors.shape[1] == 4:
    mapped_colors = mapped_colors[:, :3]  # Only use RGB, discard alpha

# Apply colors to the mesh
tube.point_data['Matcap Colors'] = mapped_colors

# Add the mesh to the plotter with Matcap colors
# plotter.add_mesh(tube, scalars='Matcap Colors', rgb=True)

# Add the tube to the plotter with a color and smooth shading
# plotter.add_mesh(tube, color='#c1c1ff', smooth_shading=True)
# Add the mesh to the plotter with a light purple color and smooth shading
# plotter.add_mesh(tube, color='#b2b3db', smooth_shading=True, specular=1.0, specular_power=100)
plotter.add_mesh(tube, color='#b6b8e2', smooth_shading=True, specular=1.0, specular_power=100)

# Set the camera position for a nice view
plotter.camera_position = [(5, 5, 5), (0, 0, 0), (0, 0, 1)]

# Adjust lighting
light = pv.Light(position=(10, 10, 10), focal_point=(0, 0, 0), color='white', intensity=0.8)
plotter.add_light(light)

# Add shadows for a realistic effect
# plotter.enable_shadows()

# Show the plot
plotter.show()