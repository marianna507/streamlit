import shapefile
input = shapefile.Reader("All_Merged.shp")
shapes = input.shapes() # -> the geometries in a list
fields = input.fields[1:] # -> the fields definition in a list
fields_name = [field[0] for field in fields] # -> the fields names in a list
attributes = input.records() # -> the attributes in a list

