import csv

#hepmasss: 1, 0 dota2: 1, -1

def CSV2Libsvm(data,savepath):
    '''
    Transfer .csv data file to libsvm data file
    '''
    csv_reader=csv.reader(open(data))
    
    data_list=[]
    res = []
    for one_line in csv_reader:
        data_list.append(one_line)
    for one_list in data_list:
        one_tmp_line = []
        for i in range(len(one_list)):
            if i == 0:
                one_tmp = str(one_list[i])
            else:
                one_tmp = str(i)+':'+str(one_list[i])
            one_tmp_line.append(one_tmp)
        res.append(' '.join(one_tmp_line))
    with open(savepath, 'w') as f:
        for one_line in res:
            f.write(one_line)
            f.write("\n")

if __name__ == '__main__':
    csv_file_path = ''
    libsvm_save_path = ''
    CSV2Libsvm(csv_file_path, libsvm_save_path)