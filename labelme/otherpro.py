import os


def preproloadFile(filename,label_file):
        if(os.path.isfile(label_file)):
            ##如果果labelme的json文件存在则可以直接返回，用原来的json文件。  也可以和模型产生的json文件进行融合，产生新的json写入磁盘.  这里是什么也不做用原来的。
            return False
        ##当labelme的json文件不存在时，这里应该访问模型，生成标准的labelme的json文件，写入磁盘。 这里是以固定的json为例 
        labeljson ='''{
                        "version": "5.0.1",
                        "flags": {},
                        "shapes": [
                            {
                            "label": "person",
                            "points": [
                                [
                                249.3305785123967,
                                218.00826446280993
                                ],
                                [
                                532.801652892562,
                                266.7685950413223
                                ],
                                [
                                431.1487603305785,
                                132.88429752066116
                                ]
                            ],
                            "group_id": null,
                            "shape_type": "polygon",
                            "flags": {}
                            }
                        ],
                        "imagePath": "linhuchong.jpeg",
                        "imageData": null,
                        "imageHeight": 801,
                        "imageWidth": 1280
                    }'''
        with open(label_file,'w') as f:
            f.write(labeljson)
        # print(f"write labelfile={label_file}")
        return True