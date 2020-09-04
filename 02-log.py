class log:

    def info(self, message) :
        self.__message = message
        return self.__message
    
    def error(self, message) :
        self.__message = message
        return self.__message

    def notice(self, message) :
        self.__message = message
        return self.__message

    def warning(self, message) :
        self.__message = message
        return self.__message

    def debug(self, message) :
        self.__message = message
        return self.__message

    def alert(self, message) :
        self.__message = message
        return self.__message

    def critical(self, message) :
        self.__message = message
        return self.__message

    def emergency(self, message) :
        self.__message = message
        return self.__message


log = log()
print(log.info('INFO : This is an info message'))
print(log.error('ERROR: We cant divide any numbers by zero'))
print(log.notice('NOTICE: Someone loves your status.'))
print(log.warning('WARNING: Insufficient funds.'))
print(log.debug('DEBUG: This is debug message.'))
print(log.alert('ALERT: Achtung! Achtung!'))
print(log.critical('CRITICAL: Medic!! Weve got critical damages.'))
print(log.emergency('EMERGENCY: System hung. Contact system administrator immediately!'))

# print(rani.set_username("new Rani"))