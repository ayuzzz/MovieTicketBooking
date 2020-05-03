class SqlUtility:
    def convertList(valuesList):
        stringList = ''
        for i in range(len(valuesList)):
            stringList += '(0,"' + str(valuesList[i].StartTime) + '","' + str(valuesList[i].EndTime) + '",' + str(valuesList[i].TheatreId) + ',' + str(valuesList[i].MovieId) + ',' + str(valuesList[i].RateOfTickets) + '),'

        resultList = stringList.rstrip(',')
        return resultList
