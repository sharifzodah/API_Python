import json

with open('D:\\QA COURSE\\API_Testing_Python\\Simple_Json2.txt') as file1:
    data1 = json.load(file1)
    print(type(data1))
    print(data1)
    with open('body.json', 'w') as f:
        json.dump(data1, f)

    for class_name in data1:
        content = data1[class_name]
        ans = content['answer']
        options = list(content['options'])
        assert options.__contains__(ans)


with open('D:\\QA COURSE\\API_Testing_Python\\Simple_Json.txt') as file2:
    data2 = json.load(file2)
    print(type(data2))
    class_data = data2['quiz']
    class_list = list(class_data)

    for i in range(0, len(class_data)):
        class_data_content = class_data[class_list[i]]
        class_data_content_list = list(class_data_content)
        for question_data in class_data_content:
            question_content = class_data_content[question_data]
            question1 = str(question_content['question'])
            options1 = list(question_content['options'])
            answer1 = str(question_content['answer'])
            assert options1.__contains__(answer1)

# Comparing json schemas of two json files
with open('D:\\QA COURSE\\API_Testing_Python\\Simple_Json_1.txt') as file3:
    data3 = json.load(file3)
    assert data2 == data3
