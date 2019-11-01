from faker import Faker

faker = Faker('ja_JP')
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




# print('name:', faker.name())
# print('address:', faker.address())
# print('company:',faker.company())
# print('credit:',faker.credit_card_provider())
# print('phone_number:',faker.phone_number())
# print('job:',faker.job())
# print('sentence:',faker.ipv4())
# print(faker.ssn())
# print('text:', faker.text())
