class YLoader:
    file_name = ''

    def __init__(self, file_name):
        self.file_name = file_name

    def __ClearNames(self, data):
        for index in range(len(data['names'])):
            data['names'][index] = data['names'][index].replace('>', '')
        return data

    def __RemoveLineTransition(self, data):
        for index in range(len(data['names'])):
            data['names'][index] = data['names'][index].replace('\n', '')
        for index in range(len(data['data'])):
            data['data'][index] = data['data'][index].replace('\n', '')
        return data
        
    def Load(self):
        unprepared_format = {
            'names': [],
            'data': [],
            'lengths': [],
            }
        with open(self.file_name) as file:
            lines = file.readlines()
        index = 0
        breaking_flag = False
        while not breaking_flag:
            unprepared_format['names'].append(lines[index])
            index += 1
            if index >= len(lines):
                break
            num_lines = 0
            while lines[index][0] != '>':
                unprepared_format['data'].append(lines[index])
                index += 1
                num_lines += 1
                if index >= len(lines):
                    breaking_flag = True
                    break
            unprepared_format['lengths'].append(num_lines)

        self.__RemoveLineTransition(unprepared_format)
        self.__ClearNames(unprepared_format)

        sub_index = 0
        prepared_format = {
            'names' : [],
            'data' : []
           }
        for index in range(len(unprepared_format['names'])):
            summary_string = ''
            for nuc in range(sub_index, sub_index + unprepared_format['lengths'][index]):
                summary_string += unprepared_format['data'][nuc]
            sub_index += unprepared_format['lengths'][index]
            prepared_format['names'].append(unprepared_format['names'][index])
            prepared_format['data'].append(summary_string)
        return prepared_format