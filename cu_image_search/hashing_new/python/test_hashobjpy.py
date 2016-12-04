from _hasher_obj_py import *
import sys

if __name__ == "__main__":
    hasher = new_HasherObjectPy()
    # setters are not working?
    up_path = HasherObjectPy_get_base_updatepath(hasher)
    print(up_path)
    HasherObjectPy_set_base_updatepath(hasher, "/home/ubuntu/memex/update/indexing/")
    up_path = HasherObjectPy_get_base_updatepath(hasher)
    print(up_path)
    HasherObjectPy_set_base_modelpath(hasher, "/home/ubuntu/memex/data/")
    status = HasherObjectPy_initialize(hasher)
    if status != 0:
        print("Hasher was not able to initialize")
        sys.exit(-1)
    featurefilename = "/home/ubuntu/memex/DeepSentiBank_memex/cu_image_search/www/1480830128.81.dat"
    HasherObjectPy_set_query_feats_from_disk(hasher, featurefilename)
    HasherObjectPy_set_outputfile(hasher, featurefilename[:-4])
    HasherObjectPy_find_knn(hasher)
    delete_HasherObjectPy(hasher)
