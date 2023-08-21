A simple script that takes Blender's scene objects' location and rotation and saves it as func_static entity into idTech4 .map file (might also work for idTech 3). In order for this to work in a level editor and game (e.g. DarkRadiant and Doom 3), ASE/LWO model needs to be exported beforehand, with all aplicable textures and materials.

Object in Blender needs a custom property set, called "model" (string type) with value as a path to your ASE/LWO model:
![image](https://github.com/motorsep/blender-entity/assets/1927918/e807f84a-c0dd-4204-9897-7500c1418597)
