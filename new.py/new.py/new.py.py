k = int(input("Enter the task number - "))

if k == 1:
    def task1():
        import psutil
        d = psutil.disk_partitions('Disks information') # ���������� � �����
        print(d)
    task1()

if k == 2:
    def task2():
        import os

        f = open('example.txt','w') # �������� �����
        f.write(str(input()))
        f.close()
        z = open('example.txt','r') 
        print(z.read()) # ������ �����
        z.close()
        os.remove('example.txt') # �������� �����
    task2()

if k == 3:
    def task3():
        import json
        import os

        data = str(input())
        hey = {'smth': data}
        with open("data_file.json", "w") as write_file:
            json.dump(hey, write_file) # ���������� ����������������� ������������� �������
        with open("data_file.json", "r") as read_file:
            appdata = json.load(read_file)
        print(appdata)
        os.remove('data_file.json')
    task3()

if k == 4:
    def task4():
        import xml.etree.ElementTree as ET
        import os

        data1 = input()
        data2 = input()
        data3 = input()

        data_items = [
        {"first": data1, "second": data2, "third": data3}
        ] 

        root_node = ET.Element('root_node')

        for i, data_item in enumerate(data_items, 1):
            new1 = ET.SubElement(root_node, 'new1' + str(i))
            ET.SubElement(new1, 'first').text = data_item['first']
            ET.SubElement(new1, 'second').text = data_item['second']
            ET.SubElement(new1, 'third').text = data_item['third']

        tree = ET.ElementTree(root_node) # 
        tree.write('sample.xml')
    
        with open('sample.xml') as f:
            r = f.read()
            print(r)
        os.remove('sample.xml')
    task4()

if k == 5:
    def task5():
        import zipfile
        import os
        h = input()
        newzip = zipfile.ZipFile('new.zip', 'w') # ������ �����
        f = open("hi.txt", "w") # ������ ����
        f.write(h) # ���������� � ���� ������� h
        f.close()
        newzip.write("hi.txt") # ���������� ���� � �����
        os.remove("hi.txt") # ������� ���� ���� ��� ������
        newzip.extract("hi.txt") # ��������� �� ������
        newzip.close() # ��������� �����
        with open("hi.txt", "r") as f: # ��������� ������� �� ������������ ����� � �������
            r = f.read()
            print(r)
            f.close() # ��������� ����
        os.remove("new.zip") # ������� �����
        os.remove("hi.txt") # ������� ����
    task5()

if k > 5:
    print('error')
        

















   




