'''该py code是用训练好的模型来进行预测（生成数据）'''
import torch
import os
if __name__=='__main__':
    '''加载模型'''
    model=None
    model_dir_path=""
    with open(os.path.join(model_dir_path, 'model.pt'), 'rb') as f:
        model = torch.load(f)

    '''定义输入'''
    input_list=['3']
    predict_times_each=10
    # target_len

    '''模型预测'''
    # for

    '''结果展示'''