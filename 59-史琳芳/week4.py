#!/usr/bin/env python
# coding: utf-8

# In[1]:


def full_segment(sentence, word_dict):
    n = len(sentence)
    # 初始化动态规划数组
    dp = [0] * (n + 1)
    # 存储切分结果的列表
    result = []

    for i in range(1, n + 1):
        max_prob = 0
        best_cut = None

        for j in range(i):
            word = sentence[j:i]
            if word in word_dict and (dp[j] + word_dict[word] > max_prob):
                max_prob = dp[j] + word_dict[word]
                best_cut = j

        dp[i] = max_prob

        if best_cut is not None:
            result.append(sentence[best_cut:i])

    return result

# 字典
Dict = {"经常": 0.1, "经": 0.05, "有": 0.1, "常": 0.001, "有意见": 0.1, "歧": 0.001, "意见": 0.2, 
        "分歧": 0.2, "见": 0.05, "意": 0.05, "见分歧": 0.05, "分": 0.1}

# 待切分文本
sentence = '经常有意见分歧'

# 执行全切分
result = full_segment(sentence, Dict)

# 输出结果
print(result)


# In[ ]:




