#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sklearn.metrics import pairwise_distances_argmin_min

def main():
    model = load_word2vec_model("model.w2v")
    sentences = load_sentence("titles.txt")
    vectors = sentences_to_vectors(sentences, model)

    n_clusters = int(math.sqrt(len(sentences)))
    print("指定聚类数量：", n_clusters)
    kmeans = KMeans(n_clusters)
    kmeans.fit(vectors)

    sentence_label_dict = defaultdict(list)
    for sentence, label in zip(sentences, kmeans.labels_):
        sentence_label_dict[label].append(sentence)
    
    # 计算每个类别中心
    cluster_centers = kmeans.cluster_centers_
    
    # 初始化存储类内距离的字典
    intra_distances = defaultdict(list)
    
    # 计算每个样本到所属类别中心的距离，并存储到字典中
    for label, centroid in enumerate(cluster_centers):
        indices = np.where(kmeans.labels_ == label)[0]
        distances = pairwise_distances_argmin_min(centroid.reshape(1, -1), vectors[indices], metric='euclidean')[1]
        for i, idx in enumerate(indices):
            intra_distances[label].append((sentences[idx], distances[i]))

    # 对每个类别的样本按照到类别中心的距离进行排序
    for label, distances in intra_distances.items():
        print("Cluster %s (Center: %s):" % (label, cluster_centers[label]))
        sorted_distances = sorted(distances, key=lambda x: x[1])
        for sentence, distance in sorted_distances[:10]:  # 取前10个样本
            print(sentence.replace(" ", ""), " Distance:", distance)
        print("---------")

if __name__ == "__main__":
    main()

