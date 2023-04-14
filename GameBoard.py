import UnityEngine

# Create the game board
board = [
  ["-", "-", "-"],
  ["-", "-", "-"],
  ["-", "-", "-"]
]

# Set up the board's position and scale
board_position = UnityEngine.Vector3(0, 0, 0)
board_scale = UnityEngine.Vector3(1, 1, 1)

# Create the game board object
game_board = UnityEngine.GameObject.CreatePrimitive(UnityEngine.PrimitiveType.Cube)
game_board.transform.position = board_position
game_board.transform.localScale = board_scale

# Add a material to the game board
board_material = UnityEngine.Material(UnityEngine.Shader.Find("Standard"))
board_material.color = UnityEngine.Color.white
game_board.GetComponent(UnityEngine.MeshRenderer).material = board_material
