import configparser
class ReadConfig:
    @staticmethod
    def get_config(file_path,section,option):
        cf = configparser.ConfigParser()
        cf.read(file_path,encoding='utf-8')

        #读取配置文件的信息
        res = cf[section][option]
        return res

if __name__ == '__main__':
    res = ReadConfig.get_config('case.config','MODE','mode')
    print(res)


