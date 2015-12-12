import codecs

def MakeUniqueValues(fname) :

    input_file = codecs.open(fname, 'rU', 'utf-8')
    data = {}
    cnt = 1
    for line in input_file :
        print ("Processing # " + str(cnt))
        cnt += 1
        if line not in data.keys():
            data[line] = 1

    input_file.close()
    output_file = codecs.open(fname, 'wU', 'utf-8')

    for key in data.keys() :
        output_file.write(key)

    output_file.close()


if __name__ == "__main__" :
    MakeUniqueValues("D:\MyProjects\Instagram\user_ids.txt")