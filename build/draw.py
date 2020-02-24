from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import json
import random

colors = [
    "#ff0000", "#00ff00", "#0000ff", "#404040", "#ff00ff", "#00ffff", "#C0ff00", "#ffC000", "#ff00C0", "#000070", "#007000", "#700000",
]


def paint(ax, xs, ys, color, zs=None, marker='.'):
    if zs != None:
        ax.scatter(xs=xs, ys=ys, zs=zs, zdir='z', c=color, marker=marker)
    else:
        ax.scatter(x=xs, y=ys, c=color, marker=marker)


def readData():
    random.shuffle(colors)
    data = json.load(open("foo.json", mode="r", encoding="utf-8"))
    dimension = data["dimension"]
    clusters = []
    clusterCnt = 0
    for tmpRawCluster in data["clusters"]:
        tmpCluster = {"centroid": None, "xss": [],
                      "color": colors[clusterCnt % len(colors)]}
        if "centroid" in tmpRawCluster:
            tmpCluster["centroid"] = tmpRawCluster["centroid"]
        for i in range(0, dimension):
            tmpCluster["xss"].append([])
        if "points" in tmpRawCluster:
            for tmpRawPoint in tmpRawCluster["points"]:
                for j in range(0, len(tmpRawPoint)):
                    tmpCluster["xss"][j].append(tmpRawPoint[j])
        clusters.append(tmpCluster)
        clusterCnt += 1
    return {"dimension": dimension, "clusters": clusters}


def work():
    data = readData()
    fig = plt.figure()
    if data["dimension"] == 2:
        ax = fig.add_subplot(111)
        for cluster in data["clusters"]:
            if cluster["centroid"]:
                paint(ax, cluster["centroid"][0],
                      cluster["centroid"][1], "#000000", marker='^')
                paint(ax, cluster["xss"][0],
                      cluster["xss"][1], cluster["color"], marker=',')
    elif data["dimension"] == 3:
        ax = fig.add_subplot(111, projection='3d')
        for cluster in data["clusters"]:
            paint(ax, cluster["centroid"][0], cluster["centroid"]
                  [1], cluster["color"], cluster["centroid"][2], marker='^')
            paint(ax, cluster["xss"][0], cluster["xss"]
                  [1], cluster["color"], cluster["xss"][2], marker=',')
    plt.show()
    pass


if __name__ == "__main__":
    work()
