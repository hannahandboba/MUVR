# Create the X and O game pieces
x_piece = UnityEngine.GameObject.CreatePrimitive(UnityEngine.PrimitiveType.Cube)
x_piece.transform.localScale = UnityEngine.Vector3(0.9, 0.9, 0.9)
x_piece_material = UnityEngine.Material(UnityEngine.Shader.Find("Standard"))
x_piece_material.color = UnityEngine.Color.red
x_piece.GetComponent(UnityEngine.MeshRenderer).material = x_piece_material

o_piece = UnityEngine.GameObject.CreatePrimitive(UnityEngine.PrimitiveType.Sphere)
o_piece.transform.localScale = UnityEngine.Vector3(0.9, 0.9, 0.9)
o_piece_material = UnityEngine.Material(UnityEngine.Shader.Find("Standard"))
o_piece_material.color = UnityEngine.Color.blue
o_piece.GetComponent(UnityEngine.MeshRenderer).material = o_piece_material
