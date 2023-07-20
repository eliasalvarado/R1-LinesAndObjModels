from gl import Renderer
import shaders

width = 2048
height = 2048

rend = Renderer(width, height)
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader

rend.glLoadModel("skull.obj", translate=(width/2, height/20, 0), rotate=(-1.5, 0, 0.5), scale=(70, 70, 70))

rend.glRender()

rend.glFinish("skull.bmp")

