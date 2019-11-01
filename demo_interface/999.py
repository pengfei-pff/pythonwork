from faker import Faker

faker = Faker('zh_CN')
file_name = 'test.txt'#准备写入的文件
n = 0
while n < 100:
    n+=1 #每次执行后加1
    name = faker.name()
    phone_number = faker.phone_number()
    address = faker.address()
    company = faker.company()
    idCard = faker.ssn()
    fileContent = '姓名:%s'%name,'   身份证:%s'%idCard,'   手机号:%s'%phone_number,'   公司:%s'%company,'   地址:%s'%address+"\n"

    with open(file_name,'a',encoding='utf-8') as file:
        file.writelines(fileContent)
    print(fileContent)
