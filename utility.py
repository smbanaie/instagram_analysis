import codecs

def MakeUniqueValues(ifname,ofname="") :

    input_file = codecs.open(ifname, 'rU', 'utf-8')
    data = {}
    cnt = 1
    for line in input_file :
        print ("Processing # " + str(cnt))
        cnt += 1
        if line not in data.keys():
            data[line] = 1

    input_file.close()
    if ofname != "" :
       output_file = codecs.open(ofname, 'w', 'utf-8')
    else :
       output_file = codecs.open(ifname, 'w', 'utf-8')


    for key in data.keys() :
        output_file.write(key)

    output_file.close()


if __name__ == "__main__" :
    MakeUniqueValues('tags_all.txt','tags.txt')
