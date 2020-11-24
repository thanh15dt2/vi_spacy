import os
# Preprocessed vlsp data path
path = '/home/thanhlv/workspace/projects/vlsp/home_work/vi_spacy/vlsp_data'
# Split data for training path
train_data_path = '/home/thanhlv/workspace/projects/vlsp/home_work/vi_spacy/reprocessed_data'

en_path = path + '/en.txt'
vi_path = path + '/vi.txt'

with open(vi_path, 'r') as file:
    data_line = file.readlines()
    lines_number = len(data_line)

    with open(train_data_path + '/train.vi', 'w') as train_f:
        with open(train_data_path + '/test.vi', 'w') as test_f:
            with open(train_data_path + '/val.vi', 'w' ) as val_f:

                for i, value in enumerate(data_line):
                    if i < int(lines_number*0.7):
                            train_f.write(value)

                    elif i < int(lines_number*0.85):
                        train_f.close()
                        test_f.write(value)

                    else:
                        test_f.close()
                        val_f.write(value)
                val_f.close()


