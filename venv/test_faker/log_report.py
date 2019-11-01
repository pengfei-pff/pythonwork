import logging
import time
'''
日志类，传入msg信息
'''
class LogerInfo:
    def logger_info(self,msg,leve):
        #定义日志收集器
        my_logger = logging.getLogger()
        #设定级别
        my_logger.setLevel(leve)
        #创建自己的输出级别
        ch = logging.StreamHandler()
        ch.setLevel(leve)
        # 定义handler的输出格式
        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        ch.setFormatter(formatter)
        my_logger.addHandler(ch)
        #依据日志级别判断日志
        if leve == 'DEBUG':
            my_logger.debug(msg)
        elif leve == 'INFO':
            my_logger.info(msg)
        elif leve == 'CRITICAL':
            my_logger.critical(msg)
        #关闭渠道
        my_logger.removeHandler(ch)

    #收集日志函数
    def debug(self,msg):
        self.logger_info(msg,'DEBUG')
    def critical(self,msg):
        self.logger_info(msg,'CRITICAL')
    def info(self,msg):
        self.logger_info(msg,'INFO')

if __name__ == '__main__':
    LogerInfo().debug('debug')
    LogerInfo().info('info')
    LogerInfo().critical('critical')




