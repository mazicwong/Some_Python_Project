import numpy as np
from sklearn.cluster import KMeans

def loadData(filepath):
    f = open(filepath,'r+')
    lines = f.readlines()
    retData = []
    retCityName = []
    for line in lines:
        items = line.strip().split()
        retCityName.append(items[0])
        # retData.append([float(items[i])] for i in range(1,len(items)))
        retData.append([float(items[i]) for i in range(1, len(items))])
    return retData,retCityName

if __name__ == '__main__':
    data,cityName = loadData('city.txt')
    km = KMeans(n_clusters=4) # 聚类中心
    label = km.fit_predict(data)  # 获取每一条数据的聚类标签
    expenses = np.sum(km.cluster_centers_, axis=1)
    CityCluster = [[], [], [], []]  # 城市按label分成簇
    for i in range(len(cityName)):
        CityCluster[label[i]].append(cityName[i])
    for i in range(len(CityCluster)):
        print("Expenses:%.2f" % expenses[i])
        print(CityCluster[i])