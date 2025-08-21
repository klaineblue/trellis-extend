from itertools import count

import trimesh as tm
import pymesh as pm


class trellis_processing():
    def __init__(self,input_address:str=None):
        self.mesh = tm.load(input_address,force='mesh')

    def to_white_model(self,output_address:str="./white_model.glb"):
        self.mesh.visual = tm.visual.ColorVisuals(self.mesh,vertex_colors=[255,255,255,255])
        self.mesh.export(output_address,file_type='glb')
        return self

    def simplify_the_face_by_rate(self,output_address:str="./simplify result.glb"):
        """You can select the expected accuracy for your model with the parameters'rate'.
           Please input your output address."""
        rate = float(input("Please input your expected simplify rate: "))
        if not(0<rate<=1):
            raise ValueError("the rate must be between the interval(0,1]")
        else:
            target_face_count = len(self.mesh.faces)*rate
            simplified_mesh = self.mesh.simplify_quadric_decimation(face_count=target_face_count)
            simplified_mesh.export(output_address)
            return simplified_mesh

    def simplify_the_face_by_count(self,output_address:str="./simplify result(count).glb"):
        """You can select the expected accuracy for your model with the parameters'count'.
           Please input your output address."""
        count = int(input("Please input your expected counts: "))
        if not(0<count<=len(self.mesh.faces)):
            raise ValueError(f"The count must be between the interval(0,{len(self.mesh.faces)}]")
        else:
            simplified_mesh = self.mesh.simplify_quadric_decimation(face_count=count)
            simplified_mesh.export(output_address)
            return simplified_mesh
#   def triangle_to_quadrilateral(self,output_address:str="./quadrilateral mesh model.glb"):
#        fill_mesh = pm.fill_holes(self.mesh)
#        fill_mesh,_ = pm.remove_duplicated_vertices(fill_mesh)
#        fill_mesh,_ = pm.remove_degenerate_triangles(fill_mesh)
#        quad_mesh = pm.quadrangulate(fill_mesh,max_angle=30.0,target_edge_len=0.1,feature_angle=30)
#        pm.save_mesh("output_address.glb,quad_mesh")

if __name__ == '__main__':
    white_model = trellis_processing("../headset.glb")
    white_model.to_white_model()
    simply_model = trellis_processing("../headset.glb")
    simply_model.simplify_the_face_by_rate()
    simply_model = trellis_processing("../headset.glb")
    simply_model.simplify_the_face_by_count()