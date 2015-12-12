import codecs

def MakeUniqueValues(fname) :

    input_file = codecs.open(fname, 'rU', 'utf-8')
    data = {}
    for line in input_file :
        if line not in data.keys():
            data[line] = 1

    input_file.close()
    output_file = codecs.open(fname, 'wU', 'utf-8')

    for key in data.keys() :
        output_file.write(key)

    output_file.close()


if __name__ == "__main__" :
    MakeUniqueValues("medias_out")