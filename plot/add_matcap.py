import pyvista as pv

# 1. Create a sample object, such as a sphere or another complex shape
mesh = pv.Sphere()  # You can also use other shapes like pv.Cone() or pv.Cylinder()

# 2. Load a local Matcap texture
matcap_texture_path = "../pmp-data/matcap/resin.jpg"
matcap_texture = pv.read_texture(matcap_texture_path)

# 3. Create a Plotter object
plotter = pv.Plotter()

# 4. Compute normals for each vertex
normals = mesh.point_normals

# 5. Normalize normals to the range [0, 1]
normals = (normals + 1) / 2.0

# 6. Extract RGB colors from the Matcap texture
colors = matcap_texture.to_array()
# colors = colors.reshape((-1, 4))[:, :3]  # Extract RGB colors
texture_height, texture_width, _ = colors.shape

# 7. Map normals to Matcap texture coordinates
u = (normals[:, 0] * (texture_width - 1)).astype(int)
v = (normals[:, 1] * (texture_height - 1)).astype(int)

# 8. Retrieve colors based on mapped coordinates
mapped_colors = colors[u, v]

# Ensure the shape is correct: n_points by 3
if mapped_colors.shape[1] == 4:
    mapped_colors = mapped_colors[:, :3]  # Only use RGB, discard alpha

# 9. Apply colors to the mesh
mesh.point_data['Matcap Colors'] = mapped_colors

# 10. Add the mesh to the plotter with Matcap colors
plotter.add_mesh(mesh, scalars='Matcap Colors', rgb=True)

# 11. Set background color to white
plotter.set_background("white")

# 12. Render and display the scene
plotter.show()
